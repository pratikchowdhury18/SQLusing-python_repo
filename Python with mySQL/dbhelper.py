import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='Pratik18*',database='pythontest')
        query='create table if not exists user(userID int primary key, userName varchar(15), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created')

    def insert_user(self,userid,username,phone):
        query = f"insert into user(userID,userName,phone) values({userid},'{username}','{phone}')"
        print(query)
        cur=self.con.cursor()
        cur.execute(query)

        print('user saved to db')

    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userID:", row[0])
            print("Username:", row[1])
            print("phone:", row[2])
            print()
            print()

    def fetch_one(self, userid):
        query=f"select * from user where userid={userid}"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userID:", row[0])
            print("Username:", row[1])
            print("phone:", row[2])

    def delete_user(self,userid):
        query=f"delete from user where userid={userid}"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")

    def update_user(self, userid, username, phone):
        query=f"update user set username='{username}', phone='{phone}' where userid={userid}"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")