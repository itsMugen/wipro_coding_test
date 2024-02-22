import time
import psycopg2

from enum import Enum
from typing import Any
from datetime import datetime
from configparser import ConfigParser

from engine import engine
from models import data

def load_config(filename='config/database.ini', section='postgresql'):
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
	
	engine_local = engine(conn)
	with open('BIG_input.txt', 'r') as file:
		for line in file:
			data_array = line.strip().split(",")
			engine_local.calculator(data(data_array[0], datetime.strptime(data_array[1], "%d-%b-%Y"), data_array[2]))


	# loaded = numpy.genfromtxt('BIG_input.txt', delimiter='\n', dtype=numpy.str_)
	# for item in numpy.nditer(loaded):
	# 	data_array = item.item(0).split(",")
	# 	engine_local.calculator(data(data_array[0], datetime.strptime(data_array[1], "%d-%b-%Y"), data_array[2]))
	
if __name__ == "__main__":
	# time_array = []

	# for i in range(0, 5):
	# 	start = time.time()
	# 	main()
	# 	end = time.time()
	# 	time_array.append(end-start)

	# print(time_array)
	# print(f"Median time to run main: {sum(time_array)/len(time_array)}")
	start = time.time()
	main()
	end = time.time()
	print(f"Python run: {end-start}")
