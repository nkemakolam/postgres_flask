from psycopg2 import pool

class Database:
    connection_pool = None
    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(
                                                        1,
                                                        10,
                                                        user='nkemakolam',
                                                        password='ghosts123',
                                                        database='learning',
                                                        host='localhost'
                                                    )

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()
    @classmethod
    def return_connection(cls, connection):
        return cls.connection_pool.putconn(connection)
    classmethod
    def close_all_connection(cls):
        Database.connection_pool.closeall()

class CursorFromConnectFromPool:
    #create a connection 
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    #pick a connection from the pool
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    # exiting the connection to releae resource
    def __exit__(self,exc_type,exc_value,exc_tb):
        if exc_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)