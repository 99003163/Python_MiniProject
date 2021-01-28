class shop:
    def __init__(self,name=0,age=0,mobilenumber=0):
        self.name=name
        self.age=age
        self.mobilenumber=mobilenumber
    def person(self):
        print("enter name",end='')
        self.name=input()
        print("enter age",end='')
        self.age=input()
        print("enter mobilenumber",end='')
        self.mobilenumber=input()
        bill = open("bill.txt", "a")
        bill.write(str(self.name))
        bill.close()
       

class menshopping(shop):
    def shirt(self):
        print("Enter the Quantity")
        self.quantity = int(input())
        self.cost = self.quantity*500
        print("The  cost for shirt is: ", self.cost)
        return self.cost

    def pant(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*300
        print("The  cost for pant is:", cost)
        return cost

    def jacket(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*400
        print("The  cost for jacket is:", cost)
        return cost

    def spectacles(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*150
        print("The cost for spectacles is:", cost)
        return cost

    def watch(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*120
        print("The cost for watch is:", cost)
        return cost

    def shoe(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*300
        print("The cost for watch is:", cost)
        return cost

    def sliders(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*350
        print("The cost for sliders is:", cost)
        return cost

    def bag(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*250
        print("The cost for bag is:", cost)
        return cost

    def belt(self):
        print("Enter the Quantity")
        quantity = int(input())
        cost = quantity*200
        print("The cost for belt is:", cost)
        return cost


object3 = shop()
object3.person()  

class choice(menshopping):
    def __init__(self):
        self.choice=0
        self.price=0
    def select(self):
        print("1.shirt")
        print("2.pant")
        print("3.jacket")
        print("4.spectacles")
        print("5.watch")
        print("6.shoe")
        print("7.sliders")
        print("8.bag")
        print("9.belt")
        while True:
            print("select other than 1 to 9 to get total price")
            choice = int(input("select the item:"))
            if (choice == 1):
                self.price += object1.shirt()
            elif (choice == 2):
                self.price += object1.pant()
            elif (choice == 3):
                self.price += object1.jacket()
            elif (choice == 4):
                self.price += object1.spectacles()
            elif (choice == 5):
                self.price += object1.watch()
            elif (choice == 6):
                self.price += object1.shoe()
            elif (choice == 7):
                self.price += object1.sliders()
            elif (choice == 8):
                self.price += object1.bag()
            elif (choice == 9):
                self.price += object1.belt()
            else:
                break
        print("The total cost is :",self.price)
        if(self.price > 0):
            if self.price <= 500:
                discount = self.price*0.05
            elif self.price > 500 and self.price < 1500:
                discount = self.price*0.12
            else:
                discount = self.price*0.3
            print("discount is", discount)
            cash_to_be_paid = self.price-discount
            print("cash to be paid is", cash_to_be_paid)
            bill = open("bill.txt", "a")
            bill.write(str(cash_to_be_paid))
            print("please select the payment method")
            print("1-google pay\n2-phonepay\n3-paytm")
            choice_pay = int(input("select the item:"))
            if (choice_pay == 1):
                print("process payment through google pay")
            elif (choice_pay == 2):
                print("process payment through phone pay")
            elif (choice == 3):
                print("process payment through paytm")
            else:
                print("process payment through cash")
            bill.close()
            print("Thank you")
            print("please visit again")
             

print("shirt 500/- per quantity")
print("pant 300/- per quantity")
print("jacket 400/- per quantity")
print("spectacles 150/- per quantity")
print("watch 120/- per quantity")
print("shoe 300/- per quantity")
print("sliders 350/- per quantity")
print("bag 250/- per quantity")
print("beltt 200/- per quantity")
print("Please select")
object1 = menshopping()
obj=choice()
obj.select()
