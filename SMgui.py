import Tkinter
from Tkinter import *

import cPickle as pickle

import re

import locale

import stock_backend
from stock_backend import *

import analysis
from analysis import *

import sys
from sys import *

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
googleprice = []


loggedin = False
loggedInAccount = ''

registeredFirms=[]
registeredUsers = []
registeredClients =[]
registeredBrokers = []
quotelist = []
availableStocks = []
symblist={}
ticker_list={}

email_pattern = re.compile(r"^[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.(ca|com)$")

def retrieveFirm(firmName, code):
	
	'''
		This will retrieve an exsiting firm based on its ID

	'''
	errorMessage = ''
	global registeredFirms
	
	for firm in registeredFirms:
	
		if firm.FirmName == firmName:
	
			if code == firm.FirmCode:
	
				createPopup('confirmFirmCode',firmName)
				tempBroker.BrokerFirmID = firm.ID
				strfile = 'SMfiles/users/'+tempBroker.ID+'/'+tempBroker.ID+'.txt'
				with open(strfile, 'wb') as f:
					pickle.dump(tempBroker,f)

			else:
	
				createPopup('errorFirmCode',firmName)
		else:
			pass
	


def validateFirm(name, ID, firmType, code, budget):
	'''
		This will Validate a firm being registered
	'''
	errorMessage = ''
	global tempFirm
	budget = re.sub('[,$]', '', budget)

	'''
		VALIDATE Name
	'''
	if not name == '':
		
		tempFirm.FirmName= name
	else:
		errorMessage += 'Firm Name cannot be empty\n'	

	'''
		VALIDATE ID
	'''
	if not ID == '':
		
		tempFirm.ID= ID
	else:
		errorMessage += 'Firm ID cannot be empty\n'	

	'''
		VALIDATE Type
	'''
	if not firmType == '':
		
		tempFirm.FirmType= firmType
	else:
		errorMessage += 'Firm Type cannot be empty\n'	

	'''
		VALIDATE code
	'''
	if not code == '':
		
		tempFirm.FirmCode= code
	else:
		errorMessage += 'Firm ID cannot be empty\n'	

	try:
		float(budget)
		
		tempFirm.FirmBudget = budget
	except ValueError:
		
		errorMessage += 'Budget is invalid\n'		

	

	if not errorMessage == '':
		createPopup('validateFirm', errorMessage)
	else:

		registeredFirms.append(tempFirm)
		createPopup('validateFirm', 'Registration Successful!')
		os.makedirs('SMfiles/firms/'+ID)
		strfile = 'SMfiles/firms/'+ID+'/'+ID+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempFirm,f)
			
			if not tempBroker == '':
				tempBroker.BrokerFirmID = tempFirm.ID

				strfile = 'SMfiles/users/'+tempBroker.ID+'/'+tempBroker.ID+'.txt'
				with open(strfile, 'wb') as f:
					pickle.dump(tempBroker,f)

	
def validateClient(name, number, email, username, password, password2, budget, industry, broker, firm):
	'''
		This will validate a client being registered

	'''
	errorMessage = ''
	global tempClient
	budget = re.sub('[,$]', '', budget)
	number = re.sub('-', '', number)

	'''
		VALIDATE Name
	'''
	if not name == '':
		
		tempClient.ClientName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		tempClient.ClientPhoneNumber = number
	except ValueError:
		errorMessage += 'Phone Number is invalid\n'		


	''' 
		VALIDATE email
	'''
	if email_pattern.match(email):
		tempClient.ClientEmailAddress = email
	else:

		errorMessage += 'Email Address is invalid\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		tempClient.ID = username
	else:
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if not password == '' and not password2 =='':
		if password == password2:
			tempClient.ClientPassword = password
			
		else:
			
			errorMessage += 'Passwords do not match\n'		
	else:
		#createPopup('validateClient', '')
		
		errorMessage += 'Password(s) cannot be left empty\n'		

	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		
		tempClient.ClientBudget = budget
	except ValueError:
		
		errorMessage += 'Budget is invalid\n'		
		

	if not industry =='':
		
		tempClient.ClientIndustry = industry
	else:
		
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
		registeredClients.append(tempClient)
		createPopup('validateClient', 'Registration Successful!')
		os.makedirs('SMfiles/users/'+username)
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempClient,f)

		

	


def validateBroker(name, number, email, username, password, password2, budget, industry, license, authority, year):
	'''
		This will validate a broker
	'''
	budget = re.sub('[,$]', '', budget)
	errorMessage = ''
	global tempBroker

	'''
		VALIDATE Name
	'''
	if not name == '':
		
		tempBroker.BrokerName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		
		tempBroker.BrokerPhoneNumber = number
	except ValueError:
		
		errorMessage += 'Phone Number is invalid\n'		


	''' 
		VALIDATE email
	'''
	if email_pattern.match(email):
		
		tempBroker.BrokerEmailAddress = email
	else:
		
		errorMessage += 'Email Address is invalid\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		
		tempBroker.ID = username
	else:
		
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if not password == '' and not password2 =='':
		if password == password2:
			tempBroker.BrokerPassword = password
		
		else:
		
			errorMessage += 'Passwords do not match\n'			
	else:
		#createPopup('validateClient', '')
		
		errorMessage += 'Password(s) is invalid\n'		

	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		
		tempBroker.BrokerTotalBudget = budget
	except ValueError:
		
		errorMessage += 'Budget is invalid\n'		
		

	'''
		VALIDATE industry
	'''
	if not industry =='':
		
		tempBroker.BrokerIndustry = industry
	else:
		
		errorMessage += 'Industry is invalid\n'				

	'''
		VALIDATE Licence Type
	'''
	if license == 'Financial Advisor FCA' or license == 'Investment Advisor IAR' or license == 'Registered Representative':
		
		tempBroker.BrokerLicenseType = license
	else:
		
		errorMessage += 'License Type is invalid\n'

	'''
		VALIDATE issuing authority
	'''
	if not authority == '':
		
		tempBroker.BrokerAuthority = authority
	else:
		
		errorMessage += 'Issuing Authority invalid\n'

	'''
		VALIDATE year issued
	'''
	try:
		int(year)
		
		tempBroker.BrokerLicenseIssue = year
	except ValueError:
		
		errorMessage += 'License Issuing Year is invalid\n'		




	if not errorMessage == '':
		createPopup('validateBroker', errorMessage)
	else:
		
		createPopup('validateBroker', 'Registration Successful!')
		os.makedirs('SMfiles/users/'+username)
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempBroker,f)
		

def validateBrokerEdit(name, number, email, username, password, password2, budget, industry, license, authority, year):
	'''
		Validate EDIT info for Broker
	'''
	budget = re.sub('[,$]', '', budget)
	errorMessage = ''
	global tempBroker
	global loggedInAccount

	'''
		VALIDATE Name
	'''
	if not name == '':
		
		tempBroker.BrokerName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		
		tempBroker.BrokerPhoneNumber = number
	except ValueError:
		
		errorMessage += 'Phone Number is invalid\n'		

	''' 
		VALIDATE email
	'''
	if not email=='':
		if email_pattern.match(email):
			tempBroker.BrokerEmailAddress = email
			
		else:
			
			tempBroker.BrokerEmailAddress = email
	else:
		errorMessage += 'Passwords do not match\n'		

	''' 
		VALIDATE password
	'''
	if  password == '' and password2 =='':
		tempBroker.BrokerPassword = loggedInAccount.BrokerPassword
		
	elif password == password2 and not password == '':
		tempBroker.BrokerPassword = password
		
	else:

		
		errorMessage += 'Passwords do not match\n'		
	
	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		
		tempBroker.BrokerTotalBudget = budget
	except ValueError:
		
		errorMessage += 'Budget is invalid\n'		
		

	'''
		VALIDATE industry
	'''
	if not industry =='':
		
		tempBroker.BrokerIndustry = industry
	else:
		
		errorMessage += 'Industry is invalid\n'				

	'''
		VALIDATE Licence Type
	'''
	if license == 'Financial Advisor FCA' or license == 'Investment Advisor IAR' or license == 'Registered Representative':
		
		tempBroker.BrokerLicenseType = license
	else:
		
		errorMessage += 'License Type is invalid\n'

	'''
		VALIDATE issuing authority
	'''
	if not authority == '':
		
		tempBroker.BrokerAuthority = authority
	else:
		
		errorMessage += 'Issuing Authority invalid\n'

	'''
		VALIDATE year issued
	'''
	try:
		int(year)
		
		tempBroker.BrokerLicenseIssue = year
	except ValueError:
		
		errorMessage += 'License Issuing Year is invalid\n'		


	tempBroker.ID = username

	if not errorMessage == '':
		createPopup('validateBroker', errorMessage)
	else:
		tempBroker.BrokerPLReport = loggedInAccount.BrokerPLReport
		tempBroker.BrokerProfit = loggedInAccount.BrokerProfit
		tempBroker.Portfolio = loggedInAccount.Portfolio
		tempBroker.InvestmentHistory = loggedInAccount.InvestmentHistory
		tempBroker.InvestmentExpense = loggedInAccount.InvestmentExpense
		tempBroker.InvestmentRevenue = loggedInAccount.InvestmentRevenue
		




		createPopup('validateBrokerEdit', 'Information Edit Successful!')
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempBroker,f)
		loggedInAccount = tempBroker


