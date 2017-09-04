import sqlite3

# TODO -> USE SQLITE INSTEAD OF POSTGRES


class DB:

    @staticmethod
    def insert(data):

        connection = sqlite3.connect("crawler_data.db")
        cursor = connection.cursor()
        #name, download_link, download_date, origin, total_downloads, week_downloads, version, hash, path
        cursor.execute("""INSERT INTO data(pname, download_link, download_date, origin, total_downloads, week_downloads,
                          version, hash, path) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
        connection.commit()
        connection.close()

    @staticmethod
    def select():

        connection = sqlite3.connect("crawler_data.db")
        cursor = connection.cursor()
        #name, download_link, download_date, origin, total_downloads, week_downloads, version, hash, path
        cursor.execute("""SELECT download_link FROM data""")
        data = cursor.fetchall()
        connection.commit()
        connection.close()

        return data