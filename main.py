import time
import psycopg2


from enum import Enum
from typing import Any
from datetime import datetime
from configparser import ConfigParser

class instrument_name(Enum):
	INSTRUMENT1 = 1
	INSTRUMENT2 = 2
	INSTRUMENT3 = 3

class data:
	def __init__(self, instrument_name: instrument_name, date: str, value: float) -> None:
		self.instrument_name = instrument_name
		self.date = date
		self.value = value

class calculationEngine():
	def __init__(self) -> None:
		self.map_of_calcs = {
			instrument_name.INSTRUMENT1: 0,
			"len_1": 0,
			instrument_name.INSTRUMENT2: 0,
			"len_2": 0,
			instrument_name.INSTRUMENT3: 0
		}


def load_config(filename='database.ini', section='postgresql'):
	parser = ConfigParser()
	parser.read(filename)

	# get section, default to postgresql
	config = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			config[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return config

def main():
	#connect to psql db
	config = load_config()
	conn = psycopg2.connect(**config)

	conn.autocommit = True
	cursor = conn.cursor()
	
	
	# measure time elapsed
	start_time = time.time()
	engine = calculationEngine()
	with open('example_input.txt', 'r') as file:
		for line in file:
			data_array = line.strip().split(",")
			calculator(data(data_array[0], datetime.strptime(data_array[1], "%d-%b-%Y"), data_array[2]), engine, cursor)


	print("--- %s seconds ---" % (time.time() - start_time))


def calculator(data: data, engine: calculationEngine, cursor):
	if data.date <= datetime.strptime("19-Dec-2014", "%d-%b-%Y") and data.date.weekday() < 5:
		query = f"select * from instrument_price_modifier where name='{data.instrument_name.upper()}'"
		cursor.execute(query)
		results = cursor.fetchall() 
		

		if data.instrument_name == "INSTRUMENT1":
			engine.map_of_calcs[instrument_name.INSTRUMENT1] += float(data.value) * float(results[0][-1])
			engine.map_of_calcs["len_1"] += 1

			print(f"median1: {engine.map_of_calcs[instrument_name.INSTRUMENT1]/engine.map_of_calcs['len_1']}")

		elif data.instrument_name == "INSTRUMENT2" and data.date.year == 2014:
			engine.map_of_calcs[instrument_name.INSTRUMENT2] += float(data.value) * float(results[0][-1])
			engine.map_of_calcs["len_2"] += 1

			print(f"median2: {engine.map_of_calcs[instrument_name.INSTRUMENT2]/engine.map_of_calcs['len_2']}" )
		
		elif data.instrument_name == "INSTRUMENT3":
			#if bigger
			if engine.map_of_calcs[instrument_name.INSTRUMENT3] < float(data.value):
				engine.map_of_calcs[instrument_name.INSTRUMENT3] = float(data.value)

				print(f"max 3: {engine.map_of_calcs[instrument_name.INSTRUMENT3]}")
	else:
		print("Date is greater than 01-Nov-2014")


if __name__ == "__main__":
	main()