import sqlite3

class BDManager:
    def __init__(self, db_name):
        self.conection = sqlite3.connect(db_name)



    def create_table(self):
        cursor = self.conection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Qiuz (
                id TNT PRIMARY KEY,
                title VARCHAR(255),
                description TEXT
            );
        """)
        cursor.execute("""
        
        CREATE TABLE Question (
                id TNT PRIMARY KEY,
                quiz_id INT,
                content TEXT
            );
        """)
        cursor.execute("""
        CREATE TABLE Options (
                id TNT PRIMARY KEY,
                question_id INT,
                content TEXT,
                is_correct BOOLEAN
            );
        """)
        self.conection.commit()