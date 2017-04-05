from flask import Flask, session, redirect, url_for, escape, request
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


@app.route('/output', methods=['GET', 'POST'])
def out():
    if request.method == 'POST':
        if request.form['submit'] == 'Zurück zur Namenseingabe':
            return redirect(url_for('inp'))
        elif request.form['submit'] == 'Bestätige':
            session['gefuehl'] = request.form['text']
            return redirect(url_for('gefuehl'))
        else:
            pass
    if 'text' in session:
        return '''
            <form method="post">
                <br />
                <center><input type=submit name=submit value="Zurück zur Namenseingabe">
                <p>Hallo %s, wie geht es dir?
                <p><input type=text name=text>
                <p><input type=submit name=submit value=Bestätige>
            </form>
        ''' % escape(session['text'])
    redirect(url_for('inp'))


@app.route("/input", methods=['GET', 'POST'])
def inp():
    if request.method == 'POST':
        session['text'] = request.form['text']
        return redirect(url_for('out'))
    return '''
        <form method="post">
            <br />
            <br />
            <center>Wie heißt du?
            <p><input type=text name=text>
            <p><input type=submit value=Bestätige>
        </form>
    '''


@app.route("/wie_geht's", methods=['GET', 'POST'])
def gefuehl():
    if request.method == 'POST':
        if request.form['submit'] == 'Zurück zur Namenseingabe':
            return redirect(url_for('inp'))
        elif request.form['submit'] == 'Zurück zur Begrüßung':
            return redirect(url_for('out'))
        else:
            pass
    if 'text' in session:
        return '''
        <form method="post">
                <br />
                <center><input type=submit name=submit value="Zurück zur Namenseingabe">
                <p><input type=submit name=submit value="Zurück zur Begrüßung">
                <p>Cool, %s mir geht es auch %s
            </form>
        ''' % (escape(session['text']),escape(session['gefuehl']))

app.secret_key = None

if __name__ == "__main__":
    app.run()
