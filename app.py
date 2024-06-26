from flask import Flask, render_template, send_file, Response
import requests
import markdown
from pathlib import Path
import json
import io

from pymdownx.blocks import BlocksExtension
from pymdownx.blocks.block import Block
import xml.etree.ElementTree as etree

###### Add custom element blocks #######

# hstack --> horizontal alignment block:
""" 
/// hstack
some content which will be alligned horizontally
///
"""

class HstackBlock(Block):
    NAME = 'hstack'
    def on_create(self, parent):
        return etree.SubElement(parent, 'div', id="hstack")

class HstackBlockExtension(BlocksExtension):
    def extendMarkdownBlocks(self, md, block_mgr):
        block_mgr.register(HstackBlock, self.getConfigs())

def makeExtension(*args, **kwargs):
    """Return extension."""
    return HstackBlockExtension(*args, **kwargs)

###### Add custom element blocks #######

MyApp = Flask(__name__)

"""
This app reads out a git repo with md files and display it
in the wiki page. As an alternative also a local dir can be 
read out.

This file is placed among the other .md files in the repo 
or in the local directory:

[1] doc-config.json:

{
    "doc_title":"set the title of the Wiki",
    "section_names": {
        "the filename of the .md file in the repo or dir":"the section name displayed in the Wiki",
        "examplefileNamw (without .md)":"Example file name"
    }
}
	
"""

# Python markdown is used to convert markdown files into html
# pip install markdown
# pip install pymdown-extensions
# pip install Pygments

# Markdown flavor: https://daringfireball.net/projects/markdown/
# Python Markdown: https://python-markdown.github.io/
# Extensions flavor: https://facelessuser.github.io/pymdown-extensions/extras/slugs/

extension_configs = {
	"pymdownx.emoji": {
        "options": {
            "attributes": {
                "align": "absmiddle",
                "height": "20px",
                "width": "20px"
            }  
        }
    },
	"pymdownx.tasklist": {
		"custom_checkbox":"True"
	}
}

# specify the root path of the repo where alle the .md filese are -> no / at the end of the url
REPO_URL = "<A public repo is needed>"
# Use Local files instead and ignore REPO_URL path
ENABLE_REMOTE = False
# Only applies if ENABLE_REMOTE = False
# All .md notes must be stored in this dir if if ENABLE_REMOTE = False
LOCAL_PATH = Path("./local_notes")
# For images create a images dir in the LOCAL_PATH dir
# in markdown reference to images with (no leading /)APP_NAME/IMAGES_DIR_NAME/pic.something
IMAGES_DIR_NAME = "images"
# Must be the name of the root directory for ondemand
APP_NAME = "bwVisu-Wiki"

def get_data():
	# Get the .md data locally or remotely
	if ENABLE_REMOTE:
		doc_config = requests.get(f"{REPO_URL}/doc-config.json").json()
	else:
		with open(LOCAL_PATH/"doc-config.json", "r") as config_file:
			doc_config = json.loads(config_file.read())
	
	section_num = len(doc_config["section_names"])
	sections = []
	doc_title = doc_config["doc_title"]
	
	data = []
 
	# We will use some extensions for python markdown, that we can for example render math, create tables
	# and more
	for key, value in doc_config["section_names"].items():
		sections.append(value)
		if ENABLE_REMOTE:
			mardown_page = requests.get(f"{REPO_URL}/{key}.md").content.decode()
		else:
			with open(LOCAL_PATH/f"{key}.md", "r") as md_file:
				mardown_page = md_file.read()
  
		data.append(markdown.markdown(mardown_page, 
        extension_configs=extension_configs, extensions=['pymdownx.extra', 'toc', 'nl2br', 'pymdownx.b64', 
                                                         'pymdownx.highlight', 'pymdownx.keys', 'pymdownx.tasklist', 'pymdownx.arithmatex',
                                                         'pymdownx.caret', 'pymdownx.emoji', 'pymdownx.magiclink', 'pymdownx.saneheaders',
                                                         'pymdownx.smartsymbols', 'pymdownx.tilde', 'pymdownx.mark', HstackBlockExtension()]))

	return data, section_num, sections, doc_title
   

@MyApp.route("/")
def site_root():
	dt, sec_n, secs, dc_tit = get_data()
	return render_template('index.html', gitwiki=dt, section_num=sec_n, sections=secs, doc_title=dc_tit)

@MyApp.route(f"/{IMAGES_DIR_NAME}/<image_name>")
@MyApp.route(f"/{APP_NAME}/{IMAGES_DIR_NAME}/<image_name>")
def send_images(image_name):
	if ENABLE_REMOTE:
		# We only want to load images for security reasons
		r = requests.get(f"{REPO_URL}/{IMAGES_DIR_NAME}/{image_name}")
		if ".svg" in image_name:
			return Response(r.content.decode(), mimetype="image/svg+xml")
		elif ".png" in image_name:
			return send_file(io.BytesIO(r.content), mimetype="image/png")
		elif ".jpg" in image_name or ".jpeg" in image_name:
			return send_file(io.BytesIO(r.content), mimetype="image/jpeg")
		elif ".gif" in image_name:
			return send_file(io.BytesIO(r.content), mimetype="image/gif")
		else:
			return ""
	else:
 		return send_file(LOCAL_PATH/f"{IMAGES_DIR_NAME}"/f"{image_name}")

if __name__ == "__main__":
	MyApp.run()