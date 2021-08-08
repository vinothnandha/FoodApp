import csv
import food
import user

class Login:
	def __init__(self):
		print("Welcome To Food App".center(50))
		self.admin_details = {}
		self.user_details = {}
		cv = csv.reader(open("admin_list.csv","r",newline="")) 
		for row in cv:
			if row:
				self.admin_details[row[0]] = row[1]
		#print(self.admin_details)
		ad = csv.reader(open("user_list.csv","r",newline=""))
		for row in ad:
			if row:
				self.user_details[row[2]] = row[4]
		#print(self.user_details)

	def logger(self):
		while True:
			try:
				n = int(input("Press 1 Admin \nPress 2 User \nPress c to cancel"))
				if n == 1:
					self.admin_login()
					return False
				elif n == 2:
					self.user_login()
					return False
				elif n.lower() == "c":
					return False
				else:
					Print("Enter a Withing a Given Option, Try Again...!!!!")
			except:
				print("enter a Valid Input")

	def admin_login(self):
		while True:
			try:
				print("Welcome Admin".center(50))
				v = int(input("Press 1 To Admin Login... \nPress 0 To Exit..."))
				if v == 1:
					admin_id = input("Enter a Admin ID:")
					passw = input("Enter a Password:")
					check = False
					for key,value in self.admin_details.items():
						if key == admin_id and value == passw:
							check = True
							break
					else:
						print("Either Admin Id Or Password Wrong...!!!!")
					if check == True:
						print(admin_id,"Login Successfully...!!!!")
						food_obj = food.Food()
						food_obj.menu()
						return False
				elif v == 0:
					print("Thank You")
					return False
			except:
				print("Invalid Input....!!!")


	def user_login(self):
		while True:
			try:
				print("Welcome User".center(50))
				d = int(input("Press 1 To User Login... \nPress 2 To Register \nPress 0 To Exit..."))
				if d == 1:
					email_id = input("Enter a Email Id:")
					password = input("Enter a Password:")
					check = False
					for key,value in self.user_details.items():
						if key == email_id and value == password:
							check = True
							break
					else:
						print("Either Email ID or Password Wrong....!!!")
					if check == True:
						print(email_id,"Login Successfully....!!!!")
						us = user.User(email_id)
						us.user_menu()
						return False
				elif d == 2:
					df = user.User()
					df.register()
				elif d == 0:
					print("Thank You")
					return False
			except:
				print("login Invalid Input....!!!!")



obj = Login()
obj.logger()