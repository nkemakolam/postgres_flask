import  psycopg2
def connect():
    return psycopg2.connect(user='nkemakolam',password='ghosts123',database='learning',host='localhost') 