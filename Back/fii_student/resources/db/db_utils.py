import psycopg2
# from utils.config import config
from utils.config import config
""" create tables in the PostgreSQL database"""


def create_tables():
    commands = (
        """
        BEGIN;
         --
         -- Create model Resources
         --
         DROP TABLE IF EXISTS resources;
         CREATE TABLE "resources" (
             "log_id" serial NOT NULL PRIMARY KEY, 
             "title" varchar(128) NOT NULL, 
             "timestamp" timestamp with time zone NULL, 
             "url" text, 
             "path" text
         );
         COMMIT;
         """,
        """
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(1, 'Ghidul Studentului UAIC', null, 'http://www.uaic.ro/studenti/ghidul-studentului-uaic/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(2, 'Cum iti poti verifica notele', null, 'http://www.uaic.ro/studenti/cum-iti-poti-verifica-notele/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(3, 'Reprezentarea studentilor in structurile de conducere', null, 'http://www.uaic.ro/studenti/reprezentarea-studentilor-structurile-de-conducere-2/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(4, 'Orientare in Cariera, Insertie Profesionala si Alumni', null, 'http://www.uaic.ro/studenti/cariera/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(5, 'Burse', null, 'http://www.uaic.ro/studenti/burse/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(6, 'Cazare', null, 'http://www.uaic.ro/studenti/cazare/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(7, 'Mobilitati academice pentru studenti', null, 'http://www.uaic.ro/studenti/mobilitati-academice-pentru-studenti/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(8, 'Cantinele Universitatii', null, 'http://www.uaic.ro/studenti/cantinele-universitatii-alexandru-ioan-cuza/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(9, 'Servicii Medicale', null, 'http://www.uaic.ro/studenti/servicii-medicale/', null);
        INSERT INTO resources(log_id, title, timestamp, url, path)
            VALUES(10, 'Biblioteci', null, 'http://www.uaic.ro/studenti/biblioteci/', null);
        """
    )
    try:
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
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
