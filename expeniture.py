class expenditure():
    #salary=int(input("ENTER THE SALARY\n"))
    
    def __init__(self,salary,rent,food,grocery,shopping,misc,travelling,internet,recharge) :
        self.salary=salary
        self.rent=rent
        self.food=food
        self.grocery=grocery
        self.shopping=shopping
        self.misc=misc
        self.travelling=travelling
        self.internet=internet
        self.recharge=recharge
        self.saved=0
        self.percent_sav=0

    def get_self_value(self):
        self.rent=int(input("enter the rent\n"))
        self.food=int(input("enter the food expense\n"))
        self.grocery=int(input("enter the grocery expense\n"))
        self.misc=int(input("enter the misc expense\n"))
        self.travelling=int(input("enter the expense on travelling\n"))
        self.internet=int(input("enter the expense on internet\n"))
        self.recharge=int(input("enter the expense on recharge\n"))
    
    def savings( self):
        self.salary=int(input("enter your monthly salary\n"))
        self.saved=self.salary-(self.food+self.rent+self.grocery+self.shopping+self.misc+self.travelling+self.internet+self.recharge)
        print("Amount saved this month is Rs.",self.saved)

    def percent_save(self):
        self.percent_sav=((self.saved/self.salary)*100)
        print(" Percentage savings is ",self.percent_sav)

suman=expenditure(2883,3383,3833,8484,3848,8484,8484,8484,8484)
suman.get_self_value()
suman.savings()
suman.percent_save()