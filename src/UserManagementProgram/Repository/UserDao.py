from DB.DBConnection import DBConnection


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