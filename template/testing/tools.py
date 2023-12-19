import sys

TERMINAL = sys.stdout

def read_file_as_string(path):
	with open(path, "r") as file:
		return file.read()

class IOManager():

	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
		self.output_file = None
		
	def mock_input(self):
		inputs = read_file_as_string(self.input_path)
		def input_generator():
			yield from inputs.splitlines()
		generator = input_generator()
		return lambda : next(generator)
	
	def reset_defaults(self):
		sys.stdout = TERMINAL
		if self.output_file:
			ouput_file = self.output_file
			ouput_file.close()
			ouput_file = None

	def toggle_ouput(self):
		if self.output_file:
			self.reset_defaults()
		else:
			ouput_file = open(self.output_path, "w")
			self.output_file = ouput_file
			sys.stdout = ouput_file