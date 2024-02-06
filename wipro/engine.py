from datetime import datetime
from models import data

class engine():
	def __init__(self) -> None:
		self.map_of_calcs = {
		}
		
	def calculator(self, data: data, cursor):
		if data.date <= datetime.strptime("19-Dec-2014", "%d-%b-%Y") and data.date.weekday() < 5:
			query = f"select * from instrument_price_modifier where name='{data.instrument_name.upper()}'"
			cursor.execute(query)
			results = cursor.fetchall() 
			

			if data.instrument_name not in self.map_of_calcs:
				self.map_of_calcs[data.instrument_name] = float(data.value)
				self.map_of_calcs[f"len_{data.instrument_name}"] = 1
			
			if data.instrument_name == "INSTRUMENT1":
				self.map_of_calcs[data.instrument_name] += float(data.value) * float(results[0][-1])
				self.map_of_calcs[f"len_{data.instrument_name}"] += 1

				print(f"median1: {self.map_of_calcs[data.instrument_name]/self.map_of_calcs[f'len_{data.instrument_name}']}")

			elif data.instrument_name == "INSTRUMENT2" and data.date.year == 2014:
				self.map_of_calcs[data.instrument_name] += float(data.value) * float(results[0][-1])
				self.map_of_calcs[f"len_{data.instrument_name}"] += 1

				print(f"median2: {self.map_of_calcs[data.instrument_name]/self.map_of_calcs[f'len_{data.instrument_name}']}" )
			
			elif data.instrument_name == "INSTRUMENT3":
				#if bigger
				if self.map_of_calcs[data.instrument_name] < float(data.value):
					self.map_of_calcs[data.instrument_name] = float(data.value)

					print(f"max 3: {self.map_of_calcs[data.instrument_name]}")
