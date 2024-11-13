from flask import Flask, send_file, abort
import mistune
import re
import sys
import os
from string import Template
import tomllib

app = Flask(__name__)


def render_md(content, path):
    front_content, md_content = content.split("---", maxsplit=1)
    front_matter = tomllib.loads(front_content.strip("\n"))
    _shell = Template(open("templates/_shell.html").read())

    main_html_content = mistune.html(md_content)
    return _shell.substitute(
        title=front_matter["title"],
        description=front_matter["description"],
        cover_image_url=front_matter.get("cover"),
        page_url=path,
        main_html_content=main_html_content,
    )


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    filepath = os.path.join("content", path)
    if os.path.isdir(filepath):
        filepath = os.path.join(filepath, "index.html")
    md_path = re.sub("\\.html$", ".md", filepath)
    if os.path.isfile(filepath):
        return send_file(filepath)
    elif os.path.exists(md_path):
        md_content = open(md_path).read()
        return render_md(md_content, path)
    else:
        abort(404)


if __name__ == "__main__":
    if sys.argv[1] == "dev":
        app.run(host="127.0.0.1", port=3141, debug=True, use_reloader=True)
