from User import UserMst

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
        print(con)
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
