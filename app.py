from flask import Flask, render_template
import requests
import markdown

MyApp = Flask(__name__)

# pip install markdown
# pip install pymdown-extensions
# pip install Pygments

# Markdown flavor: https://daringfireball.net/projects/markdown/
# Python Markdown: https://python-markdown.github.io/
# Extensions flavor: https://facelessuser.github.io/pymdown-extensions/extras/slugs/

def get_data():
	repo_url = "https://raw.githubusercontent.com/cevinclein/bwviscodf/main"
	
	doc_config = requests.get(f"{repo_url}/doc-config.json").json()
	
	section_num = len(doc_config["section_names"])
	sections = doc_config["section_names"]
	
	data = []
	for i in range(section_num):
		mardown_page = requests.get(f"{doc_config['url_prefix']}/{doc_config['index_name']}{i}.md").content.decode()
		data.append(markdown.markdown(mardown_page, extensions=['pymdownx.extra', 'toc', 'nl2br', 'pymdownx.b64', 
                                                                'pymdownx.highlight', 'pymdownx.keys', 'pymdownx.tasklist', 'pymdownx.arithmatex',
                                                                'pymdownx.caret', 'pymdownx.emoji', 'pymdownx.magiclink', 'pymdownx.saneheaders',
                                                                'pymdownx.smartsymbols', 'pymdownx.tilde', 'pymdownx.tabbed', 'pymdownx.details']))

	return data, section_num, sections
   

@MyApp.route("/")
def hello():
	dt, sec_n, secs = get_data()
	return render_template('index.html', gitwiki=dt, section_num = sec_n, sections = secs)

if __name__ == "__main__":
	MyApp.run()