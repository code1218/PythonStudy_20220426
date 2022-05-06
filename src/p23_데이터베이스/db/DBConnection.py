import pymysql

class DBConnectionPy:
    host = "127.0.0.1"
    port = 8001
    user = "root"
    password = "toor"
    database = "python_junil"
    charset = "utf8"

    def getConnection(self):
        print(f"[{self.database}] 데이터 베이스를 연결합니다.")
        con = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = self.charset
        )
        return con

    def freeConnection(self, connect):
        connect.close()