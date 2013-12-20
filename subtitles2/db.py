import sqlite3

FILENAME_PATH = 'corpus/index.db'

def create_db():
    conn = sqlite3.connect(FILENAME_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE CHUNKS (id INT, movie TEXT, start_sec INT, DIALOGUE TEXT)''')
    conn.commit()
    conn.close()

def add_chunk(movie, start_sec, dialogue):
    conn = sqlite3.connect(FILENAME_PATH)
    c = conn.cursor()
    top_id, = c.execute("SELECT max(id) FROM CHUNKS").next()
    c.execute("INSERT INTO CHUNKS VALUES (?,?,?,?);",(top_id + 1, movie, start_sec, dialogue))
    conn.commit()
    conn.close()


def summary_chunks():
    conn = sqlite3.connect(FILENAME_PATH)
    c = conn.cursor()
    number_of_entries = c.execute("SELECT count(id) FROM CHUNKS").next()
    query = c.execute("SELECT * FROM CHUNKS")
    print 'CHUNKS table | %d records' % number_of_entries
    for row in query:
        print "id: %d, title: %s, time: %d, text: %s" % row
    conn.commit()
    conn.close()

def interupt():
    conn = sqlite3.connect(FILENAME_PATH)
    conn.commit()
    conn.close()    
    




