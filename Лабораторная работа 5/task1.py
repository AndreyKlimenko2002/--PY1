# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_ = [{"bin" : bin(a), "dec": a, "hex" : hex(a), "oct" : oct(a)} for a in range(16)]
pprint(list_)
