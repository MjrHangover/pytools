#######################################################
## for writing unbuffered output 
#######################################################

import sys

class Unbuffered():

	def __init__(self, stream):
		self.stream = stream
		
	def write(self, data):
		self.stream.write(data)
		self.stream.flush()

	def __getattr__(self, attr):
		return getattr(self.stream, attr)

###
#from mytools.unbuffered_stream_functions import Unbuffered, PrintFunction.rprint, PrintFunction.Print
#
#rprint(data) or rprint(stream=sys.stdout, data)
###
def rprint(data):
	sys.stdout.write(data)

def Print(data):
	sys.stdout.write(data)
	sys.stdout.write('\n')

#####################################################
## Ex usage:
#####
#
# sys.stdout = Unbuffered(sys.stdout)
# print 'Hello'
#
#####
## result is Hello is printed immediately (no buffer)
