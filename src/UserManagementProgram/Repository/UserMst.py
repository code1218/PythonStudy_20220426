
class UserMst:
    usercode = None
    email = None
    name = None
    username = None
    password = None
    create_date = None
    update_date = None

    def toString(self):
        print(f"""
usercode = {self.usercode}
email = {self.email}
name = {self.name}
username = {self.username}
password = {self.password}
create_date = {self.create_date}
update_date = {self.update_date}
        """)