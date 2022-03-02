#!/usr/bin/python

import psycopg2
from config import config


def connect():
    """Koneksi ke PostgreSQL Database server"""
    conn = None
    try:
        params = config()
        print('Menghubungkan ke PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Koneksi Database telah ditutup.')


if __name__ == '__main__':
    connect()
