# Initial node class

class Node: 
	# simply initialize the class, with itself and the dataval
	def __init__(self, dataval=None):
		self.dataval = dataval
		# this itself stores a node class vs a pointer to it in C
		self.nextval = None

class head:
	#head basically
	def __init__(self):
		self.headval = None
		
list1 = head()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
