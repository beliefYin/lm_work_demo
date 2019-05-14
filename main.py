from basicPackage import *
import initView
import globalVar as g_

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')#, filename="log.txt")
logger = logging.getLogger('main')
app = tk.Tk()


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

def exit(event):
	app.destroy()

def main():
	create_db()
	app.title("某某软件")
	app.iconbitmap("res\\app.ico")
	app.bind('<Escape>' , exit)
	g_.theViewManager.set_root(app)
	g_.theViewManager.open_view('Login')
	app.mainloop()

if __name__ == '__main__':
	try:
		main()
	except Exception:
		logger.error('Login page error', exc_info=True)
