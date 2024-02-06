import time
import random

# https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates?page=1&tab=scoredesc#tab-top
def str_time_prop(start, end, time_format, prop):
	"""Get a time at a proportion of a range of two formatted times.
	start and end should be strings specifying times formatted in the
	given format (strftime-style), giving an interval [start, end].
	prop specifies how a proportion of the interval to be taken after
	start.  The returned time will be in the specified format.
	"""

	stime = time.mktime(time.strptime(start, time_format))
	etime = time.mktime(time.strptime(end, time_format))

	ptime = stime + prop * (etime - stime)

	return time.strftime(time_format, time.localtime(ptime))

#create data to test the engine
def generator():
	with open('BIG_input.txt', 'w') as file:
		for i in range(0, 99999999999):
			instrument = random.randrange(1, 10000)
			date = str_time_prop("01-Jan-1995", "19-Dec-2014", "%d-%b-%Y", random.random())
			value = round(random.uniform(0.10, 20.00), random.randrange(3, 5))

			file.write(f"INSTRUMENT{instrument},{date},{value}\n")


if __name__ == "__main__":
	generator()