#passgen#
import sys, random, string

len = 26

def hexdigits():
	while True:
                try:
                        char_set = string.hexdigits
                        result = ''.join(random.sample(char_set*6, len))
                        print result
                except (KeyboardInterrupt):
                        exit()
def lowercase():
	while True:
		try:
			char_set = string.ascii_lowercase
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def lowerupper():
	while True:
		try:
			char_set = string.ascii_lowercase + string.ascii_uppercase
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def lowernum():
	while True:
		try:
			char_set = string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def uppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.digits
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def loweruppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def uppercase():
	while True:
		try:
			char_set = string.ascii_uppercase
			result = ''.join(random.sample(char_set*6, len))
			print result
		except (KeyboardInterrupt):
			exit()
def arglist():
	print 'options: -l lowercase, -lU lower and uppercase, -l1 lower and numerals, -U upper ascii, -U1 upper and numerals, -lU1 lower, upper, and numerals, -C [char] [num] custom character set and length, --help this list'

args = sys.argv[1:]
if args:
	for arg in args:
		if arg == '-l':
			lowercase()
		elif arg == '-h':
			hexdigits()
		elif arg == '-lU':
			lowerupper()
		elif arg == '-l1':
			lowernum()
		elif arg == '-U1':
			uppernum()
		elif arg == '-lU1':
			loweruppernum()
		elif arg == '-U':
			uppercase()
		elif arg == '--help':
			arglist()
		elif arg == '-C':
			while True:
				try:
					char_set = sys.argv[2]
					char_len = sys.argv[3]
					result = ''.join([random.choice(char_set) for _ in range(int(char_len))])
					print result
				except (IndexError):
					print(IndexError, "Make sure you've added your character map and length")
					exit() 
				except (ValueError):
					print(ValueError, 'ValueError: sample larger than population')
					exit()
				except (KeyboardInterrupt):
					exit()
else:
	arglist()
