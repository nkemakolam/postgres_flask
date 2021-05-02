from psycopg2 import pool
connection_pool = pool.SimpleConnectionPool(
    1,
    1,
    user='nkemakolam',
    password='ghosts123',
    database='learning',
    host='localhost'
)

class ConnectFromPool:
    #create a connection 
    def __init__(self):
        self.connection = None
    
    #pick a connection from the pool
    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection
    # exiting the connection to releae resource
    def __exit__(self,exc_type,exc_value,exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)