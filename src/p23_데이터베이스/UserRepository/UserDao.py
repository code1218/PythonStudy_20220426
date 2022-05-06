class UserDao:

    pool = None

    def __init__(self, pool):
        self.pool = pool
        
    def test(self):
        con = self.pool.getConnection()
        self.pool.freeConnection(con)
    