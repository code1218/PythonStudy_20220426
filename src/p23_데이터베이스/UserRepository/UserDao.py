from User import UserMst
import pymysql

class UserDao:

    pool = None

    def __init__(self, pool):
        self.pool = pool
        
    def test(self):
        con = self.pool.getConnection()
        self.pool.freeConnection(con)
    
    def getUserAll(self):
        userList = list()

        con = self.pool.getConnection()
        sql = """
            select 
                * 
            from 
                user_mst
        """
        cur = con.cursor()
        cur.execute(sql)
        rs = cur.fetchall()
        for rsUser in rs:
            user = UserMst()
            user.setUserMstAllArgs(
                usercode=rsUser[0],
                email=rsUser[1],
                name=rsUser[2],
                username=rsUser[3],
                password=rsUser[4],
                create_date=rsUser[5],
                update_date=rsUser[6]
            )
            userList.append(user)
        self.pool.freeConnection(con)
        return userList

    def getUserByUsername(self, username):
        con = self.pool.getConnection()
        cur = con.cursor(pymysql.cursors.DictCursor)
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
        self.pool.freeConnection(con)

    def deleteUserByUsername(self, username):
        key = 'username'
        con = self.pool.getConnection()
        cur = con.cursor(pymysql.cursors.DictCursor)
        sql = f"""
            delete
            from
                user_mst
            where
                {key} = '{username}'
        """
        cur.execute(sql)
        con.commit()
        self.pool.freeConnection(con)