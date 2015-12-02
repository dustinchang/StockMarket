import Tkinter
from Tkinter import *

import re

import main
from main import *

import sys
from sys import *

from googlefinance import getQuotes
import json

import matplotlib.pyplot as plt
import matplotlib, sys
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from numpy import *
root = Tk()
tempClient = Client()
tempBroker = Broker()
tempFirm = Firm()

loggedin = False


def validateClient(name, number, email, username, password, password2, budget, industry, broker, firm):
	print('___________________________________________________________')
	print("Validating new Client")
	errorMessage = ''
	global tempClient
	budget = re.sub('[,$]', '', budget)

	'''
		VALIDATE Name
	'''
	if not name == '':
		print('Name Validation - Clear!')
		tempClient.ClientName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		print('Phonenumber Validation - Clear!')
		tempClient.ClientPhoneNumber = number
	except ValueError:
		print('Phonenumber Validation - Error!')
		errorMessage += 'Phone Number is invalid\n'		


	''' 
		VALIDATE email
	'''
	if not email == '':
		print('Email Validation - Clear!')
		tempClient.ClientEmailAddress = email
	else:
		print('Email Validation - Error!')
		errorMessage += 'Email Address cannot be left empty\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		print('Username Validation - Clear!')
		tempClient.ClientID = username
	else:
		print('Username Validation - Error!')
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if not password == '' and not password2 =='':
		if password == password2:
			tempClient.ClientPassword = password
			print('Password Validation - Clear!')
		else:
			print('Password Validation - Error!')
			errorMessage += 'Passwords do not match\n'		
	else:
		#createPopup('validateClient', '')
		print('Name Validation - Error!')
		errorMessage += 'Password(s) cannot be left empty\n'		

	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		print('Budget Validation - Clear!')
		tempClient.ClientBudget = budget
	except ValueError:
		print('Phonenumber Validation - Error!')
		errorMessage += 'Budget is invalid\n'		
		

	if not industry =='':
		print('Industry Validation - Clear!')
		tempClient.ClientIndustry = industry
	else:
		print('Industry Validation - Error!')
		errorMessage += 'Industry is invalid\n'				


	if broker == 'If not applicable, skip this field':
		
		tempClient.ClientBrokerID = 'NA'
	else:
		tempClient.ClientBrokerID = broker

	if firm == 'If not applicable, skip this field':
		tempClient.ClientFirmID = 'NA'
	else:
		tempClient.ClientFirmID = firm


	if not errorMessage == '':
		createPopup('validateClient', errorMessage)
	else:
		createPopup('validateClient', 'Registration Successful!')
		

	print('___________________________________________________________')