def logout():
	'''
		logout by clearing the logged in variable
	'''
	global loggedInAccount
	loggedInAccount = ''
	windowMenus(root)
	createPopup('logout','')
	
def login(username, password):
	'''
		login by entering the correct details of an account and initiate the logged in variable
	'''
	global loggedInAccount
	
	if not os.path.exists('SMfiles/users/'+username):
		
		createPopup('loginError-user', username)
	else:
		with open('SMfiles/users/'+username+'/'+username+'.txt','rb') as f:
			tempAccount = pickle.load(f)
		
		if isinstance(tempAccount, Client):
			if password == tempAccount.ClientPassword:
		
				createPopup('login-pass', tempAccount.ClientName)
				global loggedInAccount
				loggedInAccount = tempAccount
			else:
		
				createPopup('loginError-pass', username)
		elif isinstance(tempAccount, Broker):
			if password == tempAccount.BrokerPassword:
				createPopup('login-pass', tempAccount.BrokerName)
				
				
				loggedInAccount = tempAccount
			else:
				createPopup('loginError-pass', username)

def hotkeyWindow(root):
	'''
		HOTKEY WINDOW to help users make the most of the software
		by listing command shortcuts
	'''
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

	Label(text="Buy Stock Hotkey -").grid(row=10, column=0, sticky=E)
	Label(text="%s%s" % (u"\u2318","B"),fg="#006400").grid(row=10, column=1, sticky=W)
	
	Frame(root, height=10).grid(row=13, column=0)
	Label(text="Hotkeys highlighted in Green are only available when Logged In").grid(row=14, column=0, columnspan=2)

