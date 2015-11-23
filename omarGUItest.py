import Tkinter
from Tkinter import *

from googlefinance import getQuotes
import json

import matplotlib.pyplot as plt
import matplotlib, sys
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from numpy import *
root = Tk()

def register(name, number, email, username, password, budget, Industry):
	print("Registering new User")

def login(username, password):
	print('in login')
	print(str(username))
	print(str(password))
	return

def firmRegisterForm(firm):
	print("firm reg form")
		

def registerForm(accountType):
	print(accountType)
	if accountType == 1:
		print('This will register a Broker')
		clear(root)
		root.wm_title("Stock Market App - Register Broker")
		root.geometry("500x500")
		
		Frame(root, height=10).grid(row=0, column=0)
		
		accountType = IntVar()
		Label(root,width=20, text="Account Type: ").grid(row=1, column=0, sticky=W)

		Radiobutton(root, text="Broker", variable=accountType, value=0, command=lambda: registerForm(accountType.get())).grid(row=1, column=1, sticky=W)
		Radiobutton(root, text="Client", variable=accountType, value=2, command=lambda: registerForm(accountType.get())).grid(row=1, column=1, sticky=E)
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Personal Information _____________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		nameVar = StringVar()
		numberVar = StringVar()
		emailVar = StringVar()
		userVar = StringVar()
		passVar1 = StringVar()
		passVar2 = StringVar()
		budgetVar = StringVar()
		industryVar = StringVar()
		licenceVar = StringVar()
		authorityVar = StringVar()

		Label(root,width=20, text="Broker Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="Phone Number: ").grid(row=4, column=0, sticky=E)
		phoneEntry = Entry(root,width=35, textvariable=numberVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Email Address: ").grid(row=5, column=0, sticky=E)
		emailEntry = Entry(root,width=35, textvariable=emailVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Username: ").grid(row=6, column=0, sticky=E)
		userEntry = Entry(root,width=35, textvariable=userVar).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="Password: ").grid(row=7, column=0, sticky=E)
		passEntry1 = Entry(root,width=35, textvariable=passVar1, show="*").grid(row=7, column=1, sticky=W)	

		Label(root,width=20, text="Confirm Password: ").grid(row=8, column=0, sticky=E)
		passEntry2 = Entry(root,width=35, textvariable=passVar2, show="*").grid(row=8, column=1, sticky=W)	

		Label(root,width=20, text="Budget: ").grid(row=9, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33, values=('$10,000','$25,000','$50,000','$100,000','$250,000','$500,000','$1,000,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Licensing ________________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="License Type: ").grid(row=12, column=0, sticky=W)
		licenceEntry = Spinbox(root, width = 33,values=('License Type','Registered Representative', 'Investment Advisor IAR', 'Financial Advisor FCA')).grid(row=12, column=1, sticky=W)	
		
		Label(root, width=20, text="Issuing Authority: ").grid(row=13, column=0, sticky=W)
		authorityEntry = Entry(root,width=35, textvariable=authorityVar).grid(row=13, column=1, sticky=W)			
		
		Label(root, width=20, text="Year Issued: ").grid(row=14, column=0, sticky=W)
		budgetEntry = Spinbox(root, width = 33, from_=1980, to=2015).grid(row=14, column=1, sticky=W)		
		
		
		
		
		
		Frame(root, height=10).grid(row=17, column=0)


		Button(root, text="Clear", command=lambda: clear(root)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: firmRegisterForm(1)).grid(row=18, column=1, sticky=E)		

	elif accountType ==2:
		print('This will register a Client')
		clear(root)
		root.wm_title("Stock Market App - Register Client")
		root.geometry("500x500")
		Frame(root, height=10).grid(row=0, column=0)
		
		accountType = IntVar()
		Label(root,width=20, text="Account Type: ").grid(row=1, column=0, sticky=W)

		Radiobutton(root, text="Broker", variable=accountType, value=1, command=lambda: registerForm(accountType.get())).grid(row=1, column=1, sticky=W)
		Radiobutton(root, text="Client", variable=accountType, value=0, command=lambda: registerForm(accountType.get())).grid(row=1, column=1, sticky=E)
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Personal Information _____________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		nameVar = StringVar()
		numberVar = StringVar()
		emailVar = StringVar()
		userVar = StringVar()
		passVar1 = StringVar()
		passVar2 = StringVar()
		budgetVar = StringVar()
		industryVar = StringVar()
		brokerVar = StringVar()
		firmVar = StringVar()

		brokerVar.set("If not applicable, skip this field")
		firmVar.set("If not applicable, skip this field")

		Label(root,width=20, text="Client Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="Phone Number: ").grid(row=4, column=0, sticky=E)
		phoneEntry = Entry(root,width=35, textvariable=numberVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Email Address: ").grid(row=5, column=0, sticky=E)
		emailEntry = Entry(root,width=35, textvariable=emailVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Username: ").grid(row=6, column=0, sticky=E)
		userEntry = Entry(root,width=35, textvariable=userVar).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="Password: ").grid(row=7, column=0, sticky=E)
		passEntry1 = Entry(root,width=35, textvariable=passVar1, show="*").grid(row=7, column=1, sticky=W)	

		Label(root,width=20, text="Confirm Password: ").grid(row=8, column=0, sticky=E)
		passEntry2 = Entry(root,width=35, textvariable=passVar2, show="*").grid(row=8, column=1, sticky=W)	

		Label(root,width=20, text="Budget: ").grid(row=9, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33, values=('$1,000','$2,500','$5,000','$10,000','$25,000','$50,000','$100,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Representation ___________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="Representative: ").grid(row=12, column=0, sticky=W)
		authorityEntry = Entry(root,width=35,textvariable=brokerVar).grid(row=12, column=1, sticky=W)			
		
		Label(root, width=20, text="Firm: ").grid(row=13, column=0, sticky=W)
		authorityEntry = Entry(root,width=35,textvariable=firmVar).grid(row=13, column=1, sticky=W)			
		
		Label(root,height=2,text=" _________________________________________________________________").grid(row=14, column=0, sticky=E, columnspan=2)		
		
		
		
		Frame(root, height=10).grid(row=15, column=0)


		Button(root, text="Clear", command=lambda: clear(root)).grid(row=16, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: login(username.get(), password.get())).grid(row=16, column=1, sticky=E)		

def clear(yourwindow):
	for widget in yourwindow.winfo_children():
		widget.destroy()
	windowMenus(yourwindow)

def myGraph():
	clear(root)
	root.geometry("900x900")
	fig = plt.Figure(facecolor='w', edgecolor='w')
	x = numpy.arange(10)
	y = numpy.sqrt([81,99,100,29,10,29,19,55,53,4, 9, 100])


	#plt.plot(x, x)
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=1)
	fig.suptitle('Test Plot in Window Prototype')
	
	ax = fig.add_subplot(111)
	ax.set_xlabel("Time")
	ax.set_ylabel("Price $")
	ax.plot(x, label='GOOG')
	ax.plot(y, label='POOP')
	ax.legend()

	#plt.show()

def registerWindow():
	'''realstock = json.dumps(getQuotes('AAPL'), indent=2)
	print(realstock)'''
	registerPopup = Toplevel(root)
	registerPopup.title("Registeration")
	registerPopup.geometry('250x80')
	registerPopup.transient(root)
	registerPopup.resizable(width=FALSE, height=FALSE)

	Frame(registerPopup, height=10, width=10).grid(row=0, column=0, columnspan = 3)
	Label(registerPopup, width=30, text="Please Choose an Account Type").grid(row=1,columnspan = 3, column=1, sticky=W)
	Frame(registerPopup, height=10, width=10).grid(row=2, column=0, columnspan = 3)
	Button(registerPopup, text="Client", command=lambda: registerForm(2)).grid(row=3, column=1, sticky=E)
	Button(registerPopup, text="Broker", command=lambda: registerForm(1)).grid(row=3, column=2, sticky=E)
	
def loginWindow():
	loginPopup = Toplevel(root)
	loginPopup.title("Login")
	loginPopup.geometry('252x97')
	loginPopup.transient(root)
	loginPopup.resizable(width=FALSE, height=FALSE)

	username = StringVar()
	password = StringVar()

	Frame(loginPopup, height=10).grid(row=0, column=0)
	Label(loginPopup, text="Username: ").grid(row=1, column=0, sticky=W)
	Label(loginPopup, text="Password: ").grid(row=2, column=0, sticky=W)
	Entry(loginPopup, textvariable = username).grid(row=1, column=1, sticky=E)
	Entry(loginPopup, show="*", textvariable = password).grid(row=2, column=1, sticky=E)


	Button(loginPopup, text="Login", command=lambda: login(username.get(), password.get())).grid(row=3, column=1, sticky=E)
	Button(loginPopup, text="destroy", command=lambda: clear(loginPopup)).grid(row=3, column=0, sticky=W)


	return

def windowMenus(root):
	menubar = Menu(root)
	'''
	filemenu = Menu(menubar, tearoff=1)
	root.config(menu=menubar)
	'''
	#menubar = Menu(win)
	#appmenu = Menu(menubar, name='apple')
	#menubar.add_cascade(menu=appmenu)
	#appmenu.add_command(label='About My Application')
	#appmenu.add_separator()

	root['menu'] = menubar
	'''frame1 = Frame(root, width = 100, height = 300)
	frame1.configure(background="red")
	frame1.pack(side = LEFT, expand = YES, fill=Y)
	frame2 = Frame(root, width = 50, height = 150)
	frame2.configure(background="blue")
	frame2.pack(side = LEFT, expand = YES, fill=Y)
	
	mylabel = Label(root,text="Test Label Widget")    
	mybutton = Button(root,text="Test Button Widget")
	mylabel.pack()
	mybutton.pack()
	'''

	windowmenu = Menu(menubar, name='window')
	omarMenu = Menu(menubar)
	accountMenu = Menu(menubar)
	stocksMenu = Menu(menubar)
	helpMenu = Menu(menubar)

	menubar.add_cascade(menu=accountMenu, label='Account')
	menubar.add_cascade(menu=stocksMenu, label="Stocks")
	menubar.add_cascade(menu=omarMenu, label="Omar's Tool")
	menubar.add_cascade(menu=helpMenu, label="Help")

	accountMenu.add_command(label="Login", accelerator='cmd-l', command=loginWindow)
	registerMenu=accountMenu.add_command(label="Register", accelerator = 'cmd-r',command=registerWindow)
	accountMenu.add_separator()
	accountMenu.add_command(label="Change Info", command="")
	accountMenu.add_command(label="View History", command="")
	accountMenu.add_separator()
	accountMenu.add_command(label="Bleh", command="")

	root.bind('<Command-l>', lambda e: loginWindow())
	root.bind('<Command-r>', lambda e: registerWindow()) 
	root.bind('<Command-p>', lambda e: myGraph()) 


	stocksMenu.add_command(label="View Portfolio", accelerator="cmd-p",command="")
	stocksMenu.add_separator()
	stocksMenu.add_command(label="View Stock Market", accelerator="cmd-v", command="")
	stocksMenu.add_command(label="Compare Stocks", accelerator="cmd-c", command="")
	stocksMenu.add_separator()
	stocksMenu.add_command(label="Sell", accelerator="cmd-s",command="")
	stocksMenu.add_command(label="Buy", accelerator="cmd-b",command="")
	stocksMenu.add_command(label="Trade", accelerator="cmd-t",command="")

	omarMenu.add_command(label="Do This", command="")
	omarMenu.add_command(label="Do That", command="")
	omarMenu.add_separator()
	omarMenu.add_command(label="Do Something", command="")
	omarMenu.add_separator()
	omarMenu.add_command(label="Do The Barracuda", command="")

	helpMenu.add_separator()
	helpMenu.add_command(label="Software Tutorial", command="")
	helpMenu.add_command(label="Hotkey List", command="")


def main():
	
	root.tk.call('tk', 'windowingsystem') 
	root.wm_title("Stock Market App - Home")
	root.geometry("500x500")
	root.resizable(width=FALSE, height=FALSE)
	windowMenus(root)
	







	#indexMenu = menubar.add_cascade(menu=windowmenu, label='Open Indexes')
	#toolsMenu = menubar.add_cascade(menu=windowmenu, label="Omar's Tools")
	#account
	#accountMenu.add_cascade(menu = port)

	root.mainloop()
if __name__ == "__main__":
	main()