def validateBroker(name, number, email, username, password, password2, budget, industry, license, authority, year):
	print('==========================================================')
	print("Validating new Broker")
	budget = re.sub('[,$]', '', budget)
	errorMessage = ''
	global tempBroker

	'''
		VALIDATE Name
	'''
	if not name == '':
		print('Name Validation - Clear!')
		tempBroker.BrokerName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		print('Phonenumber Validation - Clear!')
		tempBroker.BrokerPhoneNumber = number
	except ValueError:
		print('Phonenumber Validation - Error!')
		errorMessage += 'Phone Number is invalid\n'		


	''' 
		VALIDATE email
	'''
	if not email == '':
		print('Email Validation - Clear!')
		tempClient.ClientEmailAddress = email
	else:
		print('Email Validation - Error!')
		errorMessage += 'Email Address is invalid\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		print('Username Validation - Clear!')
		tempBroker.BrokerID = username
	else:
		print('Username Validation - Error!')
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if not password == '' and not password2 =='':
		if password == password2:
			tempBroker.BrokerPassword = password
			print('Password Validation - Clear!')
		else:
			print('Password Validation - Error!')
			errorMessage += 'Passwords do not match\n'			
	else:
		#createPopup('validateClient', '')
		print('Password Validation - Error!')
		errorMessage += 'Password(s) is invalid\n'		

	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		print('Budget Validation - Clear!')
		tempBroker.BrokerBudget = budget
	except ValueError:
		print('Budget Validation - Error!')
		errorMessage += 'Budget is invalid\n'		
		

	'''
		VALIDATE industry
	'''
	if not industry =='':
		print('Industry Validation - Clear!')
		tempBroker.BrokerIndustry = industry
	else:
		print('Industry Validation - Error!')
		errorMessage += 'Industry is invalid\n'				

	'''
		VALIDATE Licence Type
	'''
	if license == 'Financial Advisor FCA' or license == 'Investment Advisor IAR' or license == 'Registered Representative':
		print('Licence Type Validation - Clear!')
		tempBroker.BrokerLicenseType = license
	else:
		print('License Type Validation - Error!')
		errorMessage += 'License Type is invalid\n'

	'''
		VALIDATE issuing authority
	'''
	if not authority == '':
		print('Issuing Authority Validation -  Clear!')
		tempBroker.BrokerAuthority = authority
	else:
		print('Issuing Authority Validation - Error!')
		errorMessage += 'Issuing Authority invalid\n'

	'''
		VALIDATE year issued
	'''
	try:
		int(year)
		print('License Issuing Year Validation - Clear!')
		tempBroker.BrokerLicenseIssue = year
	except ValueError:
		print('License Issuing Year Validation - Error!')
		errorMessage += 'License Issuing Year is invalid\n'		




	if not errorMessage == '':
		createPopup('validateBroker', errorMessage)
	else:
		createPopup('validateBroker', 'Registration Successful!')
		

	print('==========================================================')


def login(username, password):
	print('In Login function')
	if not os.path.exists('SMfiles/users/'+username):
		createPopup('error','')
		return

	error = getattr(__builtins__, 'FileNotFoundError',IOError)
	try:
		txt = open(filename)
	except error:
		print('File: '+ filename+' could not be found')
		txt = open(filename, 'w+')
	
	return
