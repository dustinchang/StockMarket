import Tkinter
from Tkinter import *

import cPickle as pickle

import re

import locale

import main
from main import *

import sys
from sys import *

import scrapper
from scrapper import *

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
googleprice = []
#print()
'''print tempStock.StockPrice
print tempStock.StockClose'''

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
def retrieveFirm(firmName, code):
	
	print('//////////////////////////////////////////////////////')
	print("Validating Firm Retrieval")
	errorMessage = ''
	global registeredFirms
	print('Find -> '+firmName)
	for firm in registeredFirms:
		print(firm.FirmName)
		if firm.FirmName == firmName:
			print('Firm Found')
			if code == firm.FirmCode:
				print('Code Confirmed')
				createPopup('confirmFirmCode',firmName)
				tempBroker.BrokerID = firm.ID
				os.makedirs('SMfiles/users/'+tempBroker.ID)
				strfile = 'SMfiles/users/'+tempBroker.ID+'/'+tempBroker.ID+'.txt'
				with open(strfile, 'wb') as f:
					pickle.dump(tempBroker,f)

			else:
				print('Invalid Code')
				createPopup('errorFirmCode',firmName)
		else:
			print('Firm NOT found!')
	print('//////////////////////////////////////////////////////')


def validateFirm(name, ID, firmType, code, budget):
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	print("Validating new Firm")
	errorMessage = ''
	global tempFirm
	budget = re.sub('[,$]', '', budget)

	'''
		VALIDATE Name
	'''
	if not name == '':
		print('Name Validation - Clear!')
		tempFirm.FirmName= name
	else:
		errorMessage += 'Firm Name cannot be empty\n'	

	'''
		VALIDATE ID
	'''
	if not ID == '':
		print('ID Validation - Clear!')
		tempFirm.ID= ID
	else:
		errorMessage += 'Firm ID cannot be empty\n'	

	'''
		VALIDATE Type
	'''
	if not firmType == '':
		print('Type Validation - Clear!')
		tempFirm.FirmType= firmType
	else:
		errorMessage += 'Firm Type cannot be empty\n'	

	'''
		VALIDATE code
	'''
	if not code == '':
		print('Code Validation - Clear!')
		tempFirm.FirmCode= code
	else:
		errorMessage += 'Firm ID cannot be empty\n'	

	try:
		float(budget)
		print('Budget Validation - Clear!')
		tempFirm.FirmBudget = budget
	except ValueError:
		print('Budget Validation - Error!')
		errorMessage += 'Budget is invalid\n'		

	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

	if not errorMessage == '':
		createPopup('validateFirm', errorMessage)
	else:

		registeredFirms.append(tempFirm)
		createPopup('validateFirm', 'Registration Successful!')
		os.makedirs('SMfiles/firms/'+ID)
		strfile = 'SMfiles/firms/'+ID+'/'+ID+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempFirm,f)
	
def validateClient(name, number, email, username, password, password2, budget, industry, broker, firm):
	print('___________________________________________________________')
	print("Validating new Client")
	errorMessage = ''
	global tempClient
	budget = re.sub('[,$]', '', budget)
	number = re.sub('-', '', number)

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
		tempClient.ID = username
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
		print('Budget Validation - Error!')
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
		registeredClients.append(tempClient)
		createPopup('validateClient', 'Registration Successful!')
		os.makedirs('SMfiles/users/'+username)
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempClient,f)

		

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
		tempBroker.BrokerEmailAddress = email
	else:
		print('Email Validation - Error!')
		errorMessage += 'Email Address is invalid\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		print('Username Validation - Clear!')
		tempBroker.ID = username
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
		tempBroker.BrokerTotalBudget = budget
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
		os.makedirs('SMfiles/users/'+username)
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempBroker,f)
		

	print('==========================================================')

