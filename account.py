class Investment:
	company_name = ""
	amount = 0

	def __init__(self, comName, amo):
		self.company_name = comName
		self.amount = amo


class BankAccount:
	id = 0
	balance = 0
	investments = []

	def __init__(self, id, balance):
		self.id = id
		self.balance = balance

	def invest(self, invest_com, invest_amo):
		self.investments.append(Investment(invest_com, invest_amo))