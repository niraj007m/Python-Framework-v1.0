###############################################################
### Python Framework for VAPT v 1.0			 	    		###
### 														###
### Designed by Niraj M. 			     					###
### niraj007m[at]gmail[dot]com        						###
### This work is licensed under the Creative Commons        ###
### Attribution-ShareAlike 3.0 Unported License.            ###
### To view a copy of this license, visit                   ###
### http://creativecommons.org/licenses/by-sa/3.0/ or send a###
### letter to Creative Commons, PO Box 1866, Mountain View, ###
### CA 94042, USA. 											###
###############################################################

from Tkinter import *
import ttk
import socket
from datetime import datetime
import subprocess
import tkMessageBox


class Scanning_port:

	def __init__(self, master):

		master.title('Infosecplatform Presents PFv1.0')
		master.resizable(False, False)
		master.configure(background = "#e1d8b9")

		self.style = ttk.Style()
		self.style.configure('TFrame', background = "#e1d8b9")
		self.style.configure('TButton', background = "#e1d8b9")
		self.style.configure('TLabel', background = "#e1d8b9")
		self.style.configure('TSeparator', background = "#e1d8b9")
		self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

		## Frame 1 ##
		self.frame_header = ttk.Frame(master)
		self.frame_header.pack()

		ttk.Label(self.frame_header, text = "Python Framework v 1.0", style = 'Header.TLabel').grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'sw')
		ttk.Label(self.frame_header, wraplength=295, text = "Port Scanning and").grid(row = 1, column = 1, padx = 5, sticky = 'sw')
		ttk.Label(self.frame_header, wraplength=295, text = "Banner Grabbing Tool for VAPT Professionals").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'sw')
		ttk.Separator(self.frame_header,orient=HORIZONTAL).grid(row=3, columnspan=5,sticky="ew", padx =5, pady = 10)
		## END ##
		## Frame 2 ##

		self.frame_content = ttk.Frame(master)
		self.frame_content.config(height = 200, width = 400)
		#self.frame_content.config(relief = GROOVE)
		self.frame_content.pack()

		ttk.Label(self.frame_content, text = "Enter Target IP Address: ").grid(row = 2, column = 0, padx =5, pady = 10)

		self.entry_name = ttk.Entry(self.frame_content, textvariable="server")
		self.entry_name.setvar(name="server", value="127.0.0.1")
		self.entry_name.grid(row = 3, column = 0, padx = 5)

		ttk.Button(self.frame_content, text = "Scan", command=self.dscan).grid(row = 3, column = 1, padx = 5, pady = 10, sticky = 'se')
		ttk.Button(self.frame_content, text = "Clear", command = self.Clear).grid(row = 3, column = 2, padx = 5, pady = 10, sticky = 'se')

		## END ##
		## Frame 3 ##

		self.frame_report = ttk.Frame(master)
		self.frame_content.config(height = 400, width = 400)
		self.frame_report.pack()

		self.txt = Text(self.frame_report, width = 60, height = 15)
		self.txt.grid(row=4,column=0, sticky=W, padx = 5, pady = 5)
		self.txt.insert(0.0, 'Open port will appear here (default range 1-1025)-Click Scan')

	def dscan(self):
		self.txt.delete(0.0, END)
		subprocess.call('clear', shell=True)
		remoteServer = self.entry_name.get()
		remoteServerIP = socket.gethostbyname(remoteServer)

		t1 = datetime.now()
		
		print('Please wait, scanning remote host (default port range 1-1025)', remoteServerIP)
		try:
			for port in range(1,1025):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((remoteServer,port))
				if result == 0:
					#print "Port {}:	Open".format(port)
					msg0 = "\nPort {}:	Open ".format(port) + "--> Banner Grabbing: " + sock.recv(1024) 
					self.txt.insert(0.0, msg0)
				sock.close()
		except KeyboardInterrupt:
			print "You Pressed Ctrl + c"
			sys.exit()

		except socket.gaierror:
			print "Couldn't connect to server"
			sys.exit()

		t2 = datetime.now()

		total = t2 - t1
		print "Scanning Completed in: ", total
		tkMessageBox.showinfo(title="Report Status!",message="Scaning Process Completed ")
		
	def Clear(self):
		self.entry_name.delete(0, 'end')
		self.txt.delete(0.0, 'end')

