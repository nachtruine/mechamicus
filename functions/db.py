import psycopg2
import sys
import urllib.parse as urlparse

DATABASE_URL = sys.argv[3]


def connect():
    try:
        url = urlparse.urlparse(DATABASE_URL)

        conn = psycopg2.connect(
            dbname=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        return conn
    except:
        pass