def validateBrokerEdit(name, number, email, username, password, password2, budget, industry, license, authority, year):
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
	if  not email == '':
		tempBroker.BrokerEmailAddress = email
		print('Email Validation - Clear!')		
	else:

		print('Email Validation - Error!')
		print(loggedInAccount.BrokerEmailAddress)
		errorMessage += 'Passwords do not match\n'		

	''' 
		VALIDATE password
	'''
	if  password == '' and password2 =='':
		tempBroker.BrokerPassword = loggedInAccount.BrokerPassword
		
	elif password == password2 and not password == '':
		tempBroker.BrokerPassword = password
		print(password)
		print('Password Validation - Clear!')
	else:

		print('Password Validation - Error!')
		errorMessage += 'Passwords do not match\n'		
	
	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		print('Budget Validation - Clear!')
		tempBroker.BrokerTotalBudget = budget
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


	tempBroker.ID = username

	if not errorMessage == '':
		createPopup('validateBroker', errorMessage)
	else:
		createPopup('validateBrokerEdit', 'Information Edit Successful!')
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempBroker,f)
		

	print('==========================================================')


def logout():
	global loggedInAccount
	loggedInAccount = ''
	windowMenus(root)
	createPopup('logout','')
	
def login(username, password):
	print('In Login function')
	print(username)
	print(password)
	
	if not os.path.exists('SMfiles/users/'+username):
		print('user not found')
		createPopup('loginError-user', username)
	else:
		print('User found')
		with open('SMfiles/users/'+username+'/'+username+'.txt','rb') as f:
			tempAccount = pickle.load(f)
		
		if isinstance(tempAccount, Client):
			if password == tempAccount.ClientPassword:
				print('password match -> log in')
				createPopup('login-pass', tempAccount.ClientName)
				global loggedInAccount
				loggedInAccount = tempAccount
			else:
				print('password does not match -> DO NOT log in')
				createPopup('loginError-pass', username)
		elif isinstance(tempAccount, Broker):
			if password == tempAccount.BrokerPassword:
				print('password match -> log in')
				createPopup('login-pass', tempAccount.BrokerName)
				
				global loggedInAccount
				loggedInAccount = tempAccount
			else:
				print('password does not match -> DO NOT log in')
				createPopup('loginError-pass', username)

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
		print('This will get an existing firm')
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
	print('___________________________________________________________')
	print("Validating new Client")
	errorMessage = ''
	global tempClient
	budget = re.sub('[,$]', '', budget)
	number = re.sub('-', '', number)

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
		if tempClient.ClientEmailAddress == email:
			print('Email Validation - NOT CHANGED!')
			
		else:

			print('Email Validation - Clear! CHANGED!!!')
			tempClient.ClientEmailAddress = email
	else:
		print('Email Validation - Error!')
		errorMessage += 'Email Address cannot be left empty\n'

	'''
		VALIDATE username
	'''
	if not username == '':
		print('Username Validation - Clear!')
		tempClient.ID = username
	else:
		print('Username Validation - Error!')
		errorMessage += 'Username is invalid\n'	

	'''
		VALIDATE password
	'''
	if  password == '' and password2 =='':
		tempClient.ClientPassword = loggedInAccount.ClientPassword
		
	elif password == password2 and not password == '':
		tempClient.ClientPassword = password
		print('Password Validation - Clear!')
	else:

		print('Password Validation - Error!')
		errorMessage += 'Passwords do not match\n'		


	'''
		VALIDATE budget
	'''
	try:
		float(budget)
		print('Budget Validation - Clear!')
		tempClient.ClientBudget = budget
	except ValueError:
		print('Budget Validation - Error!')
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
		createPopup('validateClientEdit', errorMessage)
	else:
		createPopup('validateClientEdit', 'Information Edit Successful!')
		strfile = 'SMfiles/users/'+username+'/'+username+'.txt'
		with open(strfile, 'wb') as f:
			pickle.dump(tempClient,f)

		

	print('___________________________________________________________')

def clear(yourwindow):
	for widget in yourwindow.winfo_children():
		widget.destroy()
	windowMenus(yourwindow)
'''
	stock homepage should include:
	welcome message
	nsadaq + nyse + LON index activities
	3 trending stock graphed and projected
	refer to notes in the meeting log

'''