def firmRegisterForm(firm):

	'''
		allows you to register a firm through the different scenarious
		1,2 -> through a broker Registration
		3 -> manually through the menu or using command F

		all variables are passed to the respective validation functions
	'''
	if firm == 1:
		
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
		budgetVar = StringVar()
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
		budgetEntry = Spinbox(root, textvariable = budgetVar,width = 33,values=('$10,000.00','$25,000.00','$50,000.00','$100,000.00','$250,000.00','$500,000.00','$1,000,000.00')).grid(row=7, column=1)	
		Frame(root, height=10).grid(row=16, column=0)
		Frame(root, height=10).grid(row=17, column=0)

		Button(root, text="Clear", command=lambda: firmRegisterForm(1)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: validateFirm(nameVar.get(), idVar.get(), typeVar.get(), codeVar.get(), budgetVar.get())).grid(row=18, column=1, sticky=E)		

	elif firm ==2:
		
		clear(root)
		clear(root)
		root.wm_title("Stock Market App - Retrieve Firm")
		root.geometry("500x270")

		firmList = []
		
		for firm in registeredFirms:
			firmList.append(firm.FirmName)
		
		Frame(root, height=10).grid(row=0, column=0)
		
		firm = IntVar()
		Label(root,width=20, text="Firm: ").grid(row=1, column=0, sticky=W)

		Radiobutton(root, text="New Firm", variable=firm, value=1, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=W)
		Radiobutton(root, text="Existing Firm", variable=firm, value=0, command=lambda: firmRegisterForm(firm.get())).grid(row=1, column=1, sticky=E)
		
		#Frame(root, height=10).grid(row=2, column=0)
		Label(root,height=2,text="Firm Information __________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		firmVar = StringVar()
		codeVar = StringVar()
		
		Label(root,width=20, text="Select Firm: ").grid(row=3, column=0, sticky=E)
		firmEntry = Spinbox(root, width = 33,textvariable=firmVar,values=(firmList)).grid(row=3, column=1)	
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
		Button(root, text="Submit", command=lambda: retrieveFirm(firmVar.get(), codeVar.get())).grid(row=18, column=1, sticky=E)		

	elif firm == 3:
		clear(root)
		
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
		budgetVar = StringVar()
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
		budgetEntry = Spinbox(root, width = 33,textvariable=budgetVar,values=('$10,000.00','$25,000.00','$50,000.00','$100,000.00','$250,000.00','$500,000.00','$1,000,000.00')).grid(row=7, column=1)	

		Frame(root, height=10).grid(row=17, column=0)

		Button(root, text="Clear", command=lambda: firmRegisterForm(3)).grid(row=18, column=1, sticky=W)		
		Button(root, text="Next", command=lambda: validateFirm(nameVar.get(), idVar.get(), typeVar.get(), codeVar.get(), budgetVar.get())).grid(row=18, column=1, sticky=E)		
			
def registerForm(accountType):
	'''
		user Regiseration form 
		type1 -> broker
		type2 -> client

		all variables are passed to the respective validation functions
	'''
	
	if accountType == 1:
		
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
		budgetEntry = Spinbox(root, width = 33, textvariable = budgetVar ,values=('$10,000.00','$25,000.00','$50,000.00','$100,000.00','$250,000.00','$500,000.00','$1,000,000.00')).grid(row=9, column=1, sticky=W)

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
		
		brokerList = []
		brokerList.append('If not applicable, skip this field')

		firmList = []
		firmList.append('If not applicable, skip this field')

		for broker in registeredBrokers:
			brokerList.append(broker.BrokerName)

		for firm in registeredFirms:
			firmList.append(firm.FirmName)

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
		budgetEntry = Spinbox(root, width = 33, textvariable=budgetVar, values=('$1,000.00','$2,500.00','$5,000.00','$10,000.00','$25,000.00','$50,000.00','$100,000.00')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Representation ___________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="Representative: ").grid(row=12, column=0, sticky=W)
		brokerEntry = Spinbox(root, width = 33,textvariable = brokerVar, values=brokerList).grid(row=12, column=1, sticky=W)	
		
		Label(root, width=20, text="Firm: ").grid(row=13, column=0, sticky=W)
		firmEntry = Spinbox(root, width = 33,textvariable = firmVar, values=firmList).grid(row=13, column=1, sticky=W)			
		
		Label(root,height=2,text=" _________________________________________________________________").grid(row=14, column=0, sticky=E, columnspan=2)		
		
		Frame(root, height=10).grid(row=15, column=0)
		# def register(name, number, email, username, password, budget, industry):
		Button(root, text="Clear", command=lambda: registerForm(2)).grid(row=16, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: 
			validateClient(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(), passVar2.get(), budgetVar.get(), industryVar.get(), brokerVar.get(), firmVar.get())).grid(row=16, column=1, sticky=E)		

def validateClientEdit(name, number, email, username, password, password2, budget, industry, broker, firm):
	'''
		VALIDATE CLIENT EDIT
	'''
	errorMessage = ''
	global tempClient
	budget = re.sub('[,$]', '', budget)
	number = re.sub('-', '', number)
	global loggedInAccount
	'''
		VALIDATE Name
	'''
	if not name == '':
		
		tempClient.ClientName = name
	else:
		errorMessage += 'Name cannot be empty\n'	

	'''
		VALIDATE phonenumber
	'''	
	try:
		int(number)
		
		tempClient.ClientPhoneNumber = number
	except ValueError:
		
		errorMessage += 'Phone Number is invalid\n'		


	''' 
		VALIDATE email
	'''
	if not email == '':
		if email_pattern.match(email):

			tempClient.ClientEmailAddress = email
	else:
		
		errorMessage += 'Email Address cannot be left empty\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		
		tempClient.ID = username
	else:
		
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if  password == '' and password2 =='':
		tempClient.ClientPassword = loggedInAccount.ClientPassword
		
	elif password == password2 and not password == '':
		tempClient.ClientPassword = password
		
	else:
		errorMessage += 'Passwords do not match\n'		


	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		
		tempClient.ClientBudget = budget
	except ValueError:
		
		errorMessage += 'Budget is invalid\n'		
		

	if not industry =='':
		
		tempClient.ClientIndustry = industry
	else:
	
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
		createPopup('validateClientEdit', errorMessage)
	else:
		createPopup('validateClientEdit', 'Information Edit Successful!')
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		tempClient.ClientPLReport = loggedInAccount.ClientPLReport
		tempClient.Portfolio = loggedInAccount.Portfolio
		tempClient.ClientProfit = loggedInAccount.ClientProfit
		tempClient.ClientProfit = loggedInAccount.ClientProfit
		tempClient.InvestmentHistory = loggedInAccount.InvestmentHistory
		tempClient.InvestmentExpense = loggedInAccount.InvestmentExpense
		tempClient.InvestmentRevenue = loggedInAccount.InvestmentRevenue

		with open(strfile, 'wb') as f:
			pickle.dump(tempClient,f)
		loggedInAccount = tempClient


def clear(yourwindow):
	'''
		loop through the window in the GUI and destroy all widgets
		a quicker (newPage) function
	'''
	for widget in yourwindow.winfo_children():
		widget.destroy()
	windowMenus(yourwindow)

def buyWindow(stock1,duration, quantity, priceVal):
	'''
		users here can view a stock, see what the algorithm recommends
		and if logged in, they can purchase stock(s) as per their budgets

	'''

	clear(root)

	root.wm_title("Stock Market App - Buy Stock")
	root.geometry("654x800")
	
	if stock1 == '':
		stockOption1 = StringVar()
	else:
		stockOption1 = StringVar()
		stockOption1.set(stock1)
		
	
	'''
		use Figure attribute figsize=(int, int) to determine size of plot
	'''
	fig = plt.Figure(facecolor='w', edgecolor='w',figsize=(8, 5))
	
	plotTitle = ''
	stockVar1 = StringVar()
	
	Frame(root, height=10).grid(row=0, column=0, columnspan = 2)	
	Button(root ,text='View Stock Info', command = lambda: buyWindow(stockOption1.get(),durationVar.get(),0,0)).grid(row=1,column=0, sticky=E)
	stock1Entry = Spinbox(root, fg="blue",width = 15,textvariable=stockOption1,values=availableStocks).grid(row=1, column=1, sticky=W)	
	
	xList = []
	
	xLabel = ''
	

	durationVar = IntVar()
	quantityVar = IntVar()



	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=3, columnspan=2)
	quantityAvailable = quantity
	
	
	Label(root, text='Select Duration in Day(s):').grid(row=2, column=0, sticky=E)	
	stock3Entry = Spinbox(root, width = 15,textvariable=durationVar,values=(1,2,5,7,14)).grid(row=2, column=1, sticky=W)	
	Frame(root, height=10, width=10).grid(row=3,columnspan=2, column=0)
	ax = fig.add_subplot(111)

	if stock1 == '' or stock1 =='Select Stock':
		stockOption1.set('Select Stock')
		
	else:
		stockOption1.set(stock1)
		plotTitle += stockOption1.get()
		
		for key,value in ticker_list.iteritems():
			if key == stockOption1.get():
				xLabel = value

		xTestList = get_historical(xLabel, duration)
		for element in xTestList:
			xList.append(element.StockPrice)
		
		ax.plot(xList, label=xLabel)

		

		test00 = stock_estimate(xTestList,xLabel)
		
		'''
			choosing text colour based on recommendation type
			to be more prominent
		'''
		colour = 'black'

		if test00 == 'Sell, as stocks may be reaching peak':	
			colour='red'
		elif test00 == 'Buy, as stocks are at a low point':
			colour='#006400'
		elif test00 == 'Hold, stocks may continue to rise':
			colour='blue'		
		elif test00 == 'Buy, stocks rising from a low':
			colour='#006400'
		elif test00 == 'Sell, stocks dropping from a high':
			colour='red'
		elif test00 == 'Hold, stable fluctuation':
			colour='blue'	

		Label(root, fg="blue",text=stockOption1.get()).grid(row=5, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockDate).grid(row=6, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockPrice).grid(row=7, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockOpen).grid(row=8, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockDayRange).grid(row=9, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockVolume).grid(row=10, column=1,sticky=W)
		Label(root, fg="blue",text=xTestList[-1].StockClose).grid(row=11, column=1,sticky=W)
		Label(root, font = "Helvetica 14 bold",fg=colour,text=test00).grid(row=13, column=1,sticky=W)

		quantityAvailable = int(xTestList[-1].StockVolume)
		price = float(xTestList[-1].StockPrice)
		


	
	#plt.plot(x, x)
	if duration == 1:
		ax.set_xlabel("Fluctuation over the past day")
	elif duration == 2:
		ax.set_xlabel("Fluctuation over the past 2 days")
	elif duration == 5:
		ax.set_xlabel("Fluctuation over the past 5 days")
	elif duration == 7:
		ax.set_xlabel("Fluctuation over the past week")
	elif duration == 14:	
		ax.set_xlabel("Fluctuation over the past 2 weeks")
	ax.set_ylabel("Price $")
	ax.get_xaxis().set_ticks([])
	fig.suptitle(plotTitle)
	
	#ax.plot(z, label='COOP')
	#ax.plot(a, label='HOOP')
	ax.legend(prop={'size':12})

	if not duration == '':
		durationVar.set(duration)

	Frame(root, height=10).grid(row=4, column=0, columnspan = 2)
	Label(root, text="Stocks compared are: ").grid(row=5, column=0, sticky=E)
	Label(root, text="Current as of: ").grid(row=6, column=0, sticky=E)
	Label(root, text="Price: ").grid(row=7, column=0, sticky=E)
	Label(root, text="Open: ").grid(row=8, column=0, sticky=E)
	Label(root, text="Day Range: ").grid(row=9, column=0, sticky=E)
	Label(root, text="Volume: ").grid(row=10, column=0, sticky=E)
	Label(root, text="Close: ").grid(row=11, column=0, sticky=E)

	Label(root,text="________________________________________________________________________________________________").grid(row = 12, columnspan=2, column=0)

	Label(root, text="Analysis Recommends: ").grid(row=13, column=0,sticky=E)
	
	Label(root,text="________________________________________________________________________________________________").grid(row = 14, columnspan=2, column=0)
	


	if quantityAvailable == 0:
		root.geometry("654x750")
		Label(root, text='Purchase Unavailable. Please Select a Stock to view').grid(row = 16, column=0, columnspan=2)

	else:
		root.geometry("654x840")


		Label(root, text="Select Quantity: ").grid(row=16, column=0, sticky=E)
		quantityEntry = Spinbox(root, width = 15,textvariable=quantityVar,from_=1, to=quantityAvailable).grid(row=16, column=1, sticky=W)	
		price = float(price)
		price = format(float(price), ",.2f")

		Label(root, text="Price Estimate for "+str(quantity)+' Stocks:').grid(row=17, column=0, sticky=E)
		totalPrice = float(price) * quantity

		totalPrice = float(totalPrice)
		displayTotalPrice = format(float(totalPrice), ",.2f")
		Label(root, text='$'+str(displayTotalPrice)).grid(row=17, column=1, sticky=W)


		Frame(root, height=10).grid(row=20, column=0, columnspan = 2)
		Button(root ,text='Estimate', command = lambda: buyWindow(stockOption1.get(),durationVar.get(),quantityVar.get(),price)).grid(row=20,column=0, sticky=E)
		'''
			validate budget and calculate quote based on
			account type and info
		'''

		if isinstance(loggedInAccount,Broker) == True:
			budget = float(loggedInAccount.BrokerTotalBudget)
			displayBudget = format(float(budget), ",.2f")
			
			Label(root, text="Current Budget: ").grid(row=18, column=0, sticky=E)
			
			if  float(totalPrice)==0.0:
				buyButton = Button(root ,text='Buy', state ='disabled').grid(row=20,column=1, sticky=W)
				Label(root, fg='#006400',text='$'+displayBudget).grid(row=18, column=1, sticky=W)

			if float(budget) < float(totalPrice):
				
				Label(root, fg='red',text='$'+str(displayBudget)).grid(row=18, column=1, sticky=W)
				buyButton = Button(root ,text='Buy', state ='disabled').grid(row=20,column=1, sticky=W)
			
			elif not float(totalPrice) == 0.0:
				Label(root, fg='#006400',text='$'+displayBudget).grid(row=18, column=1, sticky=W)
				

				Label(root,text='Budget after purchase:').grid(row=19, column=0, sticky=E)
				newBudget = float(budget) - float(totalPrice)
				newBudget = format(float(newBudget), ",.2f")
				Label(root,text='$'+str(newBudget)).grid(row=19, column=1, sticky=W)

				buyButton = Button(root ,text='Buy', command=lambda: buy(loggedInAccount,xLabel,quantityVar.get(),totalPrice)).grid(row=20,column=1, sticky=W)


				

		elif isinstance(loggedInAccount, Client) ==True:
			budget = float(loggedInAccount.ClientBudget)
			displayBudget = format(float(budget), ",.2f")
			
			Label(root, text="Current Budget: ").grid(row=18, column=0, sticky=E)
			
			if  float(totalPrice)==0.0:
				buyButton = Button(root ,text='Buy', state ='disabled').grid(row=20,column=1, sticky=W)
				Label(root, fg='#006400',text='$'+displayBudget).grid(row=18, column=1, sticky=W)

			if float(budget) < float(totalPrice):
				
				Label(root, fg='red',text='$'+str(displayBudget)).grid(row=18, column=1, sticky=W)
				buyButton = Button(root ,text='Buy', state ='disabled').grid(row=20,column=1, sticky=W)
			
			elif not float(totalPrice) == 0.0:
				Label(root, fg='#006400',text='$'+displayBudget).grid(row=18, column=1, sticky=W)
				

				Label(root,text='Budget after purchase:').grid(row=19, column=0, sticky=E)
				newBudget = float(budget) - float(totalPrice)
				newBudget = format(float(newBudget), ",.2f")
				Label(root,text='$'+str(newBudget)).grid(row=19, column=1, sticky=W)

				buyButton = Button(root ,text='Buy', command=lambda: buy(loggedInAccount,xLabel,quantityVar.get(),totalPrice)).grid(row=20,column=1, sticky=W)

		quantityVar.set(quantity)
