import sqlite3 as lite
import os
class DatabaseManager(object):

    def __init__(self, path):
        self.conn = lite.connect(path)
        self.conn.commit()
        self.cur = self.conn.cursor()
        
        self.create_tables()
        self.make_used_all_deleted_image()

    def create_tables(self):
        self.query('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, profile TEXT, name TEXT, date TEXT, is_used INTEGER DEFAULT 0)')
        
    def query(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()
    
    def make_used_all_deleted_image(self):
        
        for image_data in self.fetchall("SELECT id, name FROM images WHERE is_used = 0"):
            if not os.path.exists("images/" + image_data[1]):
                self.query("UPDATE images SET is_used = 1 WHERE is_used = 0 AND name NOT IN (SELECT name FROM images WHERE is_used = 1)")
    
    def set_image_as_used(self, image_id):
        """Mark an image as used by setting is_used=1 for the given image ID."""
        self.cur.execute("UPDATE images SET is_used = 1 WHERE id = ?", (image_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

