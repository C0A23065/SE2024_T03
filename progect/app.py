
# from flask import Flask, render_template, request, redirect, url_for  
# import sqlite3  
# import os  
  
# app = Flask(__name__)  
  
# def get_db_connection():  
#     conn = sqlite3.connect('database.db')  
#     conn.row_factory = sqlite3.Row  
#     return conn  
  
# @app.route('/', methods=['GET', 'POST'])  
# def index():  
#     conn = get_db_connection()  
#     categories = conn.execute('SELECT category FROM categories').fetchall()  
  
#     if request.method == 'POST':  
#         name = request.form.get('name')  
#         category = request.form.get('category')  
#         photo = request.files.get('photo')                                                                                      
  
#         # デバッグ用の出力  
#         print(f"Name: {name}, Category: {category}, Photo: {photo}")  
  
#         if not name or not category or not photo:  
#             return "All fields are required", 400  
  
#         # 保存先ディレクトリが存在するか確認  
#         if not os.path.exists('static/photos'):  
#             os.makedirs('static/photos')  
  
#         photo_path = os.path.join('static/photos', photo.filename)  
#         photo.save(photo_path)  
  
#         try:  
#             # 'products' テーブルが存在するか確認  
#             conn.execute('INSERT INTO products (name, category, photo_path) VALUES (?, ?, ?)',  
#                          (name, category, photo_path))  
#             conn.commit()  
#         except sqlite3.Error as e:  
#             print(f"Database error: {e}")  
#             return "Database error", 500  
#         finally:  
#             conn.close()  
  
#         return redirect(url_for('match', category=category))  
  
#     conn.close()  
#     return render_template('index.html', categories=categories)  
  
# @app.route('/match/<category>')  
# def match(category):  
#     conn = get_db_connection()  
#     matching_store_data = conn.execute('SELECT * FROM store_data WHERE category = ?', (category,)).fetchall()  
#     conn.close()  
#     return render_template('match.html', store_items=matching_store_data, category=category)  
  
# if __name__ == '__main__':  
#     app.run(debug=True) 



from flask import Flask, render_template, request, redirect, url_for  
import sqlite3  
import os  
  
app = Flask(__name__)  
  
def get_db_connection():  
    conn = sqlite3.connect('database.db')  
    conn.row_factory = sqlite3.Row  
    return conn  
  
@app.route('/', methods=['GET'])  
def home():  
    return render_template('home.html')  
  
@app.route('/index', methods=['GET', 'POST'])  
def index():  
    conn = get_db_connection()  
    categories = conn.execute('SELECT category FROM categories').fetchall()  
  
    if request.method == 'POST':  
        name = request.form.get('name')  
        category = request.form.get('category')  
        photo = request.files.get('photo')  
  
        # デバッグ用の出力  
        print(f"Name: {name}, Category: {category}, Photo: {photo}")  
  
        if not name or not category or not photo:  
            return "All fields are required", 400  
  
        # 保存先ディレクトリが存在するか確認  
        if not os.path.exists('static/photos'):  
            os.makedirs('static/photos')  
  
        photo_path = os.path.join('static/photos', photo.filename)  
        photo.save(photo_path)  
  
        try:  
            # 'products' テーブルが存在するか確認  
            conn.execute('INSERT INTO products (name, category, photo_path) VALUES (?, ?, ?)',  
                         (name, category, photo_path))  
            conn.commit()  
        except sqlite3.Error as e:  
            print(f"Database error: {e}")  
            return "Database error", 500  
        finally:  
            conn.close()  
  
        return redirect(url_for('match', category=category))  
  
    conn.close()  
    return render_template('index.html', categories=categories)  
  
@app.route('/match/<category>')  
def match(category):  
    conn = get_db_connection()  
    matching_store_data = conn.execute('SELECT * FROM store_data WHERE category = ?', (category,)).fetchall()  
    conn.close()  
    return render_template('match.html', store_items=matching_store_data, category=category)  
  
# @app.route('/mypage')  
# def mypage():  
#     conn = get_db_connection()  
#     user_products = conn.execute('SELECT * FROM products').fetchall()  
#     conn.close()  
#     return render_template('mypage.html', products=user_products)

@app.route('/mypage')  
def mypage():  
    conn = get_db_connection()  
    user_products = conn.execute('SELECT * FROM products').fetchall()  
    conn.close()  
    return render_template('mypage.html', products=user_products)  
  
@app.route('/recommend')  
def recommend():  
    conn = get_db_connection()  
    recommended_items = conn.execute('SELECT * FROM store_data ORDER BY RANDOM() LIMIT 5').fetchall()  
    conn.close()  
    return render_template('recommend.html', items=recommended_items)  
  
if __name__ == '__main__':  
    app.run(debug=True)  