def portfolioWindow():
	'''
		retrieve and list all investments in a user's portfolio
	'''
	clear(root)
	root.geometry("500x500")
	root.wm_title('Stock Market App - Portfolio')

	frame=Frame(root,width=500,height=500)
	frame.grid(row=0,column=0)
	canvas=Canvas(frame,width=478,height=491)

	y = 10


	if isinstance(loggedInAccount,Client) ==True:
		
		if len(loggedInAccount.Portfolio) == 0:
			canvas_id = canvas.create_text(239, 245, anchor="center")
			canvas.itemconfig(canvas_id, text='You have no investment(s) in your current portfolio')
			canvas.config(width=478,height=491)
			canvas.pack(side=LEFT,expand=True,fill=BOTH)	
		else:
		
			x = len(loggedInAccount.Portfolio)

			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, text='The following is a list of current investment(s):')	

			y += 30
			for element in loggedInAccount.Portfolio:
				test00 = stock_estimate(loggedInAccount.Portfolio, element.StockID)
				
				line = canvas.create_line(10, y, 490, y)
				y+=3

				canvas_id = canvas.create_text(10, y+5, anchor="nw")
				canvas.itemconfig(canvas_id, fill='blue',text=str(element.StockID))
				button1 = Button(canvas, text = "Sell", command = lambda j=loggedInAccount.Portfolio.index(element): sell(loggedInAccount,j), anchor ="ne")
				button1_window = canvas.create_window(450, y-1, anchor=NE, window=button1)

				y+=30
				line = canvas.create_line(10, y, 497, y)

				y+=3
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Trade Date & Time:")


				canvas_id = canvas.create_text(135, y, anchor="nw")
				canvas.itemconfig(canvas_id,text=str(element.TradeDate))

				priceT = format(float(element.PriceTraded), ",.2f")

				y+=20
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Trade Price: ")
				

				canvas_id = canvas.create_text(85, y, anchor="nw")
				canvas.itemconfig(canvas_id, text='$'+str(priceT))

				y+=20
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Volume Owned:")

				canvas_id = canvas.create_text(115, y, anchor="nw")
				canvas.itemconfig(canvas_id,text=str(element.Volume))

				y+=20

				'''
					choosing a colour based on analysis response
					to make the recommendation more prominent

				'''

				colour = 'black'

				if test00 == 'Sell, as stocks may be reaching peak':
					
					colour='red'
				elif test00 == 'Buy, as stocks are at a low point':
					
					colour='#006400'
				elif test00 == 'Hold, stocks may continue to rise':
					
					colour='blue'		
				elif test00 == 'Buy, stocks rising from a low':
					
					colour='#006400'
				elif test00 == 'Sell, stocks dropping from a high':
					
					colour='red'
				elif test00 == 'Hold, stable fluctuation':
					
					colour='blue'	

				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Analysis Recommends:")

				canvas_id = canvas.create_text(155, y, anchor="nw")
				canvas.itemconfig(canvas_id,fill = colour, text=str(test00))				
				
				y+=40
			
			if x*140 <500:
				canvas.config(scrollregion=(0,0,478,0))
				canvas.config(width=478,height=491)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
			else:
				scrollh = (x*140)
				scrollh += 30
				canvas.config(scrollregion=(0,0,478,scrollh))
				vbar=Scrollbar(frame,orient=VERTICAL)
				vbar.pack(side=RIGHT,fill=Y)
				vbar.config(command=canvas.yview)
				canvas.config(width=478,height=491)
				canvas.config( yscrollcommand=vbar.set)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
	
		'''
		Based on account type, loop through and add to the scrollable canvas
		all the entries and data whilst incrementing the y coordinate counter

		'''
	elif isinstance(loggedInAccount,Broker) ==True:
		
		if len(loggedInAccount.Portfolio) == 0:
			canvas_id = canvas.create_text(239, 245, anchor="center")
			canvas.itemconfig(canvas_id, text='You have no investment(s) in your current portfolio')
			canvas.config(width=478,height=491)
			canvas.pack(side=LEFT,expand=True,fill=BOTH)	
		else:


			x = len(loggedInAccount.Portfolio)

			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, text='The following is a list of current investment(s):')	

			y += 30
			for element in loggedInAccount.Portfolio:
				test00 = stock_estimate(loggedInAccount.Portfolio, element.StockID)
				
				line = canvas.create_line(10, y, 490, y)
				y+=3

				canvas_id = canvas.create_text(10, y+5, anchor="nw")
				canvas.itemconfig(canvas_id, fill='blue',text=str(element.StockID))
				button1 = Button(canvas, text = "Sell", command = lambda j=loggedInAccount.Portfolio.index(element): sell(loggedInAccount,j), anchor ="ne")
				button1_window = canvas.create_window(450, y-1, anchor=NE, window=button1)

				y+=30
				line = canvas.create_line(10, y, 497, y)

				y+=3
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Trade Date & Time:")


				canvas_id = canvas.create_text(135, y, anchor="nw")
				canvas.itemconfig(canvas_id,text=str(element.TradeDate))

				priceT = format(float(element.PriceTraded), ",.2f")

				y+=20
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Trade Price: ")
				
				

				canvas_id = canvas.create_text(85, y, anchor="nw")
				canvas.itemconfig(canvas_id, text='$'+str(priceT))

				y+=20
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Volume Owned:")

				canvas_id = canvas.create_text(115, y, anchor="nw")
				canvas.itemconfig(canvas_id,text=str(element.Volume))

				y+=20
				'''
					choose recommendation highlight colour

				'''
				colour = 'black'

				if test00 == 'Sell, as stocks may be reaching peak':
					
					colour='red'
				elif test00 == 'Buy, as stocks are at a low point':
					
					colour='#006400'
				elif test00 == 'Hold, stocks may continue to rise':
					
					colour='blue'		
				elif test00 == 'Buy, stocks rising from a low':
					
					colour='#006400'
				elif test00 == 'Sell, stocks dropping from a high':
					
					colour='red'
				elif test00 == 'Hold, stable fluctuation':
					
					colour='blue'	

				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Analysis Recommends:")

				canvas_id = canvas.create_text(155, y, anchor="nw")
				canvas.itemconfig(canvas_id,fill = colour, text=str(test00))				
				y+=40
			
			if x*140 <500:
				canvas.config(scrollregion=(0,0,478,0))
				canvas.config(width=478,height=491)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
			else:
				scrollh = (x*140)
				scrollh += 30
				canvas.config(scrollregion=(0,0,478,scrollh))
				vbar=Scrollbar(frame,orient=VERTICAL)
				vbar.pack(side=RIGHT,fill=Y)
				vbar.config(command=canvas.yview)
				canvas.config(width=478,height=491)
				canvas.config( yscrollcommand=vbar.set)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
	

def historyWindow():
	'''
		retrieve and list all transactions a user has made
	'''
	clear(root)
	root.geometry("500x500")
	root.wm_title('Stock Market App - History')

	frame=Frame(root,width=500,height=500)
	frame.grid(row=0,column=0)
	canvas=Canvas(frame,width=478,height=491)

	y = 10



	username = loggedInAccount.ID

	if os.path.exists('SMfiles/users/'+username+'/transactions.txt'):
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text='The following is a History of your transaction(s):')	

		y += 30
		with open('SMfiles/users/'+username+'/transactions.txt','rb') as f:
			tempList = pickle.load(f)
			x = len(tempList)
			for element in tempList:
					
				line = canvas.create_line(10, y, 490, y)
				y+=3

				canvas_id = canvas.create_text(10, y+5, anchor="nw")
				canvas.itemconfig(canvas_id, fill='blue',text=str(element.TransactionID))

				y+=30
				line = canvas.create_line(10, y, 497, y)

				y+=3
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Transaction Time:")


				canvas_id = canvas.create_text(125, y, anchor="nw")
				canvas.itemconfig(canvas_id,text=str(element.TransactionTime))


				y+=20
				canvas_id = canvas.create_text(10, y, anchor="nw")
				canvas.itemconfig(canvas_id, text="Transaction Type: ")
				

				if element.TransactionType == 'buy':
					canvas_id = canvas.create_text(125, y, anchor="nw")
					canvas.itemconfig(canvas_id, text='Purchase')
					y+=20
					canvas_id = canvas.create_text(10, y, anchor="nw")
					canvas.itemconfig(canvas_id, text="Buyer:")

					canvas_id = canvas.create_text(55, y, anchor="nw")
					canvas.itemconfig(canvas_id,text=str(element.TransactionBuyer))
					inv = element.TransactionPLReport
					
				else:
					canvas_id = canvas.create_text(125, y, anchor="nw")
					canvas.itemconfig(canvas_id, text='Sell')

					y+=20

					canvas_id = canvas.create_text(10, y, anchor="nw")
					canvas.itemconfig(canvas_id, text="Seller:")

					canvas_id = canvas.create_text(55, y, anchor="nw")
					canvas.itemconfig(canvas_id, text=str(element.TransactionSeller))				

					inv = element.TransactionPLReport
					
					
				

				y+=40
			
			if x*117 <500:
				canvas.config(scrollregion=(0,0,478,0))
				canvas.config(width=478,height=491)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
			else:
				scrollh = (x*117)
				scrollh += 30
				canvas.config(scrollregion=(0,0,478,scrollh))
				vbar=Scrollbar(frame,orient=VERTICAL)
				vbar.pack(side=RIGHT,fill=Y)
				vbar.config(command=canvas.yview)
				canvas.config(width=478,height=491)
				canvas.config( yscrollcommand=vbar.set)
				canvas.pack(side=LEFT,expand=True,fill=BOTH)
	else:
		
		canvas_id = canvas.create_text(239, 245, anchor="center")
		canvas.itemconfig(canvas_id, text='You have no Transaction(s) showcasing your history')
		canvas.config(width=478,height=491)
		canvas.pack(side=LEFT,expand=True,fill=BOTH)	
	

