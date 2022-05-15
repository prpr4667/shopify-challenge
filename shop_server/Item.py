class Item:
	def __init__(self, name, category, keywords):
		self.name = name
		self.category = category
		self.keywords = keywords
		
	def update_item(self, category, keywords):
		self.category = category
		self.keywords = keywords