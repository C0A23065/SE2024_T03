# database.dbに店側のデータを追加するプログラム

import sqlite3  
  
def add_store_data(name, category, price, store_name):  
    try:  
        conn = sqlite3.connect('database.db')  
        c = conn.cursor()  
          
        c.execute(  
            'INSERT INTO store_data (name, category, price, store_name) VALUES (?, ?, ?, ?)',  
            (name, category, price, store_name)  
        )  
          
        conn.commit()  
  
    except sqlite3.Error as e:  
        print(f"An error occurred: {e}")  
  
    finally:  
        if conn:  
            conn.close()  
  
if __name__ == '__main__':  
    # 例として店側のデータを追加  
    # 追加したときは/SE2024_T03/progectでpython3 init_db.pyでデータベースを初期化してから実行すること
    # 実行コマンドはpython3 add_store_data.py
    add_store_data('デニムパンツ', '服', 2999.99, 'ユニクロ')  
    add_store_data('カップラーメンセット', '食品', 500, 'スーパー')  