def hotkeyWindow(root):
	print('This is the hotkeyWindow')
	clear(root)
	root.wm_title("Stock Market App - Help - Hotkey List")
	root.geometry("500x320")
	
	Frame(root, height=10).grid(row=0, column=0)
	
	#Frame(root, height=10).grid(row=2, column=0)
	Label(root,height=2,text="   Hotkey List ___________________________________________________________").grid(row=1, column=0, columnspan=2)

	Label(text="Login Hotkey -").grid(row=3, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","L")).grid(row=3, column=1, sticky=W)
	
	Label(text="Register Hotkey -").grid(row=4, column=0, sticky=E)
	Label(text= "%s%s" % (u"\u2318","R")).grid(row=4, column=1, sticky=W)

	Label(text="Stock Comparison Hotkey -").grid(row=5, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","C")).grid(row=5, column=1, sticky=W)

	Label(text="View Stock Market Hotkey -").grid(row=6, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","V")).grid(row=6, column=1, sticky=W)
	
	Label(text="Register Firm Hotkey -").grid(row=7, column=0 , sticky=E)
	Label(text="%s%s" % (u"\u2318","F")).grid(row=7, column=1, sticky=W)

	Label(text="Edit Information Hotkey -").grid(row=8, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","E"),fg="#006400").grid(row = 8, column=1, sticky=W)

	Label(text="Portfolio Hotkey -").grid(row=9, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","P"),fg="#006400").grid(row=9, column=1, sticky=W)

	Label(text="Sell Stock Hotkey -").grid(row=10, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","S"),fg="#006400").grid(row=10, column=1, sticky=W)

	Label(text="Trade Stock Hotkey -").grid(row=11, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","T"),fg="#006400").grid(row=11, column=1, sticky=W)

	Label(text="Buy Stock Hotkey -").grid(row=12, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","B"),fg="#006400").grid(row=12, column=1, sticky=W)
	
	Frame(root, height=10).grid(row=13, column=0)
	Label(text="Hotkeys highlighted in Green are only available when Logged In").grid(row=14, column=0, columnspan=2)

def firmRegisterForm(firm):
	if firm == 1:
		print('This will register a new Firm')
		clear(root)
		root.wm_title("Stock Market App - Register Firm")
		root.geometry("500x270")
		
		Frame(root, height=10).grid(row=0, column=0)
		
		firm = IntVar()
		Label(root,width=20, text="Firm: ").grid(row=1, column=0, sticky=W)

		Radiobutton(root, text="New Firm", variable=firm, value=0, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=W)
		Radiobutton(root, text="Existing Firm", variable=firm, value=2, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=E)
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Firm Information __________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		nameVar = StringVar()
		idVar = StringVar()
		typeVar = StringVar()
		budgetVar = IntVar()
		codeVar = StringVar()

		Label(root,width=20, text="Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="ID: ").grid(row=4, column=0, sticky=E)
		idEntry = Entry(root,width=35, textvariable=idVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Type: ").grid(row=5, column=0, sticky=E)
		typeEntry = Entry(root,width=35, textvariable=typeVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Authorization Code: ").grid(row=6, column=0, sticky=E)
		codeEntry = Entry(root,width=35, textvariable=codeVar).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="Budget ").grid(row=7, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33,values=('$10,000','$25,000','$50,000','$100,000','$250,000','$500,000','$1,000,000')).grid(row=7, column=1)	
		Frame(root, height=10).grid(row=16, column=0)
		Frame(root, height=10).grid(row=17, column=0)

		Button(root, text="Clear", command=lambda: firmRegisterForm(1)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: createPopup('firm', '')).grid(row=18, column=1, sticky=E)		

	elif firm ==2:
		print('This will get an existing firm')
		clear(root)
		clear(root)
		root.wm_title("Stock Market App - Retrieve Firm")
		root.geometry("500x270")
		
		Frame(root, height=10).grid(row=0, column=0)
		
		firm = IntVar()
		Label(root,width=20, text="Firm: ").grid(row=1, column=0, sticky=W)

		Radiobutton(root, text="New Firm", variable=firm, value=1, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=W)
		Radiobutton(root, text="Existing Firm", variable=firm, value=0, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=E)
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Firm Information __________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		codeVar = StringVar()
		
		Label(root,width=20, text="Select Firm: ").grid(row=3, column=0, sticky=E)
		firmEntry = Spinbox(root, width = 33,values=('Select Firm','Chang & Associates', 'Malikorp', 'Gelera Inc.')).grid(row=3, column=1)	
		Frame(root, height=10).grid(row=4, column=0)
		Label(root,width=20, text="Authorization Code: ").grid(row=6, column=0, sticky=E)
		codeEntry = Entry(root,width=35, textvariable=codeVar).grid(row=6, column=1, sticky=W)
		Frame(root, height=10).grid(row=8, column=0)
		Frame(root, height=10).grid(row=9, column=0)
		Frame(root, height=10).grid(row=10, column=0)
		Frame(root, height=10).grid(row=11, column=0)
		Frame(root, height=10).grid(row=12, column=0)
		Frame(root, height=10).grid(row=13, column=0)
		Frame(root, height=10).grid(row=14, column=0)
		Frame(root, height=10).grid(row=15, column=0)
		Frame(root, height=10).grid(row=16, column=0)
		

		Button(root, text="Clear", command=lambda: firmRegisterForm(2)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: createPopup('firm', '')).grid(row=18, column=1, sticky=E)		

	elif firm == 3:
		clear(root)
		print('This will register a new Firm')
		clear(root)
		root.wm_title("Stock Market App - Register Firm")
		root.geometry("500x250")
		
		Frame(root, height=10).grid(row=0, column=0)
		
		firm = IntVar()
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Firm Information __________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		nameVar = StringVar()
		idVar = StringVar()
		typeVar = StringVar()
		budgetVar = IntVar()
		codeVar = StringVar()

		Label(root,width=20, text="Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="ID: ").grid(row=4, column=0, sticky=E)
		idEntry = Entry(root,width=35, textvariable=idVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Type: ").grid(row=5, column=0, sticky=E)
		typeEntry = Entry(root,width=35, textvariable=typeVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Authorization Code: ").grid(row=6, column=0, sticky=E)
		codeEntry = Entry(root,width=35, textvariable=codeVar).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="Budget ").grid(row=7, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33,values=('$10,000','$25,000','$50,000','$100,000','$250,000','$500,000','$1,000,000')).grid(row=7, column=1)	

		Frame(root, height=10).grid(row=17, column=0)

		Button(root, text="Clear", command=lambda: firmRegisterForm(3)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: createPopup('firm', '')).grid(row=18, column=1, sticky=E)		
			
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
		licenseVar = StringVar()
		authorityVar = StringVar()
		yearVar = StringVar()

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
		budgetEntry = Spinbox(root, width = 33, textvariable = budgetVar ,values=('$10,000','$25,000','$50,000','$100,000','$250,000','$500,000','$1,000,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Licensing ________________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="License Type: ").grid(row=12, column=0, sticky=W)
		licenceEntry = Spinbox(root, width = 33,textvariable = licenseVar, values=('License Type','Registered Representative', 'Investment Advisor IAR', 'Financial Advisor FCA')).grid(row=12, column=1, sticky=W)	
		
		Label(root, width=20, text="Issuing Authority: ").grid(row=13, column=0, sticky=W)
		authorityEntry = Entry(root,width=35, textvariable=authorityVar).grid(row=13, column=1, sticky=W)			
		
		Label(root, width=20, text="Year Issued: ").grid(row=14, column=0, sticky=W)
		budgetEntry = Spinbox(root, width = 33, textvariable = yearVar,from_=1980, to=2015).grid(row=14, column=1, sticky=W)		
				
		Frame(root, height=10).grid(row=17, column=0)

		Button(root, text="Clear", command=lambda: registerForm(1)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: validateBroker(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(), passVar2.get(), budgetVar.get(), industryVar.get(), licenseVar.get(), authorityVar.get(), yearVar.get())).grid(row=18, column=1, sticky=E)		

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
		budgetEntry = Spinbox(root, width = 33, textvariable=budgetVar, values=('$1,000','$2,500','$5,000','$10,000','$25,000','$50,000','$100,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Representation ___________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="Representative: ").grid(row=12, column=0, sticky=W)
		authorityEntry = Entry(root,width=35,textvariable=brokerVar).grid(row=12, column=1, sticky=W)			
		
		Label(root, width=20, text="Firm: ").grid(row=13, column=0, sticky=W)
		authorityEntry = Entry(root,width=35,textvariable=firmVar).grid(row=13, column=1, sticky=W)			
		
		Label(root,height=2,text=" _________________________________________________________________").grid(row=14, column=0, sticky=E, columnspan=2)		
		
		Frame(root, height=10).grid(row=15, column=0)
		# def register(name, number, email, username, password, budget, industry):
		Button(root, text="Clear", command=lambda: registerForm(2)).grid(row=16, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: 
			validateClient(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(), passVar2.get(), budgetVar.get(), industryVar.get(), brokerVar.get(), firmVar.get())).grid(row=16, column=1, sticky=E)		
def clear(yourwindow):
	for widget in yourwindow.winfo_children():
		widget.destroy()
	windowMenus(yourwindow)
def home():
	clear(root)
	root.wm_title("Stock Market App - Home")
	root.geometry("654x760")
	'''
	root.resizable(width=FALSE, height=FALSE)
	fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,5))
	x = numpy.arange(12)
	y = numpy.sqrt([81,99,100,29,10,29,19,55,53,4, 9, 100])
	z = [10,23,39,40,29,01,11,16,8,12]
	a = [7,8,9,10,9,8,7,6,5,4,3,2,10]

	stockVar1 = StringVar()
	stockVar2 = StringVar()


	#plt.plot(x, x)
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=1, columnspan=4)
	fig.suptitle('Stock Exchange Activity (15 Days)')
	ax = fig.add_subplot(111)
	ax.set_ylabel("Exchange Open in M$")
	ax.plot(x, label='NASDAQ')
	ax.plot(y, label='NYSE')
	ax.plot(z, label='LON')
	#ax.plot(a, label='HOOP')
	ax.legend(prop={'size':12})
	'''
def myGraph():
	clear(root)
	root.wm_title("Stock Market App - Stock Comparison")
	root.geometry("654x760")
	'''
		use Figure attribute figsize=(int, int) to determine size of plot
	'''
	fig = plt.Figure(facecolor='w', edgecolor='w')
	x = numpy.arange(12)
	y = numpy.sqrt([81,99,100,29,10,29,19,55,53,4, 9, 100])
	z = [10,23,39,40,29,01,11,16,8,12]
	a = [7,8,9,10,9,8,7,6,5,4,3,2,10]

	stockVar1 = StringVar()
	stockVar2 = StringVar()
	Frame(root, height=10, width=10).grid(row=0, column=0, columnspan = 4)	
	Button(root ,text='Compare Stocks').grid(row=1,column=0)
	stock1Entry = Spinbox(root, width = 10,values=('Google','Poople', 'Coople', 'Hoople')).grid(row=1, column=1, sticky=W)	
	stock2Entry = Spinbox(root, width = 10,values=('Poople','Google', 'Coople', 'Hoople')).grid(row=1, column=2, sticky=W)	
	stock3Entry = Spinbox(root, width = 10,values=( 'Coople', 'Hoople','Google','Poople')).grid(row=1, column=3, sticky=W)	


	#plt.plot(x, x)
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=3, columnspan=4)
	fig.suptitle('Compare: Google, Poople, and Coople')
	Frame(root, height=10, width=10).grid(row=2, column=0, columnspan = 4)	
	ax = fig.add_subplot(111)
	ax.set_xlabel("Time")
	ax.set_ylabel("Price $")
	ax.plot(x, label='GOOG')
	ax.plot(y, label='POOP')
	ax.plot(z, label='COOP')
	#ax.plot(a, label='HOOP')
	ax.legend(prop={'size':12})


	Frame(root, height=10, width=10).grid(row=4, column=0, columnspan = 4)
	Label(root, width = 30, text="Stocks compared are: ").grid(row=5, column=0)
	Label(root, width = 10, fg="blue",text="Google").grid(row=5, column=1)
	Label(root, width = 10, fg="#006400",text="Poople").grid(row=5, column=2)
	Label(root, width = 10, fg="red",text="Coople").grid(row=5, column=3)
	
	Label(root, width = 30, text="Stocks Date: ").grid(row=6, column=0)
	Label(root, width = 10, fg="blue",text="meh").grid(row=6, column=1)
	Label(root, width = 10, fg="#006400",text="meh").grid(row=6, column=2)
	Label(root, width = 10, fg="red",text="meh").grid(row=6, column=3)

	Label(root, width = 30, text="Stocks Price: ").grid(row=7, column=0)
	Label(root, width = 15, fg="blue",text="$280").grid(row=7, column=1)
	Label(root, width = 15, fg="#006400",text="$10").grid(row=7, column=2)
	Label(root, width = 15, fg="red",text="$10").grid(row=7, column=3)

	Label(root, width = 30, text="Stocks Open: ").grid(row=8, column=0)
	Label(root, width = 15, fg="blue",text="Google").grid(row=8, column=1)
	Label(root, width = 15, fg="#006400",text="Poople").grid(row=8, column=2)
	Label(root, width = 15, fg="red",text="Poople").grid(row=8, column=3)

	Label(root, width = 30, text="Stocks High: ").grid(row=9, column=0)
	Label(root, width = 15, fg="blue",text="Google").grid(row=9, column=1)
	Label(root, width = 15, fg="#006400",text="Poople").grid(row=9, column=2)
	Label(root, width = 15, fg="red",text="Poople").grid(row=9, column=3)

	Label(root, width = 30, text="Stocks Volumn: ").grid(row=10, column=0)
	Label(root, width = 15, fg="blue",text="some").grid(row=10, column=1)
	Label(root, width = 15, fg="#006400",text="value").grid(row=10, column=2)
	Label(root, width = 15, fg="red",text="Poople").grid(row=10, column=3)

	Label(root, width = 30, text="Stocks Close: ").grid(row=11, column=0)
	Label(root, width = 15, fg="blue",text="some").grid(row=11, column=1)
	Label(root, width = 15, fg="#006400",text="value").grid(row=11, column=2)
	Label(root, width = 15, fg="red",text="Poople").grid(row=11, column=3)

	Label(root,text="________________________________________________________________________________________________").grid(row = 12, columnspan=4, column=0)

	Label(root, width = 30, text="Analysis Recommends: ").grid(row=13, column=0)
	Label(root, width = 15, font = "Helvetica 14 bold",fg="blue",text="Buy").grid(row=13, column=1)
	Label(root, width = 15, font = "Helvetica 14 bold", fg="#006400",text="Sell").grid(row=13, column=2)
	Label(root, width = 15, font = "Helvetica 14 bold",fg="red",text="Hold").grid(row=13, column=3)
	#plt.show()


def createPopup(popupType, message):

	if popupType == "login":
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

		return
	elif popupType =='register':
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

	elif popupType =='firm':
		'''realstock = json.dumps(getQuotes('AAPL'), indent=2)
		print(realstock)'''
		firmPopup = Toplevel(root)
		firmPopup.title("Firm")
		firmPopup.geometry('250x80')
		firmPopup.transient(root)
		firmPopup.resizable(width=FALSE, height=FALSE)

		Frame(firmPopup, height=10, width=10).grid(row=0, column=0, columnspan = 3)
		Label(firmPopup, width=30, text="Firm Association").grid(row=1,columnspan = 3, column=1, sticky=W)
		Frame(firmPopup, height=10, width=10).grid(row=2, column=0, columnspan = 3)
		Button(firmPopup, text="New Firm", command= lambda: firmRegisterForm(1) ).grid(row=3, column=1, sticky=E)
		Button(firmPopup, text="Existing Firm", command= lambda: firmRegisterForm(2)).grid(row=3, column=2, sticky=E)

	elif popupType=='notification':
		notificationPopup = Toplevel(root)
		notificationPopup.title("Notification")
		notificationPopup.geometry('250x80')
		notificationPopup.transient(root)
		notificationPopup.resizable(width=FALSE, height=FALSE)

		Frame(notificationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
		Label(notificationPopup, width=30, text="This Is a Notification").grid(row=1,columnspan = 2, column=1, sticky=W)
		Frame(notificationPopup, height=10, width=10).grid(row=2, column=0, columnspan = 2)
		Button(notificationPopup, text="View").grid(row=3, columnspan=3, column=0)

	elif popupType=='validateClient':
		if message == 'Registration Successful!':
			validationPopup = Toplevel(root)
			validationPopup.title("Congratulations")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message+'\n Please Login').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		else:
			validationPopup = Toplevel(root)
			validationPopup.title("Validation")
			#validationPopup.geometry('250x80')
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='validateBroker':
		if message == 'Registration Successful!':
			validationPopup = Toplevel(root)
			validationPopup.title("Continue Registration")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message+'\n Please Proceed to registering your \n Firm affiliation by selecting an option').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="New Firm", command= lambda: firmRegisterForm(1) ).grid(row=3, column=1, sticky=E)
			Button(validationPopup, text="Existing Firm", command= lambda: firmRegisterForm(2)).grid(row=3, column=2, sticky=W)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		else:
			validationPopup = Toplevel(root)
			validationPopup.title("Validation")
			#validationPopup.geometry('250x80')
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)
	elif popupType=='error':
		print("Error! No records found.")
		loginPopup = Toplevel(root)
		loginPopup.title("Error")
		loginPopup.geometry('252x97')
		loginPopup.transient(root)
		loginPopup.resizable(width=FALSE, height=FALSE)


		Frame(loginPopup, height=10).grid(row=0, column=0)
		Label(loginPopup, text="Error ").grid(row=1, column=0, sticky=W)

def forceLogin():
	print("IN forceLogin")
	global loggedin
	print("loggedin before: "+str(loggedin))
	loggedin = True
	print("loggedin after: "+str(loggedin))
	windowMenus(root)

def forceLogout():
	print("IN forceLogout")
	global loggedin
	print("loggedin before: "+str(loggedin))
	loggedin = False
	print("loggedin after: "+str(loggedin))
	windowMenus(root)
	home()

def checkLogin():
	print("loggedin in check: "+str(loggedin))	

def logout():
	print("In logout")
	home()

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
	firmMenu = Menu(menubar)
	disableMenu = Menu(menubar)

	menubar.add_cascade(menu=accountMenu, label='Account')
	menubar.add_cascade(menu=stocksMenu, label="Stocks")
	menubar.add_cascade(menu=firmMenu, label="Firm")
	menubar.add_cascade(menu=omarMenu, label="Omar's Tool")
	menubar.add_cascade(menu=helpMenu, label="Help")
	

	omarMenu.add_command(label="Force Login", command= lambda: forceLogin())
	omarMenu.add_command(label="Check Login", command= lambda: checkLogin())
	omarMenu.add_command(label="Force Logout", command= lambda: forceLogout())
	omarMenu.add_separator()

	accountMenu.add_command(label="Login", accelerator='cmd-l', command= lambda: createPopup('login', ''))
	registerMenu=accountMenu.add_command(label="Register", accelerator = 'cmd-r',command=lambda :createPopup('register',''))
	accountMenu.add_separator()
	accountMenu.add_command(label="Edit Info",accelerator="cmd-e", command= lambda: editClientInfo(root,'user'))
	accountMenu.add_command(label="View History", command="")
	accountMenu.add_separator()
	accountMenu.add_command(label="Bleh", command="")


	stocksMenu.add_command(label="View Portfolio", accelerator="cmd-p",command= lambda: myGraph())
	stocksMenu.add_separator()
	stocksMenu.add_command(label="View Stock Market", accelerator="cmd-v", command="")
	stocksMenu.add_command(label="Compare Stocks", accelerator="cmd-c", command=lambda: myGraph())
	stocksMenu.add_separator()
	stocksMenu.add_command(label="Sell", accelerator="cmd-s",command="")
	stocksMenu.add_command(label="Buy", accelerator="cmd-b",command="")
	stocksMenu.add_command(label="Trade", accelerator="cmd-t",command="")

	firmMenu.add_command(label="Register Firm",accelerator="cmd-f",command= lambda: firmRegisterForm(3))
	firmMenu.add_separator()
	firmMenu.add_command(label="View Registered Firms", command="")
	
	helpMenu.add_separator()
	helpMenu.add_command(label="Software Tutorial", command="")
	helpMenu.add_command(label="Hotkey List", accelerator="cmd-k", command= lambda: hotkeyWindow(root))

	'''
		Default hotkeys
	'''
	root.bind('<Command-l>', lambda e: createPopup('login', ''))
	root.bind('<Command-r>', lambda e: createPopup('register','')) 
	root.bind('<Command-c>', lambda e: myGraph())
	root.bind('<Command-k>', lambda e: hotkeyWindow(root))

	if loggedin == True:
		'''
		if logged in enable additional hotkeys and menu options
		'''
		root.bind('<Command-p>', lambda e: myGraph()) 
		root.bind('<Command-e>', lambda e: editClientInfo(root,'username')) 
		root.bind('<Command-f>', lambda e: firmRegisterForm(3)) 
		root.bind('<Command-l>', lambda e: forceLogout())

		accountMenu.entryconfig("Login", label="Log Out", command=lambda: forceLogout())
		stocksMenu.entryconfig("Sell", state="normal")
		stocksMenu.entryconfig("Buy", state="normal")
		stocksMenu.entryconfig("Trade", state="normal")
		stocksMenu.entryconfig("Sell", state="normal")
		stocksMenu.entryconfig("View Portfolio", state="normal")

		accountMenu.entryconfig("Edit Info", state="normal")
		accountMenu.entryconfig("View History", state="normal")

	
	elif loggedin == False:
		'''
		if NOT logged in disable additional hotkeys and menu options
		'''
		stocksMenu.entryconfig("Sell", state="disabled")
		stocksMenu.entryconfig("Buy", state="disabled")
		stocksMenu.entryconfig("Trade", state="disabled")
		stocksMenu.entryconfig("Sell", state="disabled")
		stocksMenu.entryconfig("View Portfolio", state="disabled")

		root.bind('<Command-p>',"") 
		root.bind('<Command-e>',"") 
		root.bind('<Command-f>',"") 

		accountMenu.entryconfig("Edit Info", state="disabled")
		accountMenu.entryconfig("View History", state="disabled")


def editClientInfo(root, username):
	print("This will edit a Client's info")
	clear(root)
	root.wm_title("Stock Market App - Edit Information")
	root.geometry("500x460")
	Frame(root, height=10).grid(row=0, column=0)
	
	#Frame(root, height=10).grid(row=2, column=0)
	Label(root,height=2,text="Edit Information __________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

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
	budgetEntry = Spinbox(root, width = 33, textvariable=budgetVar, values=(1000,2500,5000,10000,25000,50000,100000)).grid(row=9, column=1, sticky=W)

	Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
	industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

	Label(root,height=2,text="Representation ___________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

	Label(root, width=20, text="Representative: ").grid(row=12, column=0, sticky=W)
	authorityEntry = Entry(root,width=35,textvariable=brokerVar).grid(row=12, column=1, sticky=W)			
	
	Label(root, width=20, text="Firm: ").grid(row=13, column=0, sticky=W)
	authorityEntry = Entry(root,width=35,textvariable=firmVar).grid(row=13, column=1, sticky=W)			
	
	Label(root,height=2,text=" _________________________________________________________________").grid(row=14, column=0, sticky=E, columnspan=2)		
	
	#Frame(root, height=10).grid(row=15, column=0)
	# def register(name, number, email, username, password, budget, industry):
	Button(root, text="Cancel", command=lambda: editClientInfo(root,'user')).grid(row=16, column=1, sticky=W)		
	Button(root, text="Submit", command=lambda: 
		register(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(), budgetVar.get(), industryVar.get(), brokerVar.get(), firmVar.get())).grid(row=16, column=1, sticky=E)		
def main():
	
	root.tk.call('tk', 'windowingsystem') 
	root.wm_title("Stock Market App - Home")
	root.geometry("500x500")
	home()
	root.resizable(width=FALSE, height=FALSE)
	windowMenus(root)

	if not os.path.exists('SMfiles'):
		os.makedirs('SMfiles')
		os.makedirs('SMfiles/users')
		os.makedirs('SMfiles/stocks')
		os.makedirs('SMfiles/indexes')
		os.makedirs('SMfiles/firms')
		os.makedirs('SMfiles/notifications')

	if not os.listdir('SMfiles/notifications'): 
		print "Notifications Empty"
	else:
		createPopup('notification',root)

	root.mainloop()
if __name__ == "__main__":
	main()
