import psycopg2
from time import sleep


class DBConnector(object):
    def __init__(self, host, username, password, port=3306, database=None):
        self.host = host
        self.port = port
        self.user = username
        self.passwd = password
        self.database = database
        self.db = self.get_connection()

    def __del__(self):
        if self.db:
            self.db.close()

    def close_conn(self):
        if self.db.status:
            self.db.close()

    def get_connection(self):
        for i in range(0, 5):
            try:
                db = psycopg2.connect(host=self.host, port=self.port, user=self.user,
                                     password=self.passwd)
                return db
            except psycopg2.Error as e:
                print(str(e))
                print('Unable to connect to the database. Retrying...... {0}'.format(i+1))
                sleep(2)
        print('Failed to establish connection after 5 attempts.')
        raise psycopg2.Error

    def execute_single(self, query):
        try:
            self.db.autocommit(False)
            cursor = self.db.cursor()
            cursor.execute(query)
            cursor.close()
            self.db.commit()
            self.db.autocommit(True)
            return True
        except psycopg2.Error as e:
            print('Failed execute_single.... Rolling Back.')
            self.db.rollback()
            self.db.autocommit(True)
            raise ValueError(str(e))

    def select_query(self, query):
        data = list()
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            if cursor.rowcount > 0:
                data = [record for record in cursor.fetchall()]
            cursor.close()
            return data
        except psycopg2 as e:
            cursor.close()
            print('Failed execute_single.... Rolling Back.')
            self.db.rollback()
            self.db.autocommit(True)
            raise ValueError(str(e))
