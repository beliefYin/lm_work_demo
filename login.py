from passlib.hash import sha256_crypt
from basicPackage import *
logger = logging.getLogger('main.login')

def check_encrypted_password(password, hashed):
	return sha256_crypt.verify(password, hashed)

class Login():
	def __init__(self, root):
		self.root = root
		self.username = tk.StringVar()
		self.password = tk.StringVar()
		self.create_page()

	def create_page(self):
		self.root.geometry('300x200')
		self.page = tk.Frame(self.root)
		self.page.pack()

		tk.Label(self.page, text="某某软件").grid(row=0)

		tk.Label(self.page, text="账号：").grid(row=1,column=0)
		password_entry = tk.Entry(self.page, textvariable=self.username)
		password_entry.grid(row=1,column=1)
		tk.Label(self.page, text="密码：").grid(row=2,column=0)
		tk.Entry(self.page, textvariable=self.password).grid(row=2,column=1)

		tk.Button(self.page, text="确定",command=self.login).grid(row=3)
		self.root.bind('<Return>' , self.login)
		password_entry.focus_set()

	def login(self, event=None):
		username = self.username.get()
		password = self.password.get()
		db = sqlite3.connect('app.db')
		connect = db.cursor()
		cursor = connect.execute('SELECT password FROM account WHERE username="%s" LIMIT 1'%self.username.get())
		isExist = False
		encryptedPw = ""
		for row in cursor:
			encryptedPw = row[0]
			isExist = True
		if isExist and check_encrypted_password(self.password.get(), encryptedPw):
			self.page.destroy()
			self.root.unbind('<Return>' )
			try:
				g_.theViewManager.open_view('HomePage')
			except Exception:
				logger.error('HomePage error', exc_info=True)
			
		else:
			messbox.showinfo(title="错误", message="账号密码错误")

