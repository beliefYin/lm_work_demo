import tkinter as tk
import sqlite3
from passlib.hash import sha256_crypt
import tkinter.messagebox as messbox

def encrypt_password(password):
	return sha256_crypt.hash(password)

class Admin():
	def __init__(self, root):
		self.root = root
		self.root.geometry('300x200')
		self.username = tk.StringVar()
		self.password = tk.StringVar()
		self.page = tk.Frame(self.root)
		self.page.pack()
		tk.Label(self.page, text="添加账号").grid(row=0)

		tk.Label(self.page, text="账号：").grid(row=1,column=0)
		tk.Entry(self.page, textvariable=self.username).grid(row=1,column=1)

		tk.Label(self.page, text="密码：").grid(row=2,column=0)
		tk.Entry(self.page, textvariable=self.password).grid(row=2,column=1)

		tk.Button(self.page, text="添加",command=self.add_user).grid(row=3)
		
	def add_user(self):
		db = sqlite3.connect('app.db')
		connect = db.cursor()
		cursor = connect.execute('SELECT username FROM account WHERE username="%s" LIMIT 1'%self.username.get())
		isExist = False
		for row in cursor:
			isExist = True
		if isExist:
			messbox.showinfo(title="错误", message="已经存在这个账号了")
		else:
			encryptedPw = encrypt_password(self.password.get())
			connect.execute('INSERT INTO account (username,password) VALUES ("%s", "%s");'%(self.username.get(), encryptedPw))
			db.commit()
			messbox.showinfo(title="成功", message="添加账号成功")
		db.close()


def create_db():
	db = sqlite3.connect('app.db')
	connect = db.cursor()
	connect.execute('''CREATE TABLE IF NOT EXISTS account
		(id integer PRIMARY KEY autoincrement,
		username char(128) NOT NULL,
		password char(128) NOT NULL
		);''')
	db.commit()
	db.close()

app = tk.Tk()
def exit(event):
	app.destroy()
def main():
	create_db()
	app.title("管理员")
	app.bind('<Escape>' , exit)
	Admin(app)
	app.mainloop()

if __name__ == '__main__':
	main()