def buy(user, symb, quantity, total):
	'''
		Allows user to purchase a stock using its ID
	'''
	# load transaction file
	userpath = 'SMfiles/users/'+user.ID+'/'+user.ID+'.txt'
	transpath = 'SMfiles/users/'+user.ID+'/transactions.txt'
	#transactions = pickle.load(open(transpath,"rb"))

	if not os.path.exists(transpath):
		transactions = []       
	else:
		transactions = pickle.load(open(transpath,"rb"))        

    # add investment into user portfolio
	inv = Investment(get_current(symb),quantity)
	user.Portfolio.append(inv)

	# check user type to subtract from their budget
	# subtract from client's budget
	if isinstance(user, Client):
		originalBudget = float(user.ClientBudget)
		originalBudget -= total # ---------------- this is fixed
		user.ClientBudget = originalBudget
	# subtract from broker's budget
	elif isinstance(user, Broker):
		originalBudget = float(user.BrokerTotalBudget)
		originalBudget -= total # ---------------- this is fixed
		user.BrokerTotalBudget = originalBudget
	# subtract from the buyer of the firm's budget
	else:
		user.FirmBudget -= total

	# add investment into transaction file
	trans = Transaction(user, 'buy', inv)
	transactions.append(trans)

	# save transaction and user file
	pickle.dump(transactions, open(transpath, "wb"))
	pickle.dump(user, open(userpath,"wb"))

	createPopup('BuyPopup','Congratulations!\n You have successfully purchased '
	+str(quantity)+' of the stock: '+symb+' for $'+str(total))


	# inv_index will be the index in portfolio of investment to be sold
def sell(user, inv_index): # user: Client, Broker, or Firm object
	'''
		Allows user to sell stocks bought as a single investment entity
	'''
	# load transaction file
	userpath = 'SMfiles/users/'+user.ID+'/'+user.ID+'.txt'
	transpath = 'SMfiles/users/'+user.ID+'/transactions.txt'
	
	if not os.path.exists(transpath):
		pass
	else:
		transactions = pickle.load(open(transpath,"rb"))        
		# get investment from user portfolio
		inv_bought = user.Portfolio[inv_index]
		del user.Portfolio[inv_index]

		# get investment objects
		symb = inv_bought.StockID
		stock = get_current(symb)
		inv_now = Investment(stock,1)

		# add investment to investment history
		user.InvestmentHistory.append([inv_bought, inv_now])

		# calculate profit lost report
		# and adds to user profit
		inves = [inv_bought, inv_now]
		user.calculate_profit_loss(inves)

		# add investment in transaction file
		trans = Transaction(user, 'sell', inv_now)
		trans.calculate_profit_loss(inves)
		transactions.append(trans)

		# save transaction and user files
		pickle.dump(user, open(userpath, "wb"))
		pickle.dump(transactions, open(transpath, "wb"))
		portfolioWindow()

		
def home():
	'''
		HOMEPAGE -> has three states, not logged in, logged in as Client, and logged in as Broker

	'''

	clear(root)
	root.wm_title("Stock Market App - Home")
	root.geometry("500x720")
	windowMenus(root)
	
	if not loggedInAccount == '' and isinstance(loggedInAccount,Broker) == True:
		Frame(root, height=10, width=10).grid(row=0,column=0)
		Label(root, text="Welcome back our Stock Market App, "+loggedInAccount.BrokerName+".").grid(row=1,column=0, columnspan=4)
		Label(root, text="In this homepage, we are happy to catch you up").grid(row=2,column=0, columnspan=4)
		Label(root, text="as to what happened while you were gone!").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		
		
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
		
		
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
		

		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		
		
		xLabel = ''
		yLabel = ''
		

		xList = []
		yList = []
		
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
		
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		
		ax2.plot(yList, label=yLabel)

		
		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
	

	elif not loggedInAccount == '' and isinstance(loggedInAccount,Client) == True:

		Frame(root, height=10, width=10).grid(row=0,column=0)
		Label(root, text="Welcome back our Stock Market App, "+loggedInAccount.ClientName+".").grid(row=1,column=0, columnspan=4)
		Label(root, text="In this homepage, we are happy to catch you up").grid(row=2,column=0, columnspan=4)
		Label(root, text="as to what happened while you were gone!").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
			
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
		
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
	
		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		
		xLabel = ''
		yLabel = ''
		
		xList = []
		yList = []
		
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
		
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		
		ax2.plot(yList, label=yLabel)

		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
		
	else:
		
		Label(root, text="Welcome to our Stock Market App").grid(row=1,column=0, columnspan=4)
		Label(root, text="Please Login or Register to use the App's full functionality").grid(row=2,column=0, columnspan=4)
		Label(root, text="The following dashboard displays notable changes in the stock market").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
	
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
	
		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		
		xLabel = ''
		yLabel = ''
	
		xList = []
		yList = []
		
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
	
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		
		ax2.plot(yList, label=yLabel)

		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
		


