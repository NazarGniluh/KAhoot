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


    def add_qiuz(self, id, title, description):
        cursor = self.conection.cursor()
        cursor.execute(f"INSERT INTO Qiuz(id, title, description) VALUES (?, ?, ?)",
                       [id, title, description])
        self.conection.commit()
        cursor.close()

    def add_question(self, id, quiz_id, content):
        cursor = self.conection.cursor()
        cursor.execute(f"INSERT INTO Question(id, quiz_id, content) VALUES (?, ?, ?)",
                       [id, quiz_id, content])
        self.conection.commit()
        cursor.close()


    def get_quizzer(self):
        cursor = self.conection.cursor()
        cursor.execute("SELECT * FROM Qiuz")
        res = cursor.fetchall()
        cursor.close()
        return res


    def get_questions(self, quiz_id):
        cursor = self.conection.cursor()
        cursor.execute("SELECT * FROM Question WHERE quiz_id = ?", [quiz_id])
        res = cursor.fetchall()
        cursor.close()
        return res


    def get_options(self, question_id):
        cursor = self.conection.cursor()
        cursor.execute("SELECT * FROM Options WHERE question_id = ?", [question_id])
        res = cursor.fetchall()
        cursor.close()
        return res


    def add_options(self, id, question_id, content, is_correct):
        cursor = self.conection.cursor()
        cursor.execute(f"INSERT INTO Options(id, question_id, content, is_correct) VALUES (?, ?, ?, ?)",
                       [id, question_id, content, is_correct])
        self.conection.commit()
        cursor.close()
