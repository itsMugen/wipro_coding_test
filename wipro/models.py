from datetime import datetime
class data:
	def __init__(self, instrument_name: str, date: datetime, value: float) -> None:
		self.instrument_name = instrument_name
		self.date = date
		self.value = value