from datetime import date
import csv
import food
class User:

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
            except ValueError:
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
                            flag = False
                            return ph_no

                    else:
                        flag = False
                        return ph_no

                else:
                    print("Enter in a digit format... \nOnly 10 Number are allowed...")
            except TypeError:
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

                else:
                    return email_id

            except ValueError:
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
            except ValueError:
                print("Invalid Input..!!!")

    def what(self,iid):
        ab = csv.reader(open('food_list.csv','r'))
        nme = []
        for row in ab:
            if row:
                if str(row[0]).lower()==iid.lower():
                    nme.append(str(row[1]))
                    p = row[3].split(' ')
                    nme.append(p[1])
        #print(''.join(nme))
        return str(('    '.center(15)).join(nme))


    def order_history(self):
        print('-'*60)
        print("Food Order History !".center(60))
        print('-'*60)
        fl = False
        fst = 1
        ak = csv.reader(open('order_list.csv','r'))
        for row in ak:
            if row:
                if row[0]==self.email_id:
                    fl = True
                    c = row[1:]
                    for e in c:
                        p = 0
                        nw = e.split('@')
                        datee = nw[1]
                        ites = nw[0].split('~')
                        print("On ",datee,"You have tasted...")
                        for f in ites:
                            if f:
                                a = self.what(f)
                                print("      --> ",f,a,sep='   ')
                                aspp = a.split(' ')
                                p+=int(aspp[-1])
                        print("        Total Bil --> ".center(40),p) if p>0 else ''


        if not fl:
            print('No past order history!!..Order food')

        return True



    def idc(self,ao):
        now = str(date.today())
        oid = []
        for e in ao:
            if e:
                oid.append(str(e[0]+'~'))
        oid.append(str('@'+now))
        #print("final oid",''.join(oid))
        return str(''.join(oid))


    def write(self):
        ae = self.tmp
        ap = True
        ooid = self.idc(ae)
        ab = []
        ak = csv.reader(open('order_list.csv','r'))
        for row in ak:
            if row:
                if row[0]==self.email_id:
                    ap = False
                    #self.order_history()
                    row.append(ooid)
                    ab.append(row)
                else:
                    ab.append(row)

        if ap:
            ab = [[self.email_id , ooid]]

        final = csv.writer(open('order_list.csv','w',newline=''))
        #print(final,"writing/...")
        final.writerows(ab)

        self.tmp=[]



    def place_order(self):
        a = food.Food()
        a.view_food()
        now = []
        while True:
            try:
                n = list(map(int,input("Enter Food Id Separate by Comma:").split(',')))
                for j in n:
                    for i in self.order_list:
                        if j == int(i[0]):
                            now.append(i)
                break
            except TypeError:
                print("Invalid Order ID..!!!")

        print("Order Placed Successfully...!!!!")
        self.ac=1
        self.tmp=[]
        self.tmp = now
        self.write()
        self.tmp = []

    def user_menu(self):
        flag = True
        while flag:
            try:
                self.choice = int(input("\nPress 1 To View Food Menu \nPress 2 To Place New Order \nPress 3 To Order History \nPress 4 To Update Profile \nPress 0 To Exit"))
                if self.choice == 1:
                    a = food.Food()
                    a.view_food()
                elif self.choice == 2:
                    dee = self.place_order()
                    self.ac = 1 if dee else 0
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








