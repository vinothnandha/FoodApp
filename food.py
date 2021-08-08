import csv
import admin
class Food():
    def __init__(self):
        self.list_of_food = []
        with open("food_list.csv",'r', newline="") as fb:
            read = csv.reader(fb)
            for row in read:
                self.list_of_food.append(row)
            #print(self.list_of_food)
    def add_food(self):
        Food_ID = int(self.list_of_food[len(self.list_of_food)-1][0])
        while True:
            try:
                Food_ID +=1
                food_name = input("Enter a Food Name:")
                qty = input("Enter a Qty:")
                price = input("Enter a Price:")
                discount = input("Enter Discount:")
                self.list_of_food.append([Food_ID,food_name.title(),qty,"INR "+price,discount])
                print(self.list_of_food)
                ab = csv.writer(open("food_list.csv",'w', newline=""))
                ab.writerows(self.list_of_food)
                print("Successfully Added Food Item...!!!")
                return False
            except:
                print("Enter a Valid Input...!!!!")

    def edit_food(self):
        while True:
            try:
                n = int(input("Enter a FoodID You Want To Edit:"))
                a = 0
                for i in self.list_of_food:
                    if int(i[0]) == n:
                        a = 1
                        print("FoodID:{0} \nFood Name:{1} \nFood Qty:{2} \nFood Price:{3} \nFood Discount:{4}".format(i[0],i[1],i[2],i[3],i[4]))
                        show = int(input("Press 1 To Edit Food Name \nPress 2 To Edit Food Qty \nPress 3 To Edit Price \nPress 4 To Edit Discount"))
                        if show == 1:
                            food_name = input("Enter a Food Name:")
                            i[1] = food_name
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 2:
                            qty = input("Enter a Qty:")
                            i[2] = qty
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 3:
                            price = input("Enter a Price:")
                            i[3] = "INR "+price
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 4:
                            discount = input("Enter Discount:")
                            i[4] = discount
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 0:
                            print("Quited....!!!!")
                            return False
                        else:
                            print("Enter a Number within a given option...!!!")
                if a == 0:
                    print(n,"-Food Id is Not Available")
                else:        
                    ab = csv.writer(open("food_list.csv",'w', newline=""))
                    ab.writerows(self.list_of_food)
                    return False
            except:
                print("Invalid Input..!!!")

    def view_food(self):
        with open("food_list.csv",'r', newline="") as fb:
            read = csv.reader(fb)
            print("List Of Food Items....!!!")
            first = 1
            for row in read:
                if first:
                    first = 0
                    print("FoodID".center(10),"Food Name".center(30),"Food Qty".center(25),"Food Price".center(20),"Food Discount".center(20), end="\n")
                print(row[0].center(10),row[1].center(30),row[2].center(25),row[3].center(20),row[4].center(20), end="\n")
                #print("FoodID:{0} \nFood Name:{1} \nFood Qty:{2} \nFood Price:{3} \nFood Discount:{4}".format(row[0],row[1],row[2],row[3],row[4]))

    def remove_food(self):
        while True:
            try:
                n = int(input("Enter a FoodID You Want To Remove:"))
                a = 0
                for i in self.list_of_food:
                    if int(i[0]) == n:
                        a = 1
                        self.list_of_food.remove(i)
                        print("Successfully Removed....!!!!")
                        break
                if a==0:
                    print("FoodID Not Available...!!!")
                else:        
                    ab = csv.writer(open("food_list.csv",'w', newline=""))
                    ab.writerows(self.list_of_food)
                    return False
            except:
                print("Invalid Input")

    def menu(self):
        flag = True
        while flag:
            try:
                self.choice = int(input("\nPress 1 To Add Food \nPress 2 To Edit Food Items \nPress 3 To Remova a Food Item \nPress 4 To View List of Food Items \nPress 5 To Create a Admin \nPress 0 To Exit"))
                if self.choice == 1:
                    self.add_food()
                elif self.choice == 2:
                    self.edit_food()
                elif self.choice == 3:
                    self.remove_food()
                elif self.choice == 4:
                    self.view_food()
                elif self.choice == 5:
                    a = admin.admin()
                    a.create_admin()
                elif self.choice == 0:
                    flag = False
                else:
                    print("Not Valid Choice, Try Again....!!!!")
            except:
                print("Invalid Input------!!!")

