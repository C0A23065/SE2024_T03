from flask import Flask, render_template, request, redirect, url_for  
import sqlite3  
  
app = Flask(__name__)  
  
def init_db():  
    conn = sqlite3.connect('database.db')  
    c = conn.cursor()  
    c.execute('''  
        CREATE TABLE IF NOT EXISTS products (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            category TEXT NOT NULL  
        )  
    ''')  
    conn.commit()  
    conn.close()  
  
@app.before_request  
def setup():  
    init_db()   
  
@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        category = request.form['category']  
        conn = sqlite3.connect('database.db')  
        c = conn.cursor()  
        c.execute('INSERT INTO products (category) VALUES (?)', (category,))  
        conn.commit()  
        conn.close()  
        return redirect(url_for('index'))  
      
    conn = sqlite3.connect('database.db')  
    c = conn.cursor()  
    c.execute('SELECT * FROM products')  
    products = c.fetchall()  
    conn.close()  
      
    return render_template('index.html', products=products)  
  
if __name__ == '__main__':  
    app.run(debug=True)  