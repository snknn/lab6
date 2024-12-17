from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
@app.route('/') 
def index():    

  connect = sqlite3.connect('sqlite_python.db') 
  cursor = connect.cursor() 
  cursor.execute('SELECT * FROM podarki') 

  items = cursor.fetchall() 
  return render_template('rows.html', items=items)

if __name__ == '__main__':
  app.run(host='0.0.0.0')