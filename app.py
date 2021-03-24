import tkinter as tk
from file_explorer import File_Explorer
from PIL import Image, ImageTk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()


	def create_widgets(self):
		self.explorer = File_Explorer(self)
		# sets the position
		self.explorer.pack(side="top")

		self.label = tk.Label(self)
		
		def set_label(e):
			self.label["text"]=self.explorer.content

		self.bind("<<Fileread>>", set_label)   
		self.label.pack()


class toolBar:
	def __init__(self, master):
		myFrame = tk.Frame(master)
		# open file button + the icon
		self.openImg = tk.PhotoImage(file="images/folder1.png")
		self.openButton = tk.Button(myFrame , image=self.openImg , command=self.printing,borderwidth=0)
		self.openButton.pack(side=tk.LEFT ,padx=10)
		#save as button + the icon
		self.saveImg = tk.PhotoImage(file="images/floppy1.png")
		self.saveAsButton =tk.Button(myFrame , image=self.saveImg , command=self.printing ,borderwidth=0)
		self.saveAsButton.pack(side=tk.LEFT)
		# scale button + the icon
		self.scaleImg = tk.PhotoImage(file="images/scale.png")
		self.scaleButton = tk.Button(myFrame , image=self.scaleImg , command=self.printing,borderwidth=0)
		self.scaleButton.pack(side=tk.LEFT ,padx=10)

		self.zoomInImg = tk.PhotoImage(file="images/zoomIn.png")
		self.scaleButton = tk.Button(myFrame , image=self.zoomInImg , command=self.printing,borderwidth=0)
		self.scaleButton.pack(side=tk.LEFT ,padx=10)

		self.zoomOutImg = tk.PhotoImage(file="images/zoomOut.png")
		self.scaleButton = tk.Button(myFrame , image=self.zoomOutImg , command=self.printing,borderwidth=0)
		self.scaleButton.pack(side=tk.LEFT ,padx=10)

		
		myFrame.pack(side="top", fill=tk.X )

	def printing(self):
		print("clicked and working ")



root = tk.Tk()
app = Application(master=root)
tool = toolBar(root)
app.mainloop()

