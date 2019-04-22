import psycopg2
from utils.config import config
from news.db.populate_db import get_real_data
from news.db.anunturi_fii import get_announcements_fii
""" create tables in the PostgreSQL database"""


def create_tables():
    commands = [
       """
       DROP TABLE IF EXISTS news;
       """,
       """
       CREATE TABLE news (
         news_id SERIAL PRIMARY KEY,
         title VARCHAR(255),
         body VARCHAR,
         author_name VARCHAR(255),
           
          category VARCHAR(255),
          inserted_time TIMESTAMP DEFAULT now(),
          published_time TIMESTAMP
        )
        """
        # , """
        # INSERT INTO news(title, body, author_name, category)
        #     VALUES(E'aaaaa', E'Cretu Marian', E'MATERII');
        # """
        ]
    try:
        get_announcements_fii()
        commands += get_real_data()
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
        # if conn is not None:
        #     conn.close()


if __name__ == '__main__':
    create_tables()
