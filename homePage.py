from basicPackage import *

logger = logging.getLogger('main.homePage')
class HomePage():
	def __init__(self, root):
		self.root = root
		self.create_page()
	def create_page(self):
		self.root.geometry('400x400')
		self.page = tk.Frame(self.root)
		self.page.pack()
		tk.Label(self.page, text="合同").grid(row=0)
		tk.Button(self.page, text="新增合同",command=self.add_new_contract).grid(row=0, column=1)
		tk.Button(self.page, text="续签/修改",command=self.test).grid(row=0, column=2)
		tk.Button(self.page, text="打税合同",command=self.test).grid(row=0, column=3)
		tk.Label(self.page, text="月初").grid(row=1)
		tk.Button(self.page, text="发票信息打印",command=self.test).grid(row=1, column=1)
		tk.Button(self.page, text="水电费",command=self.test).grid(row=1, column=2)
		tk.Button(self.page, text="租赁情况修改",command=self.test).grid(row=1, column=3)
		tk.Button(self.page, text="收据打印",command=self.test).grid(row=1, column=4)
		tk.Label(self.page, text="月中").grid(row=2)
		tk.Button(self.page, text="单据收回记录",command=self.test).grid(row=2, column=1)
		tk.Label(self.page, text="月中").grid(row=3)
		tk.Button(self.page, text="月度账务生成",command=self.test).grid(row=3, column=1)
	def test(self):
		pass
	def add_new_contract(self):
		self.page.destroy()
		try:
			g_.theViewManager.open_view('AddNewContrView')
		except Exception:
			logger.error('AddNewContrView error', exc_info=True)
