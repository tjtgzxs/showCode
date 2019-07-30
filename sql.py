import mysql.connector
import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB,auth_plugin='mysql_native_password')
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert(cls, table, **kw):
        sql_key = ""
        sql_value = ""
        for key, value in kw.items():
            sql_key += "`" + str(key) + "` "
            sql_value += str(value)
        sql = "INSERT INTO " + str(table) + "  (" + sql_key + ") " \
              + " VALUES ('" + str(sql_value) + "') "
        dd=1
        cur.execute(sql)
        cnx.commit()
