from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route("/")
def hello():
    return "Hallo"


@app.route("/about")
def about():
    return "Ich bin Linus"


@app.route("/hallo")
def hallo():
    return "Hallo"


@app.route("/hallo/<name>")
def hallo_name(name):
    return "Hallo %s" % name

if __name__ == "__main__":
    app.run()