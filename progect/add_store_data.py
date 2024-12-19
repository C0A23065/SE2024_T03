# database.dbに店側のデータを追加するプログラム

import sqlite3  
  
def add_store_data(name, category, price, store_name, photo_path):  
    try:  
        conn = sqlite3.connect('database.db')  
        c = conn.cursor()  
          
        c.execute(  
            'INSERT INTO store_data (name, category, price, store_name, photo_path) VALUES (?, ?, ?, ?, ?)',  
            (name, category, price, store_name, photo_path)  
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
    add_store_data('デニムパンツ', '服', 1000, 'ユニクロ', "static/photos/denim_pants.jpg")  
    add_store_data('カップラーメンセット', '食品', 500, 'スーパー', "static/photos/cup_ramen.jpg") 
    add_store_data('フリスビー', 'その他', 200, 'XEBIO', "static/photos/frisbee.jpg")
    add_store_data('マンガ', '本', 100, '有隣堂', "static/photos/manga.jpg") 
    add_store_data('マウス', '電子機器', 500, 'ヤマダデンキ', "static/photos/mouse.jpg")
    add_store_data('サカバンバスピス', 'その他', 1000000, '博物館のお土産コーナー', "static/photos/sakabanbasupisu.png")
    add_store_data('靴', 'その他', 2000, 'XEBIO', "static/photos/shoes.jpg")
    add_store_data('充電器', '電子機器', 1500, 'ヨドバシカメラ', "static/photos/juudennko-do.jpg")
    add_store_data('目覚まし時計', '雑貨', 200, '無印良品', "static/photos/alarm clock.jpg")
    add_store_data('カードケース', '雑貨', 500, '無印良品', "static/photos/cardcase.jpg")
    add_store_data('タンス', '家具', 30000, 'ニトリ', "static/photos/chest.jpg")
    add_store_data('辞書', '本', 3000, '有隣堂', "static/photos/dictionary.png")
    add_store_data('ファンデーション', '美容', 300, 'PRAZA', "static/photos/faundation.png")
    add_store_data('パーカー', '服', 3000, 'ユニクロ', "static/photos/pa-ka-.png")
    add_store_data('食器棚', '家具', 30000, 'ニトリ', "static/photos/syokkidana.png")

