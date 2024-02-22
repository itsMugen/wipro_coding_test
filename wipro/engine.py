import threading
from models import data
from datetime import datetime

class engine():
	def __init__(self, conn) -> None:
		self.map_of_calcs = {
		}
		self.map_multipliers = {}
		self.conn = conn

		self.updater = threading.Timer(0.25, self.update_multipliers).start()

	def update_multipliers(self):
		query = "select * from instrument_price_modifier"
		cursor = self.conn.cursor()
		cursor.execute(query)
		results = cursor.fetchall()

		for row in results:
			self.map_multipliers[row[1]] = float(row[2])

		
	def calculator(self, data: data):
		if data.date <= datetime.strptime("19-Dec-2014", "%d-%b-%Y") and data.date.weekday() < 5:
			if self.map_multipliers == {}:
				self.update_multipliers()

			if data.instrument_name not in self.map_of_calcs:
				self.map_of_calcs[data.instrument_name] = 0
				self.map_of_calcs[f"len_{data.instrument_name}"] = 0
			
			if data.instrument_name == "INSTRUMENT1":
				self.map_of_calcs[data.instrument_name] += float(data.value) * float(self.map_multipliers[data.instrument_name])
				self.map_of_calcs[f"len_{data.instrument_name}"] += 1

			elif data.instrument_name == "INSTRUMENT2" and data.date.year == 2014 and data.date.month == 11:
				self.map_of_calcs[data.instrument_name] += float(data.value) * float(self.map_multipliers[data.instrument_name])
				self.map_of_calcs[f"len_{data.instrument_name}"] += 1

			elif data.instrument_name == "INSTRUMENT3":
				if self.map_of_calcs[data.instrument_name] < float(data.value):
					self.map_of_calcs[data.instrument_name] = float(data.value)

			else:
				#For any other instrument from the input file - sum of the newest 10 elements (in terms of the date).
				if "last_10" not in self.map_of_calcs:
					self.map_of_calcs["last_10"] = [data]
				elif len(self.map_of_calcs["last_10"]) < 10:
					self.map_of_calcs["last_10"].append(data)
				else:
					self.map_of_calcs["last_10"].sort(key=lambda x: x.date)
					if self.map_of_calcs["last_10"][0].date < data.date:
						self.map_of_calcs["last_10"][0] = data
		
