from psycopg2 import pool
connection_pool = pool.SimpleConnectionPool(
    1,
    1,
    user='nkemakolam',
    password='ghosts123',
    database='learning',
    host='localhost'
)

class CursorFromConnectFromPool:
    #create a connection 
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    #pick a connection from the pool
    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor
    # exiting the connection to releae resource
    def __exit__(self,exc_type,exc_value,exc_tb):
        if exc_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)