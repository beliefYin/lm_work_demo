from basicPackage import *
from template.contract_conf import contract_conf
from docxtpl import DocxTemplate 
logger = logging.getLogger('main.contractView')

template_path = 'template\\'
new_file_path = 'template\\newfile\\'

class ContractView():
	def __init__(self, root, name):
		self.root = root
		self.var_dict = {}
		self.create_page(name)

	def create_page(self, name):
		self.root.geometry('400x400')
		self.page = tk.Frame(self.root)
		self.page.pack()

		if name not in contract_conf:
			tk.Label(self.page, text="传的name不在配置里")
			tk.Button(self.page, text="返回", command=self.back).pack()
			return

		self.config = contract_conf[name]
		view = self.config["view"]
		now_row = 0
		for k in view:
			if "showType" not in view[k] or view[k]["showType"] == "text" or view[k]["showType"] == "optional_text":
				varname = "var"+str(now_row)
				tk.Label(self.page, text=view[k]["name"]).grid(row=now_row, column=0)
				self.var_dict[varname] = tk.StringVar()
				tk.Entry(self.page, textvariable=self.var_dict[varname]).grid(row=now_row,column=1)
			now_row += 1
		tk.Button(self.page, text="返回", command=self.back).grid(row=now_row,column=0)
		tk.Button(self.page, text="保存", command=self.save).grid(row=now_row,column=1)
	def save(self):
		view = self.config["view"]
		doc = DocxTemplate(template_path+self.config["filename"])
		context = {}
		now_row = 0
		for k in view:
			if "showType" not in view[k] or view[k]["showType"] == "text" :
				varname = "var"+str(now_row)
				context[k] = self.var_dict[varname].get()
			elif view[k]["showType"] == "optional_text":
				varname = "var"+str(now_row)
				if self.var_dict[varname].get() == "":
					context[k] = ""
				else:
					context[k] = view[k]["prefix"] + self.var_dict[varname].get()
			now_row += 1
		doc.render(context)  
		doc.save(new_file_path+self.config["newfilename"])

	def back(self):
		self.page.destroy()
		try:
			g_.theViewManager.open_view('AddNewContrView')
		except Exception:
			logger.error('AddNewContrView error', exc_info=True)


