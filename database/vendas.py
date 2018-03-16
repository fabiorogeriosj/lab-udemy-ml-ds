from db import DB

def db_vendas():
    return DB(username='root', password='root', dbname='syspedidos', hostname='localhost', dbtype='mysql')