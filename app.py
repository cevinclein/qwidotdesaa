from flask import Flask, render_template
import requests
import markdown

MyApp = Flask(__name__)

# This app reads out a git repo with md files and display it
# in the wiki page

"""

[1] doc-config.json:

{
    "url_prefix":"url to the root of all .md files",
    "doc_title":"set the title of the Wiki",
    "section_names": {
        "the filename of the .md file in the repo":"the section name displayed in the Wiki",
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

def get_data():
	# specify the root path of the repo where alle the md filese are -> no / at the end of the url
	repo_url = "https://raw.githubusercontent.com/cevinclein/bwviscodf/main"
	
	# We have to create a file[1] doc-config.json in the repo next to the md files
	# In this file we can set section names an a title
	doc_config = requests.get(f"{repo_url}/doc-config.json").json()
	
	section_num = len(doc_config["section_names"])
	sections = []
	doc_title = doc_config["doc_title"]
	
	data = []
 
	# We will use some extensions for python markdown, that we can for example render math, create tables
	# and more
	for key, value in doc_config["section_names"].items():
		sections.append(value)
		mardown_page = requests.get(f"{doc_config['url_prefix']}/{key}.md").content.decode()
		data.append(markdown.markdown(mardown_page, extensions=['pymdownx.extra', 'toc', 'nl2br', 'pymdownx.b64', 
                                                                'pymdownx.highlight', 'pymdownx.keys', 'pymdownx.tasklist', 'pymdownx.arithmatex',
                                                                'pymdownx.caret', 'pymdownx.emoji', 'pymdownx.magiclink', 'pymdownx.saneheaders',
                                                                'pymdownx.smartsymbols', 'pymdownx.tilde', 'pymdownx.tabbed', 'pymdownx.details',
                                                                'pymdownx.mark']))

	return data, section_num, sections, doc_title
   

@MyApp.route("/")
def site_root():
	dt, sec_n, secs, dc_tit = get_data()
	return render_template('index.html', gitwiki=dt, section_num=sec_n, sections=secs, doc_title=dc_tit)

if __name__ == "__main__":
	MyApp.run()