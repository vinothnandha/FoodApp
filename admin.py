import csv
class admin:
    def __init__(self):
        self.admin = []
        with open("admin_list.csv",'r', newline="") as us:
            re = csv.reader(us)
            for row in re:
                self.admin.append(row)
            print(self.admin)

    def create_admin(self):
        while True:
            admin_id = input("Enter a Admin ID:")
            password = input("Enter a Password:")
            try:
                if self.admin:
                    for i in self.admin:
                        if i:
                            if i[0] == admin_id:
                                print("Admin Id Already Present...!!!")
                                break
                    else:
                        self.admin.append([admin_id,password])
                        ab = csv.writer(open("admin_list.csv",'w', newline=""))
                        ab.writerows(self.admin)
                        print("Admin Created Successfully...!!!")
                        return False
            except:
                print("Invalid Input...!!!")




