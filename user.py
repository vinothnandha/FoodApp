from datetime import date
import csv
import food
class User():

    def __init__(self,mail=''):
        self.email_id = mail
        self.user = []
        self.order_list = []
        self.ac = 0
        self.tmp = []
        



        with open("user_list.csv",'r', newline="") as us:
            re = csv.reader(us)
            for row in re:
                self.user.append(row)
        with open("food_list.csv",'r', newline="") as fb:
            read = csv.reader(fb)
            for row in read:
                self.order_list.append(row)

    def register(self):
        print('Register page'.center(10,'~'))
        while True:
            try:
                full_name = input("Enter a Full Name:")
                ph_no = self.ph_no()                     
                email_id = self.check_email()
                address = input("Enter a Address:")
                password = input("Enter a Password:")
                self.user.append([full_name.title(),ph_no,email_id,address,password])
                ab = csv.writer(open("user_list.csv",'w',newline=""))
                ab.writerows(self.user)
                print("Resgister Successfully...!!!")
                
                #print(self.user)
                return False
            except:
                print("Invalid Input")

    def ph_no(self):
        flag = True
        while flag:
            try:
                ph_no = input("Enter a Phone Number:")
                if ph_no.isdigit() and len(ph_no)==10:
                    if self.user:
                        for i in self.user:
                            if i:
                                if i[1] == ph_no:
                                    print("Entered Phone Number Already Present")
                                    break
                        else:
                            return ph_no
                            flag = False
                    else:
                        return ph_no
                        flag = False
                else:
                    print("Enter in a digit format... \nOnly 10 Number are allowed...")
            except:
                print("Invalid Input.....")
            

    def check_email(self):
        while True:
            email_id = input("Enter a Email_ID:")
            try:
                if self.user:
                    for i in self.user:
                        if i:
                            if i[2] == email_id:
                                print("Email ID is Already Available...!!!")
                                break
                    else:
                        return email_id
                        break
                else:
                    return email_id
                    break
            except:
                print("Invalid Input...!!!!")

    def update_profile(self):
        while True:
            try:
                email_id = self.email_id
                a = 0
                for i in self.user:
                    if i:
                        if i[2] == email_id:
                            a = 1
                            show = int(input("Press 1 To Edit Full Name \nPress 2 To Edit Phone Number \nPress 3 To Edit Address \nPress 4 To Edit Password \nPress 0 To Quit or Canacel"))
                            if show == 1:
                                full_name = input("Enter a Full Name:")
                                i[0] = full_name
                                print("Successfully Updated....!!!!")
                                break
                            elif show == 2:
                                ph_noo = self.ph_no()
                                i[1] = ph_noo
                                print("Successfully Updated....!!!!")
                                break
                            elif show == 3:
                                address = input("Enter a Address:")
                                i[3] = address
                                print("Successfully Updated....!!!!")
                                break
                            elif show == 4:
                                password = input("Enter a Password:")
                                i[4] = password
                                print("Successfully Updated....!!!!")
                                break
                            elif show == 0:
                                print("Quited....!!!!")
                                return False
                            else:
                                print("Enter a Number within a given option...!!!")
                if a == 0:
                    print(email_id,"-Email Id is Not Available")
                else:
                    ab = csv.writer(open("user_list.csv",'w', newline=""))
                    ab.writerows(self.user)
                    return False
            except:
                print("Invalid Input..!!!")

    def show_items(self):
        a = food.Food()
        a.view_food()

    def order_history(self):

            if not self.ac:
                print('No curren orders')
                ck = 0
                abc = csv.reader(open('order_list.csv','r'))
                for r in abc:
                    if r:
                        ck = 1
                        print(r)
                if not ck:
                    print('No order history')
                return True
            elif self.ac:
                print("Order History Of:", self.email_id)
                f_id = ''
                ff_id = []
                now_date = date.today()
                for a in self.tmp:
                    #print(a)
                    for e in a:
                        f_id += str(e[0])
                        f_id += '~'
                        break
                self.tmp = ''
                ff_id.append(str(f_id+'@'+str(now_date)))
                rac = ''.join(ff_id)
                ak ,ap = [] , 0
                ag = csv.reader(open('order_list.csv','r'))
                
                for row in ag:
                    if row:
                        if row[0]==self.email_id:
                            
                            row.append(str(rac))
                            ak.append(row)
                            ap = 1

                if ap==0:
                    ak.append(self.email_id)
                    ak.append(str(rac))
             
                done = csv.writer(open('order_list.csv','w',newline=''))
                done.writerows(ak)

    def place_order(self):
        self.show_items()
        now = []
        while True:
            try:
                n = list(map(int,input("Enter Food Id Separate by Comma:").split(',')))
                for j in n:
                    for i in self.order_list:
                        if j == int(i[0]):
                            now.append(i)
                break
            except:
                print("Invalid Order ID..!!!")
        print("Order Placed Successfully...!!!!")
        self.ac=1
        self.tmp = now
        self.order_history()



    def user_menu(self):
        flag = True
        while flag:
            try:
                self.choice = int(input("\nPress 1 To View Food Menu \nPress 2 To Place New Order \nPress 3 To Order History \nPress 4 To Update Profile \nPress 0 To Exit"))
                if self.choice == 1:
                    self.show_items()
                elif self.choice == 2:
                    dee = self.place_order()
                    self.ac = 1 if de else 0
                elif self.choice == 3:
                    self.order_history()
                elif self.choice == 4:
                    self.update_profile()
                elif self.choice == 0:
                    flag = False
                else:
                    print("Not Valid Choice, Try Again....!!!!")
            except:
                print("order Invalid Input------!!!")



    


