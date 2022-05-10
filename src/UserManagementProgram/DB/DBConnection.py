import pymysql

class DBConnection:

    @staticmethod
    def getConnection():
        db = "python_junil"

        print(f"[{db}] 데이터 베이스를 연결합니다.")
        con = pymysql.connect(
            host = "127.0.0.1",
            port = 8001,
            user = "root",
            password = "toor",
            database = db,
            charset = "utf8"
        )
        return con

    @staticmethod
    def freeConnection(connect):
        connect.close()