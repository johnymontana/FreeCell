class FCNode(object):
	def __init__(self, a_freeCells, a_cascades, a_foundations):
		self.freeCells = self.deepish_copy(a_freeCells)
		self.cascades = self.deepish_copy(a_cascades)
		self.foundations = self.deepish_copy(a_foundations)

	def deepish_copy(self, a_lol):
		newLol = []
		for i in a_lol:
			newLol.append(list(i))
		return newLol

	def printMe(self):
		print 'Foundations:'
		for foundation in self.foundations:
			print foundation
		print 'FreeCells:'
		for cell in self.freeCells:
			print cell
		print 'Cascades:'
		for cascade in self.cascades:
			print cascade

	def getAllMoves(self):
		moves = []
		
		# moves is a list of tuples of tuples
		# ex:  [((C,0),(F,0)), ((C,1),(R,2))]
				# 1=> move cascase[0].last() to Foundation[0].append()
				# 2=> move cascade[1].last() to FreeCell[2].append()
		# move any card from last of cascade to an empty freecell
		moves.append((('C',int(0)),('F',int(0))))
		moves.append((('C',int(1)),('R',int(2))))
		return moves;
		# move a cascade.last() to a cascade.append() IF VALID
			# VALID:
				#   IF card being moved < casecade.last()
				# & two cards are diff colors

		# move a casecade.last() to a foundation.append()

		# move a freecell.last() to a cascase.append()

		# move a freecell.last() to foundation.append()


class Problem(object):
	def __init__(self, a_node):
		self.firstNode = a_node
	
	def getResult(self, a_node, action):
		foundations = self.deepish_copy(a_node.foundations)
		freeCells = self.deepish_copy(a_node.freeCells)
		cascades = self.deepish_copy(a_node.cascades)
		
		#if action[0][0] == 'C':
			# get card @ action 	



		newNode = FCNode(
#############################
###    BEGIN MAIN        ####
#############################

infile = open('deal1.dat', 'r')
all_lines = infile.read().splitlines()

cascades=[]
i=0
for line in all_lines:
	cascades.append(line.split(' '))
	i += 1
newCascades = []
for cascade in cascades:
	#print cascade
	tmpTuple=()
	column=[]
	
	for card in cascade:
		tmpTuple = (card[0],card[1])
		column.append(tmpTuple)
	newCascades.append(column)
#print cascades[2][2][1]

#for newCascade in newCascades:
	#print newCascade
#print newCascades
node = FCNode([], newCascades, [])
node.printMe()
print node.getAllMoves()
