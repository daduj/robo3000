print ("\n*******************************************************")
print ("* Dobrodosli u robo3000 simulaciju *\n* Ja sam robotaur3000 *")
print ("*******************************************************\n")


class Robot:
	'Class for all Robots'
	
	valid_commands = ('PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT')
	orientations = ('NORTH', 'EAST', 'SOUTH', 'WEST')
	
	def __init__(self, name):
		self.name = name
		self.on_table = 0
		self.position = {"x":-1, "y":-1, "o":-1}
		self.table_size = range(0, 5)
	
	def brain(self, commands):
		#ddd
		for key, command in enumerate(commands):
			command = command.strip(' \t\n\r') #We are moving special chars from the beggining and end of the string

			if self.on_table == 1:
				# Our robo is set on the table, lets see if we can execute next command
				if command == "MOVE":
					self.move(self.get_orientation(True))
				elif command == "LEFT" or command == "RIGHT":
					self.rotate(command)
				elif command == "REPORT":
					print(self.get_position())

			if command == "PLACE" and key+1 < len(commands):
				# Our robo is not on the table yet, we have a valid PLACE command, we must get a valid coordinates and direction now
				self.place(commands[key+1].split(","))

	def place(self, cords):
		# Our cords must have exactlly 3 values: x, y, orientation
		if len(cords) == 3:
			# Lets try and convert x, y values to integers.
			try:
				x, y, o = int(cords[0]), int(cords[1]), cords[2]
			except ValueError:
				x, y, o = cords[0], cords[1], cords[2]
			# If x, y are between 0 - 4 and orientation is a valid string
			if ((x in self.table_size) and (y in self.table_size) and (o in self.orientations)):
				o_index = self.orientations.index(o) # We are getting the index of inserted orientation
				self.set_position(x, y, o_index) # Now we are acctually setting the position of a robo
				self.on_table = 1 # We are raising a flag that our robo is on the table
			#else:
				#print("not_ok")
		#else:
			#print("WRONG LENGTH")
	
	def move(self, orientation):
		#print orientation
		x_next, y_next = self.position["x"] + 1, self.position["y"] + 1 # We are incrementing current coordinates values by 1, it will represent coordinates of the next move
		x_prev, y_prev = self.position["x"] - 1, self.position["y"] - 1 # We are decrementing current coordinates values by 1, it will represent coordinates of the next move
		if orientation == "NORTH":
			if y_next in self.table_size:
				self.set_y_cord(y_next)
		elif orientation == "EAST":
			if x_next in self.table_size:
				self.set_x_cord(x_next)
		elif orientation == "SOUTH":
			if y_prev in self.table_size:
				self.set_y_cord(y_prev)
		elif orientation == "WEST":
			if x_prev in self.table_size:
				self.set_x_cord(x_prev)
		
	def rotate(self, rotation):
		orientation = self.get_orientation()
		#print orientation
		if rotation == "LEFT":
			if orientation == 0:
				orientation = 3
			else:
				orientation -= 1
		elif rotation == "RIGHT":
			if orientation == 3:
				orientation = 0
			else:
				orientation += 1
		self.set_orientation(orientation)
		
	def set_position(self, x, y, orientation):
		#Method for setting robots position
		self.position["x"] = x
		self.position["y"] = y
		self.position["o"] = orientation
	
	def set_x_cord(self, x):
		self.position["x"] = x
	
	def set_y_cord(self, y):
		self.position["y"] = y
	
	def set_orientation(self, o):
		self.position["o"] = o
	
	def get_position(self):
		return "%s,%s,%s" % (self.position["x"], self.position["y"], self.orientations[self.position["o"]])
		
	def get_orientation(self, value = False):
		if value:
			return self.orientations[self.position["o"]] # Returns the value of orientation eg. NORTH
		else:
			return self.position["o"] # Returns the index of orientation eg. 1


#Inicijalizacija robota
robotaur3000 = Robot('Robotaur3000')

#Infinite loop
while 1:
	command_input = raw_input("Enter command: ")
	if command_input.strip() == "0":
		print ("\n*******************************************************")
		print ("*  *\n*  *")
		print ("*******************************************************\n")
		#robotaur3000.move()
		break
	else:
		#print ("You entered " + command_input + " command")
		split_commands = command_input.split(" ") #We are spliting command by white space
		split_commands = filter(None, split_commands) # We are removing empty ones from array (if there was multiple white spaces in string)

		robotaur3000.brain(split_commands)
		