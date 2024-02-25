from app.db_connector import DBConnector
from catalyst_count.settings import DATABASES


def get_connection():
    mysql_conn = DBConnector(host=DATABASES['default']['HOST'], port=DATABASES['default']['PORT'],
                             username=DATABASES['default']['USER'], password=DATABASES['default']['PASSWORD'],
                             database=DATABASES['default']['NAME'])
    return mysql_conn


def fetch_data(query):
    conn = get_connection()
    data = conn.select_query(query)
    conn.close_conn()
    return data


def update_data(query):
    conn = get_connection()
    conn.execute_single(query)
    conn.close_conn()


if __name__ == '__main__':
    query = 'select * from accounts'
    data = fetch_data(query)
    print(data)

