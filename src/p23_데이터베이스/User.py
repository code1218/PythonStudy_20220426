class UserMst:
    usercode = None
    email = None
    name = None
    username = None
    password = None
    create_date = None
    update_date = None

    def __init__(self):
        pass

    def setUserMstAllArgs(self, 
    usercode, email, name, username, password,
    create_date, update_date):
        self.usercode = usercode
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.create_date = create_date
        self.update_date = update_date