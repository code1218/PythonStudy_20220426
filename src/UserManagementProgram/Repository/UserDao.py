from DB.DBConnection import DBConnection
from Repository.UserMst import UserMst

class UserDao:

    def signup(self, user):
        con = DBConnection.getConnection()
        cur = con.cursor()
        sql = f"""
            insert into
                user_mst
            values(
                0,
                '{user.email}',
                '{user.name}',
                '{user.username}',
                '{user.password}',
                '{user.decodeKey}',
                now(),
                now()
            )
        """
        cur.execute(sql)
        con.commit()
        DBConnection.freeConnection(con)

    def getUserByUsername(self, username):
        con = DBConnection.getConnection()
        cur = con.cursor()
        sql = f"""
            select
                *
            from
                user_mst
            where
                username = '{username}'
        """
        cur.execute(sql)
        rs = cur.fetchone()

        user = UserMst()
        user.usercode = rs[0]
        user.email = rs[1]
        user.name = rs[2]
        user.username = rs[3]
        user.password = rs[4]
        user.decodeKey = rs[5]
        user.create_date = rs[6]
        user.update_date = rs[7]

        DBConnection.freeConnection(con)

        return user
