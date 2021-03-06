from basicPackage import *

logger = logging.getLogger('main.addNewContrView')
class AddNewContrView():
	def __init__(self, root):
		self.root = root
		self.create_page()
		
	def create_page(self):
		self.root.geometry('400x400')
		self.page = tk.Frame(self.root)
		self.page.pack()
		tk.Button(self.page, text="厂房合同",command=lambda:self.open_contract_view(name="factory")).grid(row=2, column=0)
		tk.Button(self.page, text="打税合同",command=lambda:self.open_contract_view(name="factory")).grid(row=2, column=1)
		tk.Button(self.page, text="打税合同",command=lambda:self.open_contract_view(name="factory")).grid(row=2, column=2)
	def open_contract_view(self, name):
		self.page.destroy()
		try:
			g_.theViewManager.open_view('ContractView', arg=name)
		except Exception:
			logger.error('ContractView error', exc_info=True)