def compareStocks(stock1,stock2,stock3,duration):
	'''
		compare and graph stocks side by side in real time based on ID
		get ID, populate a list with realtime selling values of that stock 
		over the user selected period (1,2,5,7,14) days and graph them
	'''

	clear(root)

	root.wm_title("Stock Market App - Stock Comparison")
	root.geometry("660x785")
	
	if stock1 == '':
		stockOption1 = StringVar()
	else:
		stockOption1 = StringVar()
		stockOption1.set(stock1)
		
	if stock2 == '':
		stockOption2 = StringVar()
	else:
		stockOption2 = StringVar()
		stockOption2.set(stock2)
	
	if stock3 == '':
		stockOption3 = StringVar()
	else:
		stockOption3 = StringVar()
		stockOption3.set(stock3)

	'''
		use Figure attribute figsize=(int, int) to determine size of plot
	'''
	fig = plt.Figure(facecolor='w', edgecolor='w')

	plotTitle = 'Compare: '
	
	stockVar1 = StringVar()
	stockVar2 = StringVar()
	stockVar3 = StringVar()
	
	Frame(root, height=10, width=10).grid(row=0, column=0, columnspan = 4)	
	Button(root ,text='Compare Stocks', command = lambda: compareStocks(stockOption1.get(),stockOption2.get(),stockOption3.get(),durationVar.get())).grid(row=1,column=0)

	stock1Entry = Spinbox(root, fg="blue",width = 15,textvariable=stockOption1,values=availableStocks).grid(row=1, column=1, sticky=W)	
	stock2Entry = Spinbox(root, fg="#006400",width = 15,textvariable=stockOption2,values=availableStocks).grid(row=1, column=2, sticky=W)	
	stock3Entry = Spinbox(root, fg="red",width = 15,textvariable=stockOption3,values=availableStocks).grid(row=1, column=3, sticky=W)	

	xList = []
	yList = []
	zList = []

	xLabel = ''
	yLabel = ''
	zLabel = ''

	durationVar = IntVar()

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=3, columnspan=4)
	
	Label(root, text='Select Duration in Day(s):').grid(row=2, column=0, columnspan = 2, sticky=E)	
	stock3Entry = Spinbox(root, width = 15,textvariable=durationVar,values=(1,2,5,7,14)).grid(row=2, column=2, columnspan=2, sticky=W)	
	Frame(root, height=10, width=10).grid(row=3,columnspan=4, column=0)
	ax = fig.add_subplot(111)

	if stock1 == '' or stock1 =='Select Stock':
		stockOption1.set('Select Stock')

	else:
		stockOption1.set(stock1)
		plotTitle += stockOption1.get()+'| '
		
		for key,value in ticker_list.iteritems():
			if key == stockOption1.get():
				xLabel = value

		xTestList = get_historical(xLabel, duration)
		for element in xTestList:
			xList.append(element.StockPrice)
		
		ax.plot(xList, label=xLabel)

		test00 = stock_estimate(xTestList,xLabel)
		
		colour = 'black'
		'''
			choose highlight colour based on recommendation
			to make it more prominent

		'''
		if test00 == 'Sell, as stocks may be reaching peak':
			
			colour='red'
		elif test00 == 'Buy, as stocks are at a low point':
			
			colour='#006400'
		elif test00 == 'Hold, stocks may continue to rise':
			
			colour='blue'		
		elif test00 == 'Buy, stocks rising from a low':
			
			colour='#006400'
		elif test00 == 'Sell, stocks dropping from a high':
			
			colour='red'
		elif test00 == 'Hold, stable fluctuation':
			
			colour='blue'
		
		Label(root, fg="blue",text=stockOption1.get()).grid(row=5, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockDate).grid(row=6, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockPrice).grid(row=7, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockOpen).grid(row=8, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockDayRange).grid(row=9, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockVolume).grid(row=10, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockClose).grid(row=11, column=1)
		Label(root, font = "Helvetica 14 bold",fg=colour,text=test00).grid(row=13, column=1)

	if stock2 == '' or stock2 =='Select Stock':
		stockOption2.set('Select Stock')
	else:
		stockOption2.set(stock2)
		plotTitle += stockOption2.get()+'| '

		for key,value in ticker_list.iteritems():
			if key == stockOption2.get():
				yLabel = value

		yTestList = get_historical(yLabel, duration)
		for element in yTestList:
			yList.append(element.StockPrice)
		ax.plot(yList, label=yLabel)


		test01 = stock_estimate(yTestList,yLabel)
		
		colour1 = 'black'
		'''
			choose highlight colour
		'''
		if test01 == 'Sell, as stocks may be reaching peak':
			
			colour1='red'
		elif test01 == 'Buy, as stocks are at a low point':
			
			colour1='#006400'
		elif test01 == 'Hold, stocks may continue to rise':
			
			colour1='blue'		
		elif test01 == 'Buy, stocks rising from a low':
			
			colour1='#006400'
		elif test01 == 'Sell, stocks dropping from a high':
			
			colour1='red'
		elif test01 == 'Hold, stable fluctuation':
			
			colour1='blue'

		Label(root, fg="#006400",text=stockOption2.get()).grid(row=5, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockDate).grid(row=6, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockPrice).grid(row=7, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockOpen).grid(row=8, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockDayRange).grid(row=9, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockVolume).grid(row=10, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockClose).grid(row=11, column=2)
		Label(root, font = "Helvetica 14 bold", fg=colour1,text=test01).grid(row=13, column=2)

	if stock3 == '' or stock3 =='Select Stock':
		stockOption3.set('Select Stock')
	else:
		stockOption3.set(stock3)
		plotTitle += stockOption3.get()+'| '

		for key,value in ticker_list.iteritems():
			if key == stockOption3.get():
				zLabel = value

		zTestList = get_historical(zLabel, duration)
		for element in zTestList:
			zList.append(element.StockPrice)

		test02 = stock_estimate(zTestList,zLabel)
		
		colour2 = 'black'

		if test02 == 'Sell, as stocks may be reaching peak':
			
			colour2='red'
		elif test02 == 'Buy, as stocks are at a low point':
			
			colour2='#006400'
		elif test02 == 'Hold, stocks may continue to rise':
			
			colour2='blue'		
		elif test02 == 'Buy, stocks rising from a low':
			
			colour2='#006400'
		elif test02 == 'Sell, stocks dropping from a high':
			
			colour2='red'
		elif test02 == 'Hold, stable fluctuation':
			
			colour2='blue'

		ax.plot(zList, label=zLabel)
		Label(root, fg="red",text=stockOption3.get()).grid(row=5, column=3)
		Label(root, fg="red",text=zTestList[-1].StockDate).grid(row=6, column=3)
		Label(root, fg="red",text=zTestList[-1].StockPrice).grid(row=7, column=3)
		Label(root, fg="red",text=zTestList[-1].StockOpen).grid(row=8, column=3)
		Label(root, fg="red",text=zTestList[-1].StockDayRange).grid(row=9, column=3)
		Label(root, fg="red",text=zTestList[-1].StockVolume).grid(row=10, column=3)
		Label(root, fg="red",text=zTestList[-1].StockClose).grid(row=11, column=3)
		Label(root, font = "Helvetica 14 bold",fg=colour2,text=test02).grid(row=13, column=3)

	'''
		change X-axis label based on the number of days selected
	'''
	if duration == 1:
		ax.set_xlabel("Fluctuation over the past day")
	elif duration == 2:
		ax.set_xlabel("Fluctuation over the past 2 days")
	elif duration == 5:
		ax.set_xlabel("Fluctuation over the past 5 days")
	elif duration == 7:
		ax.set_xlabel("Fluctuation over the past week")
	elif duration == 14:	
		ax.set_xlabel("Fluctuation over the past 2 weeks")
	ax.set_ylabel("Price $")
	ax.get_xaxis().set_ticks([])
	fig.suptitle(plotTitle)
	
	ax.legend(prop={'size':12})

	if not duration == '':
		durationVar.set(duration)

	Frame(root, height=10, width=10).grid(row=4, column=0, columnspan = 4)
	Label(root, width = 20, text="Stocks compared are: ").grid(row=5, column=0)
	Label(root, width = 15, text="Current as of: ").grid(row=6, column=0)
	Label(root, width = 15, text="Price: ").grid(row=7, column=0)
	Label(root, width = 15, text="Open: ").grid(row=8, column=0)
	Label(root, width = 15, text="Day Range: ").grid(row=9, column=0)
	Label(root, width = 15, text="Volume: ").grid(row=10, column=0)
	Label(root, width = 15, text="Close: ").grid(row=11, column=0)

	Label(root,text="________________________________________________________________________________________________").grid(row = 12, columnspan=4, column=0)

	Label(root, width = 20, text="Analysis Recommends: ").grid(row=13, column=0)


def viewRegisteredFirmsWindow():
	'''
		this window will loop through the registered firms and show the ones available
		if none are registered, the user will be prompted
	'''

	clear(root)
	root.geometry("500x500")
	root.wm_title('Stock Market App - Registered Firms')

	#Frame(root, height=10, width=10).grid(row = 0, column = 0, )
	frame=Frame(root,width=500,height=500)
	frame.grid(row=0,column=0)
	canvas=Canvas(frame,width=478,height=491)

	y = 10
	

	if len(registeredFirms) == 0:
		canvas_id = canvas.create_text(239, 245, anchor="center")
		canvas.itemconfig(canvas_id, text='There are no registered Firms')
		canvas.config(width=478,height=491)
		canvas.pack(side=LEFT,expand=True,fill=BOTH)	
	else:
		x = len(registeredFirms)

		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text='The following is a list of registerd firms:')	

		y += 30
		for tempFirm in registeredFirms:
			
			
			line = canvas.create_line(10, y, 490, y)
			y+=3

			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, fill='blue',text=str(tempFirm.FirmName))

			y+=20
			line = canvas.create_line(10, y, 490, y)

			y+=3
			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, text="ID:")


			canvas_id = canvas.create_text(30, y, anchor="nw")
			canvas.itemconfig(canvas_id,text=str(tempFirm.ID))

			budget = format(float(tempFirm.FirmBudget), ",.2f")

			y+=20
			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, text="Firm Budget: ")
			

			canvas_id = canvas.create_text(95, y, anchor="nw")
			canvas.itemconfig(canvas_id, text='$'+str(budget))

			y+=20
			canvas_id = canvas.create_text(10, y, anchor="nw")
			canvas.itemconfig(canvas_id, text="Firm Type:")

			canvas_id = canvas.create_text(80, y, anchor="nw")
			canvas.itemconfig(canvas_id,text=str(tempFirm.FirmType))

			
			y+=40
		'''
			decide whether to make the window scrollable based on the number
			of entries, their average height, and the total space they require
			and whether that's larger or smaller than the set window size
			which is 500x500
		'''
		if x*100 <500:

			canvas.config(scrollregion=(0,0,478,0))
			canvas.config(width=478,height=491)
			canvas.pack(side=LEFT,expand=True,fill=BOTH)
		else:
			
			scrollh = (x*106)
			scrollh += 30
			canvas.config(scrollregion=(0,0,478,scrollh))
			vbar=Scrollbar(frame,orient=VERTICAL)
			vbar.pack(side=RIGHT,fill=Y)
			vbar.config(command=canvas.yview)
			canvas.config(width=478,height=491)
			canvas.config( yscrollcommand=vbar.set)
			canvas.pack(side=LEFT,expand=True,fill=BOTH)



