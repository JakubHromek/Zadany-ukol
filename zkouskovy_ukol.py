from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
from ddgs import DDGS

app = Flask(__name__)
app.secret_key = "nejaky-dlouhy-nahodny-tajny-retezec"

@app.route("/", methods=["GET", "POST"])
def search_on_google():
    print("Moreeee")
    if request.method == "POST":
        print("More")
        text = request.form["q"]
        with DDGS() as ddgs:
            results = list(ddgs.text(text, max_results=10))
        save_to_xml_file(results, "results.xml")


    print("AHoooj")
    return render_template("zkouskovy_ukol.html")

def save_to_xml_file(results, name):
    root = ET.Element("results")

    for i, a in enumerate(results, start = 0):
        print(a)
        result = ET.SubElement(root, "result")
        title = ET.SubElement(result, "title")
        title.text = a["title"]
            
        href = ET.SubElement(result, "href")
        href.text = a["href"]

        body = ET.SubElement(result, "body")
        body.text = a["body"]

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ", level=0)
    tree.write(name)

if __name__ == '__main__':
    app.run(debug=False)