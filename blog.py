from flask import *
import sqlite3
app = Flask(__name__)


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
        conn.execute("insert into posts (titel,inhalt) Values (?,?)", (titel, inhalt) )
        conn.commit()
        conn.close()
        return "Erfolgreich gepostet"

    return render_template('blog-post.html')


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