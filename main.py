from flask import Flask
from flask import render_template, request, redirect, url_for
import sqlite3
 
try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
 
    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)
 
    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
 
    # Close the cursor
    cursor.close()
 
# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)
 
# Close DB Connection irrespective of success
# or failure
finally:
   
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Betsy Webshop")

@app.route("/login")
def login():
    username = request.args.get("username", "")

    if username != "":
        return redirect(url_for("profile", name=username))
        
    return render_template("login.html", title="Betsy Webshop | Login")

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", title="Betsy Webshop | Profile", name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)