def createPopup(popupType, message):
	'''
		Here we have a popup creation method, it's similar to a switch statment
		two arguments are passed from any function denoting the popup type, and the message
		it should relay to the user. This is fairly lengthy.

	'''
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
	
	elif popupType =='register':
		
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
	
	elif popupType=='login-pass':
		errorPopup = Toplevel(root)
		errorPopup.title("Login Successful")
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="Welcome back, "+message+'! ').grid(row=1, column=0, columnspan = 3)
		Label(errorPopup, text='Proceed to enjoy the full functionality of the app').grid(row=2, column=0, columnspan = 3)
		
		Button(errorPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 3)

	elif popupType =='firm':
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
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)
	elif popupType=='validateClientEdit':
		if message == 'Information Edit Successful!':
			validationPopup = Toplevel(root)
			validationPopup.title("Success")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message+'\n').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		else:
			validationPopup = Toplevel(root)
			validationPopup.title("Validation")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)
	
	elif popupType=='validateBrokerEdit':
		if message == 'Information Edit Successful!':
			validationPopup = Toplevel(root)
			validationPopup.title("Success")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message+'\n').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		else:
			validationPopup = Toplevel(root)
			validationPopup.title("Validation")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='BuyPopup':
		if not message == '':
			buyPopup = Toplevel(root)
			buyPopup.title("Success")
			buyPopup.transient(root)
			buyPopup.resizable(width=FALSE, height=FALSE)

			Frame(buyPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(buyPopup,  text=message+'\n').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(buyPopup, text="Okay", command= lambda: buyPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(buyPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		
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
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)
	
	elif popupType=='validateFirm':
		if message == 'Registration Successful!':
			validationPopup = Toplevel(root)
			validationPopup.title("Congratulations")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, text='You have Successfully Registered a Firm').grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

		else:
			validationPopup = Toplevel(root)
			validationPopup.title("Validation")
			validationPopup.transient(root)
			validationPopup.resizable(width=FALSE, height=FALSE)

			Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
			Label(validationPopup, width=30, text=message).grid(row=1,columnspan = 2, column=1, sticky=W)
			Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
			Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType == 'errorFirmCode':

		validationPopup = Toplevel(root)
		validationPopup.title("Error")
		validationPopup.transient(root)
		validationPopup.resizable(width=FALSE, height=FALSE)

		Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
		Label(validationPopup, text='Invalid Authorization code for '+message).grid(row=1,columnspan = 2, column=1, sticky=W)
		Button(validationPopup, text="Okay", command= lambda: validationPopup.destroy()).grid(row=3, columnspan=3, column=0)
		Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType == 'confirmFirmCode':

		validationPopup = Toplevel(root)
		validationPopup.title("Confirmation")
		validationPopup.transient(root)
		validationPopup.resizable(width=FALSE, height=FALSE)

		Frame(validationPopup, height=10, width=10).grid(row=0, column=0, columnspan = 2)
		Label(validationPopup, text='Authorization code for '+message +' Accepted.').grid(row=1,columnspan = 2, column=1, sticky=W)
		Button(validationPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
		Frame(validationPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='loginError-user':
		
		errorPopup = Toplevel(root)
		errorPopup.title("Error")
		#errorPopup.geometry('252x97')
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="Error! No User records found for "+message).grid(row=1, column=0, sticky=W)
		Button(errorPopup, text="Okay", command= lambda: errorPopup.destroy()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='loginError-pass':
		
		errorPopup = Toplevel(root)
		errorPopup.title("Error")
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="Error! Password for user "+message+' is incorrect!').grid(row=1, column=0, sticky=W)
		Button(errorPopup, text="Okay", command= lambda: errorPopup.destroy()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='login-pass':
		
		errorPopup = Toplevel(root)
		errorPopup.title("Login Successful")
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="Welcome back, "+message+'! ').grid(row=1, column=0, columnspan = 3)
		Label(errorPopup, text='Proceed to enjoy the full functionality of the app').grid(row=2, column=0, columnspan = 3)
		
		Button(errorPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 3)
	elif popupType =='register':
		
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
	
	elif popupType=='logout':
		
		errorPopup = Toplevel(root)
		errorPopup.title("Logged out")
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="You have Successfully logged out").grid(row=1, column=0, columnspan = 3)
		Label(errorPopup, text='Come back again soon!').grid(row=2, column=0, columnspan = 3)
		
		Button(errorPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 3)



def windowMenus(root):
	'''
		define and setup menus for the main menu bar and hotkeys
		changing hotkey and menu item availability based on whether
		the user is logged in or not

	'''
	menubar = Menu(root)
	
	root['menu'] = menubar

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
	menubar.add_cascade(menu=helpMenu, label="Help")
	

	accountMenu.add_command(label="Login", accelerator='cmd-l', command= lambda: createPopup('login', ''))
	registerMenu=accountMenu.add_command(label="Register", accelerator = 'cmd-r',command=lambda :createPopup('register',''))
	accountMenu.add_separator()
	accountMenu.add_command(label="Edit Info",accelerator="cmd-e", command= lambda: editInfo())
	accountMenu.add_command(label="View History", command= lambda:  historyWindow())
	accountMenu.add_separator()
	accountMenu.add_command(label="Home", command= lambda: home())


	stocksMenu.add_command(label="View Portfolio", accelerator="cmd-p",command= lambda: portfolioWindow())
	stocksMenu.add_separator()
	stocksMenu.add_command(label="Compare Stocks", accelerator="cmd-c", command=lambda: compareStocks('','','',''))
	stocksMenu.add_separator()
	stocksMenu.add_command(label="Buy", accelerator="cmd-b",command= lambda: buyWindow('','',0,0))

	firmMenu.add_command(label="Register Firm",accelerator="cmd-f",command= lambda: firmRegisterForm(3))
	firmMenu.add_separator()
	firmMenu.add_command(label="View Registered Firms", command= lambda: viewRegisteredFirmsWindow())
	
	helpMenu.add_separator()
	helpMenu.add_command(label="Hotkey List", accelerator="cmd-k", command= lambda: hotkeyWindow(root))

	'''
		Default hotkeys
	'''
	
	root.bind('<Command-r>', lambda e: createPopup('register','')) 
	root.bind('<Command-c>', lambda e: compareStocks('','','',''))
	root.bind('<Command-k>', lambda e: hotkeyWindow(root))
	root.bind('<Command-f>', lambda e: firmRegisterForm(3))
	

	if not loggedInAccount == '':
		'''
		if logged in enable additional hotkeys and menu options
		'''
		
		root.bind('<Command-e>', lambda e: editInfo()) 
		root.bind('<Command-l>', lambda e: logout())
		root.bind('<Command-p>', lambda e: portfolioWindow()) 
		root.bind('<Command-b>', lambda e: buyWindow('','',0,0)) 

		accountMenu.entryconfig("Login", label="Log Out", command=lambda: logout())
		stocksMenu.entryconfig("Buy", state="normal")
		stocksMenu.entryconfig("View Portfolio", state="normal")

		accountMenu.entryconfig("Edit Info", state="normal")
		accountMenu.entryconfig("View History", state="normal")
	
	else:
		'''
		if NOT logged in disable additional hotkeys and menu options
		'''
		stocksMenu.entryconfig("Buy", state="disabled")
		stocksMenu.entryconfig("View Portfolio", state="disabled")

		root.bind('<Command-l>', lambda e: createPopup('login', '')) 

		accountMenu.entryconfig("Edit Info", state="disabled")
		accountMenu.entryconfig("View History", state="disabled")



def editInfo():
	'''
		This function allows a user to edit their personal information.
		Changing the fields needed based on account type (Broker vs Client)

	'''
	global loggedInAccount
	if isinstance(loggedInAccount, Client) == True:
		username = loggedInAccount.ID
		f = open('SMfiles/users/'+username+'/'+username+'.txt','rb')
		loggedInAccount = pickle.load(f)
		
		clear(root)
		root.wm_title("Stock Market App - Edit Information")
		root.geometry("500x460")
		
		Frame(root, height=10).grid(row=0, column=0)
	
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

		nameVar.set(loggedInAccount.ClientName)
		numberVar.set(loggedInAccount.ClientPhoneNumber)
		emailVar.set(loggedInAccount.ClientEmailAddress)
		userVar.set(loggedInAccount.ID)
		budget = float(loggedInAccount.ClientBudget)
		budget = format(float(budget), ",.2f")
		

		industryVar.set(loggedInAccount.ClientIndustry)
		

		brokerList = []
		brokerList.append('If not applicable, skip this field')

		firmList = []
		firmList.append('If not applicable, skip this field')

		for broker in registeredBrokers:
			brokerList.append(broker.BrokerName)

		for firm in registeredFirms:
			firmList.append(firm.FirmName)

		brokerVar.set("If not applicable, skip this field")
		firmVar.set("If not applicable, skip this field")

		Label(root,width=20, text="Client Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="Phone Number: ").grid(row=4, column=0, sticky=E)
		phoneEntry = Entry(root,width=35, textvariable=numberVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Email Address: ").grid(row=5, column=0, sticky=E)
		emailEntry = Entry(root,width=35, textvariable=emailVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Username: ").grid(row=6, column=0, sticky=E)
		Label(root, text=userVar.get()).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="New Password: ").grid(row=7, column=0, sticky=E)
		passEntry1 = Entry(root,width=35, textvariable=passVar1, show="*").grid(row=7, column=1, sticky=W)	

		Label(root,width=20, text="Confirm New Password: ").grid(row=8, column=0, sticky=E)
		passEntry2 = Entry(root,width=35, textvariable=passVar2, show="*").grid(row=8, column=1, sticky=W)	



		Label(root,width=20, text="Budget: ").grid(row=9, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33, textvariable=budgetVar, values=('$1,000','$2,500','$5,000','$10,000','$25,000','$50,000','$100,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Representation ___________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="Representative: ").grid(row=12, column=0, sticky=W)
		brokerEntry = Spinbox(root, width = 33,textvariable = brokerVar, values=brokerList).grid(row=12, column=1, sticky=W)			
		
		Label(root, width=20, text="Firm: ").grid(row=13, column=0, sticky=W)
		firmEntry = Spinbox(root, width = 33,textvariable = firmVar, values=firmList).grid(row=13, column=1, sticky=W)			
		
		Label(root,height=2,text=" _________________________________________________________________").grid(row=14, column=0, sticky=E, columnspan=2)		

		brokerVar.set(loggedInAccount.ClientBrokerID)
		firmVar.set(loggedInAccount.ClientFirmID)
		budgetVar.set(str('$'+budget))
		
		Button(root, text="Cancel", command=lambda: editInfo()).grid(row=16, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: 
			validateClientEdit(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(),passVar2.get(), budgetVar.get(), industryVar.get(), brokerVar.get(), firmVar.get())).grid(row=16, column=1, sticky=E)		
	elif isinstance(loggedInAccount, Broker) == True:
		username = loggedInAccount.ID
		f = open('SMfiles/users/'+username+'/'+username+'.txt','rb')
		loggedInAccount = pickle.load(f)
		
		
		clear(root)
		root.wm_title("Stock Market App - Edit Broker Information")
		root.geometry("500x500")
		
		Frame(root, height=10).grid(row=0, column=0)
		budget = float(loggedInAccount.BrokerTotalBudget)
		budget = format(float(budget), ",.2f")
		
		Label(root,height=2,text="Edit Information ___________________________________________________").grid(row=2, column=0, sticky=E, columnspan=2)

		nameVar = StringVar()
		numberVar = StringVar()
		emailVar = StringVar()
		passVar1 = StringVar()
		passVar2 = StringVar()
		budgetVar = StringVar()
		industryVar = StringVar()
		licenseVar = StringVar()
		authorityVar = StringVar()
		yearVar = StringVar()

		if not loggedInAccount.BrokerFirmID =='':
			with open('SMfiles/firms/'+loggedInAccount.BrokerFirmID+'/'+loggedInAccount.BrokerFirmID+'.txt','rb') as f:
				tempFirm = pickle.load(f)
				firmVar = tempFirm.FirmName
		else:
			firmVar = 'No firm affiliation found'

		nameVar.set(loggedInAccount.BrokerName)
		numberVar.set(loggedInAccount.BrokerPhoneNumber)
		emailVar.set(loggedInAccount.BrokerEmailAddress)

		authorityVar.set(loggedInAccount.BrokerAuthority)
		industryVar.set(loggedInAccount.BrokerIndustry)
		
		budget = float(loggedInAccount.BrokerTotalBudget)
		budget = format(float(budget), ",.2f")

		Label(root,width=20, text="Broker Name: ").grid(row=3, column=0, sticky=E)
		nameEntry = Entry(root,width=35, textvariable=nameVar).grid(row=3, column=1, sticky=W)

		Label(root,width=20, text="Phone Number: ").grid(row=4, column=0, sticky=E)
		phoneEntry = Entry(root,width=35, textvariable=numberVar).grid(row=4, column=1, sticky=W)

		Label(root,width=20, text="Email Address: ").grid(row=5, column=0, sticky=E)
		emailEntry = Entry(root,width=35, textvariable=emailVar).grid(row=5, column=1, sticky=W)	

		Label(root,width=20, text="Username: ").grid(row=6, column=0, sticky=E)
		userEntry = Label(text=loggedInAccount.ID).grid(row=6, column=1, sticky=W)

		Label(root,width=20, text="New Password: ").grid(row=7, column=0, sticky=E)
		passEntry1 = Entry(root,width=35, textvariable=passVar1, show="*").grid(row=7, column=1, sticky=W)	

		Label(root,width=20, text="Confirm New Password: ").grid(row=8, column=0, sticky=E)
		passEntry2 = Entry(root,width=35, textvariable=passVar2, show="*").grid(row=8, column=1, sticky=W)	

		Label(root,width=20, text="Budget: ").grid(row=9, column=0, sticky=E)
		budgetEntry = Spinbox(root, width = 33, textvariable = str(budgetVar) ,values=('$10,000','$25,000','$50,000','$100,000','$250,000','$500,000','$1,000,000')).grid(row=9, column=1, sticky=W)

		Label(root,width=20, text="Industry: ").grid(row=10, column=0, sticky=E)
		industryEntry = Entry(root,width=35, textvariable=industryVar).grid(row=10, column=1, sticky=W)	

		Label(root,height=2,text="Licensing ________________________________________________________").grid(row=11, column=0, sticky=E, columnspan=2)

		Label(root, width=20, text="License Type: ").grid(row=12, column=0, sticky=W)
		licenceEntry = Spinbox(root, width = 33,textvariable = licenseVar, values=('License Type','Registered Representative', 'Investment Advisor IAR', 'Financial Advisor FCA')).grid(row=12, column=1, sticky=W)	
		
		Label(root, width=20, text="Issuing Authority: ").grid(row=13, column=0, sticky=W)
		authorityEntry = Entry(root,width=35, textvariable=authorityVar).grid(row=13, column=1, sticky=W)			
		
		Label(root, width=20, text="Year Issued: ").grid(row=14, column=0, sticky=W)
		budgetEntry = Spinbox(root, width = 33, textvariable = yearVar,from_=1980, to=2015).grid(row=14, column=1, sticky=W)		

		Label(root,height=2,text="Firm Affiliation _____________________________________________________").grid(row=15, column=0, sticky=E, columnspan=2)
		Label(root, width=20, text=firmVar).grid(row=16, column=0, columnspan=2)
				
		Frame(root, height=10).grid(row=17, column=0)
		licenseVar.set(loggedInAccount.BrokerLicenseType)
		budgetVar.set(str('$'+budget))
		yearVar.set(loggedInAccount.BrokerLicenseIssue)
		
		Frame(root, height=10).grid(row=16, column=0)
		Button(root, text="Clear", command=lambda: editInfo()).grid(row=18, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: validateBrokerEdit(nameVar.get(), numberVar.get(), emailVar.get(), loggedInAccount.ID, passVar1.get(), passVar2.get(), budgetVar.get(), industryVar.get(), licenseVar.get(), authorityVar.get(), yearVar.get())).grid(row=18, column=1, sticky=E)		


def hello():
	root.wm_title("Stock Market App - Welcome")
	root.geometry("580x290")
	root.resizable(width=FALSE, height=FALSE)

	Frame(root,height=10, width=10).grid(column = 0, row= 0)
	Label(root, text="Hello and Welcome to our Stock Market App").grid(row=1, column=0)
	Frame(root,height=10, width=10).grid(column = 0, row= 2)
	Label(root, text="A quick reminder of the things you'll need in order to run our application").grid(row=3, column=0)
	Label(root, text="Python Tkinter Library").grid(row=4, column=0)
	Label(root, text="GoogleFinance Framework").grid(row=5, column=0)
	Label(root, text="An Internet Connection").grid(row=6, column=0)
	Frame(root,height=10, width=10).grid(column = 0, row= 7)
	Label(root, text="Keep in mind, our software queries data in real time to get you the latest stock infromation").grid(row=8, column=0)
	Label(root, text="With that in mind, you might experience some delays, but nothing too frustrating.").grid(row=9, column=0)
	Label(root, text="Please Note: Our software is optimized for Mac OSX use. Some Linux OSs also support.").grid(row=10, column=0)
	Frame(root,height=10, width=10).grid(column = 0, row= 11)
	Label(root, text="Lastly, thank you for your time and choosing our app!").grid(row=12, column=0)
	Frame(root,height=10, width=10).grid(column = 0, row= 13)
	Button(root, text='Launch!', command=lambda: home()).grid(row=14, column=0)
def main():
	'''

		THE MAIN! -> GUI LOOP and MENU INITIALIZATION
	'''
	root.tk.call('tk', 'windowingsystem') 
	root.resizable(width=FALSE, height=FALSE)
	hello()
	windowMenus(root)

	if not os.path.exists('SMfiles'):
		os.makedirs('SMfiles')
		os.makedirs('SMfiles/users')
		os.makedirs('SMfiles/stocks')
		os.makedirs('SMfiles/indexes')
		os.makedirs('SMfiles/firms')
		os.makedirs('SMfiles/notifications')
	
	else:
		'''
			populate firm list from registered firms
		'''
		directory = os.listdir('SMfiles/firms')
		if not not directory:
			if directory[0] == '.DS_Store':
				del directory[0]
	
		for element in directory:
			with open('SMfiles/firms/'+element+'/'+element+'.txt','rb') as f:
				tempFirm = pickle.load(f)
			
				registeredFirms.append(tempFirm)

			tempFirm = Firm()

		'''
			populate users list from registered users
		'''
		directory = os.listdir('SMfiles/users')
		if not not directory:
			if directory[0] == '.DS_Store':
				del directory[0]
		
		for element in directory:
			with open('SMfiles/users/'+element+'/'+element+'.txt','rb') as f:
				temp = pickle.load(f)
				if isinstance(temp, Client):
					
					registeredClients.append(temp)
					registeredUsers.append(temp)
					
				elif isinstance(temp, Broker):
					
					registeredBrokers.append(temp)
					registeredUsers.append(temp)
					


	'''
		test main from main.py
	'''
	global symblist
	symblist = {'GOOG' : 'Alphabet Inc.', 'AAPL' : 'Apple Inc.', 'NFLX' : 'Netflix, Inc.', 'AMZN' : 'Amazon.com, Inc.', 'TSLA' : 'Tesla Motors Inc', 'JNJ':'Johnson & Johnson', 'LNKD': 'LinkedIn Corp', 'FB': 'Facebook Inc', 'TWTR':'Twitter Inc', 'AIZ':'Assurant Inc.','ISRG':'Intuitive Surgical Inc.'}
	
	global ticker_list
	ticker_list = {'Alphabet Inc.' : 'GOOG', 'Apple Inc.' : 'AAPL', 'Netflix, Inc.' : 'NFLX', 'Amazon.com, Inc.' : 'AMZN', 'Tesla Motors Inc' : 'TSLA','Johnson & Johnson':'JNJ', 'LinkedIn Corp':'LNKD', 'Facebook Inc':'FB', 'Twitter Inc':'TWTR', 'Assurant Inc.':'AIZ','Intuitive Surgical Inc.':'ISRG'}
	
	close_prices_list = close_prices(symblist)
	
	availableStocks.append('Select Stock')
	
	for key,value in symblist.iteritems():
		availableStocks.append(value)
		quotelist.append(get_historical(key, 1))
	


	

	root.mainloop()
if __name__ == "__main__":
	main()
