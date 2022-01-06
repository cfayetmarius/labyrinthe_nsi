import tkinter as tk
from PIL import Image, ImageTk
import sys, time, vlc
#On crée un labyryinthe basé sur un arbre binaire
#images format 720x540
#0 : début, 1 : droite, 2 : gauche, 3 : droite et gauche , 4 : fin, 5 : impasse

class Node :
	def __init__(self,v,left, right) :
		self.v = v
		self.left = left
		self.right = right

class Stack :
	def __init__(self) :
		self._storage = []
	def stack(self, elem) :
		self._storage.append(elem)
	def destack(self) :
		try :
			return self._storage.pop()
		except :
			pass
class Game :
	def __init__(self) :
		self.pos = Node(0,None,Node(2,Node(3,Node(3,Node(3,Node(1,None,Node(2,Node(2,Node(1,None,Node(5,None,None)),None),None)),Node(5,None,None)),Node(1,None,Node(2,Node(4,None,None),None))),Node(1,None,Node(5,None,None))),None))
		self.moves = Stack()
		self.root = tk.Tk()
		self.IMG_LIST = [ImageTk.PhotoImage(Image.open('img/debut.jpg')),ImageTk.PhotoImage(Image.open('img/droite.jpg')),ImageTk.PhotoImage(Image.open('img/gauche.jpg')),ImageTk.PhotoImage(Image.open('img/droite_gauche.jpg')),ImageTk.PhotoImage(Image.open('img/fin.jpg')),ImageTk.PhotoImage(Image.open('img/impasse.jpg'))] 
		self.screenlabel = tk.Label(self.root, image=self.IMG_LIST[0])
		self.screenlabel.pack(side='bottom', fill='both', expand=True)
		self.root.title('Labyrinthe - Marius') 
		self.root.geometry('1080x810')
		self.root.minsize(1080,810)
		self.root.maxsize(1080,810)
		self.root.bind('<Escape>',self.close)
		self.root.bind('d',self.right)
		self.root.bind('q',self.left)
		self.root.bind('s',self.retreat)
	def run(self) :
		self.root.mainloop()

	def close(self, event) :
		self.root.destroy()
		sys.exit(1)

	def setimg(self, img) :
		self.screenlabel.configure(image=img)
		self.screenlabel.image = img

	def left(self,event) :
		if self.pos.v == 4 :
			self.root.destroy()
			print('You won !')
			sys.exit(0)
		self.moves.stack(self.pos)
		if self.pos.left != None :
			self.pos = self.pos.left
			self.updateimg()
		else :
			pass

	def right(self,event) :
		if self.pos.v == 4 :
			self.root.destroy()
			print('You won !')
		self.moves.stack(self.pos)
		if self.pos.right != None :
			self.pos = self.pos.right
			self.updateimg()
		else :
			pass

	def retreat(self,event) :
		self.pos = self.moves.destack()
		self.updateimg()

	def updateimg(self) :
		vlc.MediaPlayer('pas.wav').play()
		self.setimg(self.IMG_LIST[self.pos.v])

board = Game()
board.run()