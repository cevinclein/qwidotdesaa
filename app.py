from flask import Flask, render_template
import requests
MyApp = Flask(__name__)

def get_data():
	urls = [
     "https://raw.githubusercontent.com/bwvisu/bwvisu.github.io/master/user-docs/getting-started.md",
     "https://raw.githubusercontent.com/bwvisu/bwvisu.github.io/master/user-docs/jupyter.md",
     "https://raw.githubusercontent.com/bwvisu/bwvisu.github.io/master/user-docs/paraview.md",
     "https://raw.githubusercontent.com/bwvisu/bwvisu.github.io/master/user-docs/vistle_get_started.md",
     "https://raw.githubusercontent.com/bwvisu/bwvisu.github.io/master/user-docs/firststeps_post_atom.md"
    ] 

	data = []
	for i in urls:
		data.append(requests.get(i).content.decode())

	return data


@MyApp.route("/")
def hello():
	return render_template('index.html', gitwiki=get_data())

if __name__ == "__main__":
	MyApp.run()
 	#MyApp.run(host="0.0.0.0", port=80)