def main():
	root = Tk()
	scan = Scanning_port(root)
	menubar = Menu(root, background = "#e1d8b9")
	filemenu = Menu(menubar, tearoff=0, background = "#e1d8b9")
	filemenu.add_command(label="Scan", command=scan.dscan)
	filemenu.add_command(label="Clear", command=scan.Clear)
	
	filemenu.add_separator()

	filemenu.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="File", menu=filemenu, background = "#e1d8b9")

	helpmenu = Menu(menubar, tearoff=0, background = "#e1d8b9")
	helpmenu.add_command(label="Help", command=index0)
	helpmenu.add_command(label="About...", command=index)
	menubar.add_cascade(label="Help", menu=helpmenu)

	root.config(menu=menubar, background = "#e1d8b9")
	root.mainloop()

def index():
	filewin = Toplevel()
   	labelframe = LabelFrame(filewin, text="About", background = "#e1d8b9")
	labelframe.pack(fill="both", expand="yes")
 	
	left1 = Label(labelframe, background = "#e1d8b9", 
		text="Infosecplatform presents Python Framework v 1.0\n", font = "Verdana 10 bold").pack()
	
	left7 = Label(labelframe, background = "#e1d8b9", text="Got Questions ?",font = "Verdana 10 bold").pack()
	left8 = Label(labelframe, wraplength=325, background = "#e1d8b9", 
		text="Please Submit your questions, comments and requests to niraj007m@gmail.com\n https://about.me/niraj.mohite\n https://infosecplatform.wordpress.com/").pack()
	left9 = Label(labelframe, wraplength=325, background = "#e1d8b9", 
		text="This Tool is only for learning purpose, "
				"We are not responsible if you misuse it !\n", font = "Verdana 7").pack()

	left10 = Label(labelframe, wraplength=300, background = "#e1d8b9", 
		text="This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License."
				"To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.", font = "Verdana 7").pack()
	 
	filewin.mainloop()

def index0():
	filewin1 = Toplevel()
	labelframe = LabelFrame(filewin1, text="Help", background = "#e1d8b9")
	labelframe.pack(fill="both", expand="yes")
 	
	left1 = Label(labelframe, background = "#e1d8b9", 
		text="Infosecplatform presents Python Framework v 1.0\n", font = "Verdana 10 bold").pack()
	left2 = Label(labelframe, background = "#e1d8b9", 
		text="What is Python Framework v 1.0 ?", font = "Verdana 10 bold").pack()
	left3 = Label(labelframe, background = "#e1d8b9", 
		text="PFv1.0 Provides:").pack()
	left4 = Label(labelframe, background = "#e1d8b9", 
		text="Simply GUI - Python based Tool for").pack()
	left5 = Label(labelframe, background = "#e1d8b9", text="1. Port scanning.").pack()
	left6 = Label(labelframe, background = "#e1d8b9", text="2. Banner Grabbing.\n").pack()
	filewin1.mainloop()

if __name__ == "__main__": main()
###############################################################
### Python Framework for VAPT v 1.0			 	    		###
### 														###
### Designed by Niraj M. 			     					###
### niraj007m[at]gmail[dot]com        						###
### This work is licensed under the Creative Commons        ###
### Attribution-ShareAlike 3.0 Unported License.            ###
### To view a copy of this license, visit                   ###
### http://creativecommons.org/licenses/by-sa/3.0/ or send a###
### letter to Creative Commons, PO Box 1866, Mountain View, ###
### CA 94042, USA. 											###
###############################################################