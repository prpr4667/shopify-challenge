class Status:
	def __init__(self):
		self.status = 0
		self.comment = ""
		
	def update_status(self, status, comment):
		self.status = status
		self.comment = comment
		
	def get_status(self):
		return self.status
	
	def get_comment(self):
		return self.comment
	