import tkinter as tk
import sqlite3
import logging
from viewManager import ViewManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')#, filename="log.txt")
logger = logging.getLogger('main')


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
	ViewManager(app)
	app.mainloop()

if __name__ == '__main__':
	try:
		main()
	except Exception:
		logger.error('Faild to get result', exc_info=True)
