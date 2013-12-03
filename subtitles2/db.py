import sqlite3

def create_db():
    conn = sqlite3.connect('../corpus/index.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE CHUNKS (id INT, movie TEXT, start_sec INT, DIALOGUE TEXT)''')
    conn.commit()
    conn.close()


def add_chunk(movie, start_sec, dialogue):
    conn = sqlite3.connect('../corpus/index.db')
    c = conn.cursor()
    c.execute("INSERT INTO CHUNKS VALUES (?,?,?,?)",(1, movie, start_sec, dialogue))
    conn.commit()
    conn.close()




