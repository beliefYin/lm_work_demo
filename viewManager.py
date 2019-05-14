
class ViewManager():
	def __init__(self):
		self.view_dict = {}

	def open_view(self, page_name):
		self.view_dict[page_name](self.root)

	def register(self, page_name, view_class):
		self.view_dict[page_name] = view_class

	def set_root(self, root):
		self.root = root

