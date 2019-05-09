import tkinter as tk
from login import Login
import sqlite3


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
	app.title("某某软件")
	app.iconbitmap("res\\app.ico")
	app.bind('<Escape>' , exit)
	Login(app)
	app.mainloop()

if __name__ == '__main__':
	main()
