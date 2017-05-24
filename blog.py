from flask import *
import sqlite3
app = Flask(__name__)


@app.route("/game")
@app.route("/game/")
def game():
    return render_template('basic.html')


@app.route("/play")
def play():
    return "PLAY!"


@app.route("/spiel")
def spiel():
    return render_template('spiel.html')


@app.route("/feld")
def feld():
    return render_template('feld.html')


@app.route("/hallo/")
@app.route("/hallo/<name>")
def hallo(name=None):
    return render_template('hello.html', name=name)


@app.route("/blog/post", methods=['GET', 'POST'])
@app.route("/blog/post/", methods=['GET', 'POST'])
def inp():
    if request.method == 'POST':
        titel = request.form['titel']
        inhalt = request.form['inhalt']
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("insert into posts (titel,inhalt) Values (?,?)", (titel, inhalt) )
        cur.fetchall()
        number = cur.lastrowid
        conn.commit()
        conn.close()
        return redirect(url_for('out', number=number))

    return render_template('blog-post.html')


@app.route("/blog/edit", methods=['GET', 'POST'])
def edit2():
    if request.method == 'POST':
        number = request.form['number']
        return redirect(url_for('edit', number=number))
    return render_template('edit2')


@app.route("/blog/edit/<number>", methods=['GET', 'POST'])
@app.route("/blog/edit/<number>/", methods=['GET', 'POST'])
def edit(number=None):
    if request.method == 'POST':
        return ""
    return render_template('edit')


@app.route("/blog")
@app.route("/blog/")
@app.route("/blog/<number>/")
@app.route("/blog/<number>")
def out(number=None):
    post = 0
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from posts")
    rows = cur.fetchall()
    try:
        number = int(number)
        row = rows[number-1]
        rows = [row]
        post = number
    except:
        pass
    conn.close()
    return render_template('blog-all.html', rows=rows, post=post)

if __name__ == "__main__":
    app.run()