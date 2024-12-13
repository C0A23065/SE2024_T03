
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
    add_store_data('デニムパンツ', '服', 2999.99, 'ユニクロ')  
    add_store_data('Another Store Item', 'Category2', 1500.00, '無印良品')  