import tkinter as tk
class HomePage():
	def __init__(self, root):
		self.root = root
		self.create_page(root)
	def create_page(self, root=None):
		self.root = root
		self.root.geometry('400x400')
		self.page = tk.Frame(self.root)
		self.page.pack()