def portfolioWindow():
	'''
		retrieve and list all investments in a user's portfolio
	'''
	clear(root)
	root.geometry("500x500")
	root.wm_title('Stock Market App - Portfolio')

	#Frame(root, height=10, width=10).grid(row = 0, column = 0, )
	frame=Frame(root,width=500,height=500)
	frame.grid(row=0,column=0)
	canvas=Canvas(frame,width=478,height=491)
	'''	
	for x in range(100):
		label = Label(canvas, text='line #'+str(x))
		label.pack()
	'''

	'''
		ID
		TradeDate
		Volume
		pricetraded


	'''
	y = 10
	for x in xrange(1,3):
		
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[STCK #"+str(x)+']')
		line = canvas.create_line(10, y, 490, y)

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Stock:")


		canvas_id = canvas.create_text(50, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[Stock name]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Current Date of info: ")
		

		canvas_id = canvas.create_text(145, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue', text="[the StockDate]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Date Traded: ")

		canvas_id = canvas.create_text(95, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the TradeDate]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Price Traded $: ")

		canvas_id = canvas.create_text(110, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the TradedPrice]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Current Price $: ")

		canvas_id = canvas.create_text(115, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the StockPrice]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Open Price $: ")

		canvas_id = canvas.create_text(100, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the StockOpen]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Day Range: ")

		canvas_id = canvas.create_text(90, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the StockDayRange]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Volume: ")

		canvas_id = canvas.create_text(65, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the StockVolume]")

		y+=20
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Close Price $: ")

		canvas_id = canvas.create_text(100, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='blue',text="[the StockVolume]")
		
		y+=40
		canvas_id = canvas.create_text(10, y, anchor="nw")
		canvas.itemconfig(canvas_id, text="Profit/Loss: ")

		canvas_id = canvas.create_text(85, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='red',text="[Loss]")

		canvas_id = canvas.create_text(120, y, anchor="nw")
		canvas.itemconfig(canvas_id, fill='#006400',text="[Profit]")
		y+=20
		line = canvas.create_line(10, y, 490, y)
		y+=20
	if x*260 <500:

		canvas.config(scrollregion=(0,0,478,0))
		canvas.config(width=478,height=491)
		canvas.pack(side=LEFT,expand=True,fill=BOTH)
	else:
		canvas.config(scrollregion=(0,0,478,x*260))
		vbar=Scrollbar(frame,orient=VERTICAL)
		vbar.pack(side=RIGHT,fill=Y)
		vbar.config(command=canvas.yview)
		canvas.config(width=478,height=491)
		canvas.config( yscrollcommand=vbar.set)
		canvas.pack(side=LEFT,expand=True,fill=BOTH)
	#Label(canvas, text="Rodney Test").grid(row=0, column=0)
	



	'''
	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT, fill=Y)
	
	listbox = Listbox(root)

	listbox.pack()

	for i in range(500):
		listbox.insert(END, i)

# attach listbox to scrollbar
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listbox.yview)
	'''

def home():
	clear(root)
	root.wm_title("Stock Market App - Home")
	root.geometry("500x1000")
	windowMenus(root)
	
	if not loggedInAccount == '' and isinstance(loggedInAccount,Broker) == True:
		print('YOU ARE LOGEED IN BROKER FOOL')	
		Frame(root, height=10, width=10).grid(row=0,column=0)
		Label(root, text="Welcome back our Stock Market App, "+loggedInAccount.BrokerName+".").grid(row=1,column=0, columnspan=4)
		Label(root, text="In this homepage, we are happy to catch you up").grid(row=2,column=0, columnspan=4)
		Label(root, text="as to what happened while you were gone!").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, fg="#006400",text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, fg="#006400",text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, fg ="red" , text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig3 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
		canvas3 = FigureCanvasTkAgg(fig3, master=root)
		
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
		canvas3.get_tk_widget().grid(column=0,row=13, columnspan=4)

		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		ax3 = fig3.add_subplot(111)
		
		xLabel = ''
		yLabel = ''
		zLabel = ''

		xList = []
		yList = []
		zList =[]
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				print('Stock '+key+ ' code is '+ value)
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
		#print(xList)
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				print('Stock '+key+ ' code is '+ value)
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		#print(xList)
		ax2.plot(yList, label=yLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Alphabet Inc.':
				print('Stock '+key+ ' code is '+ value)
				zLabel = value

		zTestList = get_historical(zLabel,1)
		for element in zTestList:
			zList.append(element.StockPrice)
		#print(xList)
		ax3.plot(zList, label=zLabel)

		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		ax3.set_ylabel("Price $")
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		ax3.get_xaxis().set_ticks([])
	
	
		#ax.plot(z, label='COOP')
		#ax.plot(a, label='HOOP')
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
		ax3.legend(prop={'size':12})

	elif not loggedInAccount == '' and isinstance(loggedInAccount,Client) == True:
		print('YOU ARE LOGEED IN Client FOOL')	
		Frame(root, height=10, width=10).grid(row=0,column=0)
		Label(root, text="Welcome back our Stock Market App, "+loggedInAccount.ClientName+".").grid(row=1,column=0, columnspan=4)
		Label(root, text="In this homepage, we are happy to catch you up").grid(row=2,column=0, columnspan=4)
		Label(root, text="as to what happened while you were gone!").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, fg="#006400",text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, fg="#006400",text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, fg ="red" , text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig3 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
		canvas3 = FigureCanvasTkAgg(fig3, master=root)
		
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
		canvas3.get_tk_widget().grid(column=0,row=13, columnspan=4)

		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		ax3 = fig3.add_subplot(111)
		
		xLabel = ''
		yLabel = ''
		zLabel = ''

		xList = []
		yList = []
		zList =[]
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				print('Stock '+key+ ' code is '+ value)
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
		#print(xList)
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				print('Stock '+key+ ' code is '+ value)
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		#print(xList)
		ax2.plot(yList, label=yLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Alphabet Inc.':
				print('Stock '+key+ ' code is '+ value)
				zLabel = value

		zTestList = get_historical(zLabel,1)
		for element in zTestList:
			zList.append(element.StockPrice)
		#print(xList)
		ax3.plot(zList, label=zLabel)

		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		ax3.set_ylabel("Price $")
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		ax3.get_xaxis().set_ticks([])
	
	
		#ax.plot(z, label='COOP')
		#ax.plot(a, label='HOOP')
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
		ax3.legend(prop={'size':12})
	else:
		print('NAWT LOGGED IN FOOL')
		Frame(root, height=10, width=10).grid(row=0,column=0)
		Label(root, text="Welcome to our Stock Market App").grid(row=1,column=0, columnspan=4)
		Label(root, text="Please Login or Register to use the App's full functionality").grid(row=2,column=0, columnspan=4)
		Label(root, text="The following dashboard displays notable changes in the stock market").grid(row=3,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=4,column=0)
		Label(root, text="_________________________ Currently Trending Stocks ________________________").grid(row=5,column=0, columnspan=4)
		Label(root, fg="#006400",text="Netflix, Inc. NFLX").grid(row=6,column=0, columnspan=4)
		Label(root, fg="#006400",text="Tesla Motors Inc TSLA").grid(row=7,column=0, columnspan=4)
		Label(root, fg ="red" , text="Alphabet Inc. GOOG").grid(row=8,column=0, columnspan=4)
		Frame(root, height=10, width=10).grid(row=9,column=0)
		Label(root, text="__________________________ Trending Stocks Graph _________________________").grid(row=10,column=0, columnspan=4)

		fig = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig2 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		fig3 = plt.Figure(facecolor='w', edgecolor='w', figsize=(6,3))
		
		canvas = FigureCanvasTkAgg(fig, master=root)
		canvas2 = FigureCanvasTkAgg(fig2, master=root)
		canvas3 = FigureCanvasTkAgg(fig3, master=root)
		
		canvas.get_tk_widget().grid(column=0,row=11, columnspan=4)
		canvas2.get_tk_widget().grid(column=0,row=12, columnspan=4)
		canvas3.get_tk_widget().grid(column=0,row=13, columnspan=4)

		ax = fig.add_subplot(111)
		ax2 = fig2.add_subplot(111)
		ax3 = fig3.add_subplot(111)
		
		xLabel = ''
		yLabel = ''
		zLabel = ''

		xList = []
		yList = []
		zList =[]
		for key,value in ticker_list.iteritems():
			if key == 'Netflix, Inc.':
				print('Stock '+key+ ' code is '+ value)
				xLabel = value

		xTestList = get_historical(xLabel,1)
		for element in xTestList:
			xList.append(element.StockPrice)
		#print(xList)
		ax.plot(xList, label=xLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Tesla Motors Inc':
				print('Stock '+key+ ' code is '+ value)
				yLabel = value

		yTestList = get_historical(yLabel,1)
		for element in yTestList:
			yList.append(element.StockPrice)
		#print(xList)
		ax2.plot(yList, label=yLabel)

		for key,value in ticker_list.iteritems():
			if key == 'Alphabet Inc.':
				print('Stock '+key+ ' code is '+ value)
				zLabel = value

		zTestList = get_historical(zLabel,1)
		for element in zTestList:
			zList.append(element.StockPrice)
		#print(xList)
		ax3.plot(zList, label=zLabel)

		ax.set_ylabel("Price $")
		ax2.set_ylabel("Price $")
		ax3.set_ylabel("Price $")
		ax.get_xaxis().set_ticks([])
		ax2.get_xaxis().set_ticks([])
		ax3.get_xaxis().set_ticks([])
	
	
		#ax.plot(z, label='COOP')
		#ax.plot(a, label='HOOP')
		ax.legend(prop={'size':12})
		ax2.legend(prop={'size':12})
		ax3.legend(prop={'size':12})	


def compareStocks(stock1,stock2,stock3,duration):
	clear(root)

	root.wm_title("Stock Market App - Stock Comparison")
	root.geometry("654x780")
	
	if stock1 == '':
		print('if')
		stockOption1 = StringVar()
	else:
		print('else '+str(stock1))
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
	
	'''y = numpy.sqrt([81,99,100,29,10,29,19,55,53,4, 9, 100])
	z = [10,23,39,40,29,01,11,16,8,12]
	a = [7,8,9,10,9,8,7,6,5,4,3,2,10]'''
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
		'''
		for quote in quotelist:
			for stockQuote in quote:
				#googleprice.append(thea.StockPrice)
				#print('COMPARISON '+str(stockQuote.StockID)+' at '+str(stockQuote.StockDate)+' is at $'+str(stockQuote.StockPrice))
	
		print(availableStocks)
		'''
	else:
		stockOption1.set(stock1)
		plotTitle += stockOption1.get()+'| '
		
		for key,value in ticker_list.iteritems():
			if key == stockOption1.get():
				print('Stock '+key+ ' code is '+ value)
				xLabel = value

		xTestList = get_historical(xLabel, duration)
		for element in xTestList:
			xList.append(element.StockPrice)
		#print(xList)
		ax.plot(xList, label=xLabel)

		#print(xList)
		#print(testList)


		
		Label(root, fg="blue",text=stockOption1.get()).grid(row=5, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockDate).grid(row=6, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockPrice).grid(row=7, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockOpen).grid(row=8, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockDayRange).grid(row=9, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockVolume).grid(row=10, column=1)
		Label(root, fg="blue",text=xTestList[-1].StockClose).grid(row=11, column=1)
		Label(root, font = "Helvetica 14 bold",fg="blue",text="Buy").grid(row=13, column=1)

	if stock2 == '' or stock2 =='Select Stock':
		stockOption2.set('Select Stock')
	else:
		stockOption2.set(stock2)
		plotTitle += stockOption2.get()+'| '

		for key,value in ticker_list.iteritems():
			if key == stockOption2.get():
				print('Stock '+key+ ' code is '+ value)
				yLabel = value

		yTestList = get_historical(yLabel, duration)
		for element in yTestList:
			yList.append(element.StockPrice)
		#print(yList)
		ax.plot(yList, label=yLabel)

		Label(root, fg="#006400",text=stockOption2.get()).grid(row=5, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockDate).grid(row=6, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockPrice).grid(row=7, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockOpen).grid(row=8, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockDayRange).grid(row=9, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockVolume).grid(row=10, column=2)
		Label(root, fg="#006400",text=yTestList[-1].StockClose).grid(row=11, column=2)
		Label(root, font = "Helvetica 14 bold", fg="#006400",text="Sell").grid(row=13, column=2)

	if stock3 == '' or stock3 =='Select Stock':
		stockOption3.set('Select Stock')
	else:
		stockOption3.set(stock3)
		plotTitle += stockOption3.get()+'| '

		for key,value in ticker_list.iteritems():
			if key == stockOption3.get():
				print('Stock '+key+ ' code is '+ value)
				zLabel = value

		zTestList = get_historical(zLabel, duration)
		for element in zTestList:
			zList.append(element.StockPrice)
		#print(zList)
		ax.plot(zList, label=zLabel)
		Label(root, fg="red",text=stockOption3.get()).grid(row=5, column=3)
		Label(root, fg="red",text=zTestList[-1].StockDate).grid(row=6, column=3)
		Label(root, fg="red",text=zTestList[-1].StockPrice).grid(row=7, column=3)
		Label(root, fg="red",text=zTestList[-1].StockOpen).grid(row=8, column=3)
		Label(root, fg="red",text=zTestList[-1].StockDayRange).grid(row=9, column=3)
		Label(root, fg="red",text=zTestList[-1].StockVolume).grid(row=10, column=3)
		Label(root, fg="red",text=zTestList[-1].StockClose).grid(row=11, column=3)
		Label(root, font = "Helvetica 14 bold",fg="red",text="Hold").grid(row=13, column=3)





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
	#plt.show()


def viewRegisteredFirmsWindow():
	clear(root)
	root.geometry("500x500")
	root.wm_title('Stock Market App - Registered Firms')

	#Frame(root, height=10, width=10).grid(row = 0, column = 0, )
	frame=Frame(root,width=500,height=500)
	frame.grid(row=0,column=0)
	canvas=Canvas(frame,width=478,height=491)
	'''	
	for x in range(100):
		label = Label(canvas, text='line #'+str(x))
		label.pack()
	'''

	'''
		ID
		TradeDate
		Volume
		pricetraded


	'''
	y = 10
	

	if len(registeredFirms) == 0:
		print('this is an error')
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
		#Label(canvas, text="Rodney Test").grid(row=0, column=0)
		



	'''
	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT, fill=Y)
	
	listbox = Listbox(root)

	listbox.pack()

	for i in range(500):
		listbox.insert(END, i)

# attach listbox to scrollbar
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listbox.yview)
	'''


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
	elif popupType=='login-pass':
		print("Welcome back, "+message+'! Proceed to enjoy the full functionality of the app')
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
			#validationPopup.geometry('250x80')
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
			#validationPopup.geometry('250x80')
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
		print("Error! No User records found for "+message)
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
		print("Error! Password for user "+message+' is incorrect!')
		errorPopup = Toplevel(root)
		errorPopup.title("Error")
		#errorPopup.geometry('252x97')
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="Error! Password for user "+message+' is incorrect!').grid(row=1, column=0, sticky=W)
		Button(errorPopup, text="Okay", command= lambda: errorPopup.destroy()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 2)

	elif popupType=='login-pass':
		print("Welcome back, "+message+'! Proceed to enjoy the full functionality of the app')
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
	
	elif popupType=='logout':
		print("You have logged out")
		errorPopup = Toplevel(root)
		errorPopup.title("Logged out")
		errorPopup.transient(root)
		errorPopup.resizable(width=FALSE, height=FALSE)


		Frame(errorPopup, height=10).grid(row=0, column=0)
		Label(errorPopup, text="You have Successfully logged out").grid(row=1, column=0, columnspan = 3)
		Label(errorPopup, text='Come back again soon!').grid(row=2, column=0, columnspan = 3)
		
		Button(errorPopup, text="Okay", command= lambda: home()).grid(row=3, columnspan=3, column=0)
		Frame(errorPopup, height=10, width=10).grid(row=4, column=0, columnspan = 3)


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
	accountMenu.add_command(label="Edit Info",accelerator="cmd-e", command= lambda: editInfo())
	accountMenu.add_command(label="View History", command="")
	accountMenu.add_separator()
	accountMenu.add_command(label="Bleh", command="")


	stocksMenu.add_command(label="View Portfolio", accelerator="cmd-p",command= lambda: portfolioWindow())
	stocksMenu.add_separator()
	stocksMenu.add_command(label="View Stock Market", accelerator="cmd-v", command="")
	stocksMenu.add_command(label="Compare Stocks", accelerator="cmd-c", command=lambda: compareStocks('','','',''))
	stocksMenu.add_separator()
	stocksMenu.add_command(label="Sell", accelerator="cmd-s",command="")
	stocksMenu.add_command(label="Buy", accelerator="cmd-b",command="")
	stocksMenu.add_command(label="Trade", accelerator="cmd-t",command="")

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
	root.bind('<Command-p>', lambda e: portfolioWindow()) 

	if not loggedInAccount == '':
		'''
		if logged in enable additional hotkeys and menu options
		'''
		
		root.bind('<Command-e>', lambda e: editInfo()) 
		root.bind('<Command-l>', lambda e: logout())

		accountMenu.entryconfig("Login", label="Log Out", command=lambda: logout())
		stocksMenu.entryconfig("Sell", state="normal")
		stocksMenu.entryconfig("Buy", state="normal")
		stocksMenu.entryconfig("Trade", state="normal")
		stocksMenu.entryconfig("Sell", state="normal")
		stocksMenu.entryconfig("View Portfolio", state="normal")

		accountMenu.entryconfig("Edit Info", state="normal")
		accountMenu.entryconfig("View History", state="normal")

	
	else:
		'''
		if NOT logged in disable additional hotkeys and menu options
		'''
		stocksMenu.entryconfig("Sell", state="disabled")
		stocksMenu.entryconfig("Buy", state="disabled")
		stocksMenu.entryconfig("Trade", state="disabled")
		stocksMenu.entryconfig("Sell", state="disabled")
		stocksMenu.entryconfig("View Portfolio", state="disabled")

		root.bind('<Command-l>', lambda e: createPopup('login', ''))
		#root.bind('<Command-p>',"") 
		root.bind('<Command-e>',"") 

		accountMenu.entryconfig("Edit Info", state="disabled")
		accountMenu.entryconfig("View History", state="disabled")




def editInfo():
	global loggedInAccount
	if isinstance(loggedInAccount, Client) == True:
		username = loggedInAccount.ID
		print(loggedInAccount.ID)
		f = open('SMfiles/users/'+username+'/'+username+'.txt','rb')
		loggedInAccount = pickle.load(f)
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
		
		#Frame(root, height=10).grid(row=15, column=0)
		# def register(name, number, email, username, password, budget, industry):
		Button(root, text="Cancel", command=lambda: editInfo()).grid(row=16, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: 
			validateClientEdit(nameVar.get(), numberVar.get(), emailVar.get(), userVar.get(), passVar1.get(),passVar2.get(), budgetVar.get(), industryVar.get(), brokerVar.get(), firmVar.get())).grid(row=16, column=1, sticky=E)		
	elif isinstance(loggedInAccount, Broker) == True:
		print('This will edit a Broker')
		username = loggedInAccount.ID
		f = open('SMfiles/users/'+username+'/'+username+'.txt','rb')
		loggedInAccount = pickle.load(f)
		
		
		clear(root)
		root.wm_title("Stock Market App - Edit Broker Information")
		root.geometry("500x500")
		
		Frame(root, height=10).grid(row=0, column=0)
		budget = float(loggedInAccount.BrokerTotalBudget)
		budget = format(float(budget), ",.2f")
		
		#Frame(root, height=10).grid(row=2, column=0)
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
				
		Frame(root, height=10).grid(row=17, column=0)
		licenseVar.set(loggedInAccount.BrokerLicenseType)
		budgetVar.set(str('$'+budget))
		yearVar.set(loggedInAccount.BrokerLicenseIssue)
		
		Button(root, text="Clear", command=lambda: editInfo()).grid(row=18, column=1, sticky=W)		
		Button(root, text="Submit", command=lambda: validateBrokerEdit(nameVar.get(), numberVar.get(), emailVar.get(), loggedInAccount.ID, passVar1.get(), passVar2.get(), budgetVar.get(), industryVar.get(), licenseVar.get(), authorityVar.get(), yearVar.get())).grid(row=18, column=1, sticky=E)		


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
	
	else:
		'''
			populate firm list from registered firms
		'''
		directory = os.listdir('SMfiles/firms')
		
		if directory[0] == '.DS_Store':
			del directory[0]
		print(directory)
		for element in directory:
			with open('SMfiles/firms/'+element+'/'+element+'.txt','rb') as f:
				tempFirm = pickle.load(f)
				print('Firm Name '+tempFirm.FirmName+'\n'+'Firm ID '+ tempFirm.ID +'\n'+'Firm Budget '+tempFirm.FirmBudget+'\n'+'Firm Code: '+tempFirm.FirmCode+'\n')
				registeredFirms.append(tempFirm)

			tempFirm = Firm()

		'''
			populate users list from registered users
		'''
		directory = os.listdir('SMfiles/users')
		
		if directory[0] == '.DS_Store':
			del directory[0]
		print(directory)
		for element in directory:
			with open('SMfiles/users/'+element+'/'+element+'.txt','rb') as f:
				temp = pickle.load(f)
				if isinstance(temp, Client):
					#print(temp.ID +' is a Client')
					registeredClients.append(temp)
					registeredUsers.append(temp)
					#print('registeredClients '+ temp.ClientName)
				elif isinstance(temp, Broker):
					#print(temp.ID +' is a Broker')
					registeredBrokers.append(temp)
					registeredUsers.append(temp)
					#print('registeredBrokers '+ temp.BrokerName)


	'''
		test main from main.py
	'''
	global symblist
	symblist = {'GOOG' : 'Alphabet Inc.', 'AAPL' : 'Apple Inc.', 'NFLX' : 'Netflix, Inc.', 'AMZN' : 'Amazon.com, Inc.', 'TSLA' : 'Tesla Motors Inc', 'JNJ':'Johnson & Johnson', 'LNKD': 'LinkedIn Corp', 'FB': 'Facebook Inc', 'TWTR':'Twitter Inc', 'AIZ':'Assurant Inc.','ISRG':'Intuitive Surgical Inc.'}
	#symblist = {'GOOG' : 'Alphabet Inc.'}
	global ticker_list
	ticker_list = {'Alphabet Inc.' : 'GOOG', 'Apple Inc.' : 'AAPL', 'Netflix, Inc.' : 'NFLX', 'Amazon.com, Inc.' : 'AMZN', 'Tesla Motors Inc' : 'TSLA','Johnson & Johnson':'JNJ', 'LinkedIn Corp':'LNKD', 'Facebook Inc':'FB', 'Twitter Inc':'TWTR', 'Assurant Inc.':'AIZ','Intuitive Surgical Inc.':'ISRG'}
	#ticker_list = {'Alphabet Inc.' : 'GOOG'}
	# read from stock list file
	# stock_list = pickle.load(open('stocklist.p', 'rb'))

	#histo = get_historical('GOOG', 30)
	#for s in histo:
	#    s.print_hist_stock()

	#Get all the closing prices
	close_prices_list = close_prices(symblist)
	#print close_prices_list

	# get historical data on all stocks indicated in symbol list
	availableStocks.append('Select Stock')
	print('-----------------------------------------------------')
	print('Getting historical')
	for key,value in symblist.iteritems():
		availableStocks.append(value)
		quotelist.append(get_historical(key, 1))
	print('-----------------------------------------------------')
	'''
	for quote in quotelist:
		for stockQuote in quote:
			#googleprice.append(thea.StockPrice)
			#print('Stock '+str(stockQuote.StockID)+' at '+str(stockQuote.StockDate)+' is at $'+str(stockQuote.StockPrice))
	'''

	print(availableStocks)


	if not os.listdir('SMfiles/notifications'): 
		print "Notifications Empty"
	else:
		createPopup('notification',root)

	root.mainloop()
if __name__ == "__main__":
	main()
