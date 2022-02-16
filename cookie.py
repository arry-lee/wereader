import sqlite3


class ReadSqlite(object):
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.cookies = dict()

    def read_cookie(self):
        try:
            self.cursor.execute("select name,value from cookies;")
            cookies = self.cursor.fetchall()
            for key, value in cookies:
                self.cookies[key] = value
        except Exception:
            raise FileNotFoundError("Cookie Not Found")
        self.cursor.close()
        self.conn.close()
        return self.cookies


def read_cookie_from_path(path):
    sqlite = ReadSqlite(path)
    return sqlite.read_cookie()
