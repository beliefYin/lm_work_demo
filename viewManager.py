from view_def import view_dict, init_view

class ViewManager():
	def __init__(self, root):
		self.root = root
		self.now_view = init_view(root, self)

	def to_page(self, page_name):
		view_dict[page_name](self.root, self)

