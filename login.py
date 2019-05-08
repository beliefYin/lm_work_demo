from passlib.context import CryptContext
import tkinter as tk
import tkinter.messagebox as messbox
from homePage import HomePage

pwd_context = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
	return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
	return pwd_context.verify(password, hashed)

class Login():
	def __init__(self, root=None):
		self.username = tk.StringVar()
		self.password = tk.StringVar()
		self.create_page(root)

	def create_page(self, root=None):
		self.root = root
		self.root.geometry('300x200')
		self.page = tk.Frame(self.root)
		self.page.pack()

		tk.Label(self.page, text="某某软件").grid(row=0)

		tk.Label(self.page, text="账号：").grid(row=1,column=0)
		tk.Entry(self.page, textvariable=self.username).grid(row=1,column=1)

		tk.Label(self.page, text="密码：").grid(row=2,column=0)
		tk.Entry(self.page, textvariable=self.password).grid(row=2,column=1)

		tk.Button(self.page, text="确定",command=self.login).grid(row=3)

	def login(self):
		username = self.username.get()
		password = self.password.get()
		if username == 'yzx' and password == '123':
			self.page.destroy()
			HomePage(self.root)
		else:
			messbox.showinfo(title="错误", message="账号密码错误")




# password = "123"

# hashed = encrypt_password(password)
# print("hashed:%s"%hashed)
# print(check_encrypted_password("dd", hashed))