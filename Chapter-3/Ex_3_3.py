
class SetOfStacks():
	def __init__(self):
		self.size = 0
		self.index = 0
		self.substacks = [[]]
		self.threshold = 5
		self.currentIndex = 0
		self.currentStack = 0

	def get_size(self):
		return len(self.substacks)

	def push(self, element):
		#If the current stack have reach the limit then create a new stack and append it 
		#else perform a normal push and increment the current position on the stack
		if self.currentIndex >= self.threshold:
			new_stack = []
			self.substacks.append(new_stack)
			self.currentStack += 1
			self.currentIndex = 0
			self.substacks[self.currentStack].append(element)

		else:
			self.substacks[self.currentStack].append(element)
			self.currentIndex += 1


	def pop(self):
		element = self.substacks[self.currentStack].pop()
		if self.currentIndex  == 0:
			 self.currentIndex = self.threshold
			 self.currentStack -= 1
			 self.substacks.pop()
		else:
			self.currentIndex -= 1

		return element



my_stack = SetOfStacks()
for i in range(10):
	my_stack.push(i)
print(my_stack.substacks)


for i in range(10):
	print(my_stack.pop())

print(my_stack.substacks)
for i in range(0,20,2):
	my_stack.push(i)
print(my_stack.substacks)


for i in range(0,20, 2):
	print(my_stack.pop())

print(my_stack.substacks)

