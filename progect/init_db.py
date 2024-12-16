# データベースの初期化を行うプログラム
# データの追加を行うたびに初期化すること

import sqlite3  
  
def init_db():  
    conn = sqlite3.connect('database.db')  
    c = conn.cursor()  
  
    # テーブルの作成と初期データ挿入
    # store_dataテーブルの作成  
    c.execute('DROP TABLE IF EXISTS store_data')  
    c.execute('''  
        CREATE TABLE store_data (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT NOT NULL,  
            category TEXT NOT NULL,  
            price REAL,  
            store_name TEXT  
        )  
    ''')  
  
    # ユーザー登録テーブルの作成  
    c.execute('DROP TABLE IF EXISTS products')  
    c.execute('''  
        CREATE TABLE IF NOT EXISTS products (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT NOT NULL,  
            category TEXT NOT NULL,  
            photo_path TEXT NOT NULL  
        )  
    ''')  
  
    # カテゴリテーブルの作成  
    c.execute('DROP TABLE IF EXISTS categories')  
    c.execute('''  
        CREATE TABLE IF NOT EXISTS categories (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            category TEXT NOT NULL  
        )  
    ''')  
  
    # デフォルトのカテゴリを挿入  
    default_categories = [('服',), ('食品',), ('電子機器',)]  
    c.executemany('INSERT INTO categories (category) VALUES (?)', default_categories)  
  
    conn.commit()  
    conn.close()  
  
if __name__ == '__main__':  
    init_db()  