# 1 sum
# salary = 50000
# experince =7
#
# if salary < 20000:
#     if experince > 5:
#         bouns = salary * 0.15
#     else :
#         bouns = salary * 0.10
# else:
#      if salary < 50000:
#          bouns = salary * 0.05
#      else :
#          bouns = salary * 0.03
# print("bonus amt is:",bouns)
#
# # 2sum
# units =(int(input("enter units:")))
# if units <= 100:
#     bill = units * 1.5
# else:
#     if units <= 300:
#         bill = units * 2
#     else:
#         if units <= 500:
#             bill = units * 3
#         else:
#             bill = units * 4
# print("bill amt is:",bill)

#3sum
# salary = float(input("enter your salary:"))
# credit_score = float(input("enter credit score:"))
# if salary >= 50000:
#     if credit_score > 750:
#         print("Eligible for Premium Loan")
#     else :
#             print("Eligible for normal Loan")
# else:
#     print("not Eligible")

#4sum
# temp = float(input(""Enter temperature in Celsius: "))
# if temp > 40:
#     print("so hot")
# else:
#     if temp > 30:
#         if temp < 35:
#             print("very hot")
#         else:
#             print("hot")
#
#     else:
#         if temp < 20:
#             print("warm")
#         else:
#             print("cool")

#6sum
# attendance = float(input("Enter attendance percentage: "))
# marks = float(input("Enter marks: "))
# if attendance < 75:
#     print("not eligible for examination")
# else:
#     if marks >= 90:
#         print("Outstanding")
#     else:
#         if marks >= 70:
#             print("Good")
#         else:
#             print("Average")

#7sum
# income = float(input("Enter income: "))
# if income < 250000:
#     tax=0
# else:
#     if income <= 500000:
#         tax = income * 0.05
#     else:
#         if income <= 1000000:
#             if income <= 750000:
#                 tax = income * 0.10
#             else:
#                 tax = income * 0.15
#         else:
#             tax = income * 0.30
#
# print("Tax amount:", tax)


# a = int(input("Enter a number: "))
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# a= int(input("enter a marks:"))
# if a >=90:
#     print("a grade")
# elif a >=70:
#     print("b grade")
# elif a >=60:
#     print("c grade")
# elif a >=40:
#     print("d grade")
# else:
#     print("fail")
#


# b = int(input("enter a age : "))
#
#
# if b>=60:
#     print("old")
# elif b>=40:
#     print("uncle or anuty")
# elif b>=20:
#     print("mid age")
# elif b>=18:
#     print("adult")
# else:
#     print("minnor")

# for i in range(4):
#     print("joshika")
#
# ## start:stop:step: are rules in for i in range
# for i in range (1,11):
#     print(i)
# for i in range (1,6):
#     print(5*i)
#
# # table
# for i in range (1,11):
#     print("5x",i,"=",5*i)

#  list in loop
# numbers = [2, 4, 6, 8]
# for h in numbers:
#     print(h // 2)
#
# numbers = [5, 10, 15]
# for l in numbers:
#     print(l % 4)


# marks = [70, 85, 60, 70,40,90]
# print ("marks" , marks)
# print ("total: ", sum(marks))
# print ("subject",len(marks))
# print ("highest mark", max(marks))
# print ("lowest mark", min(marks))
# print ("average mark", sum(marks)/len(marks))
#
#
# marks = [20, 30, 40]
#
# average = sum(marks) / len(marks)
#
# print(average)
#
# i = 1
# while i <= 10:
#      print("pradeep")
#      i = i + 1




#
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("deposited successfully:",amount)
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("withdrawn successfully:",amount)
#         else:
#             print("Insufficient funds")
#
# obj = BankAccount("Kavi", 100000)
# obj.deposit(50000)
# obj.withdraw(10000)
# print("Current balance:", obj.balance)
#
#



class BankAccount:
    def __init__(self, name, balance,pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin
        self.history = []

    def check_pin(self,pin):
        return self.__pin == pin

    def deposit(self,amount):
        if amount >100000:
            self.__balance += 10000
            self.history.append(f"deposited: {amount}")
            print("deposited successfully:",amount)
        else:
            print("Insufficient funds")

    def withdraw(self,amount,pin):
        if not self.check_pin(pin):
            print("Incorrect pin")
            return
        if amount <= 100000:
            self.__balance -= 10000
            self.history.append(f"withdrawn: {amount}")
            print("withdrawn successfully:",amount)
        else:
                print("Insufficient funds")

    def check_balance(self,pin):
        if self.check_pin(pin):
            print("current balance:",self.__balance)
        else:
            print("incorrect pin")

    def show_history(self,pin):
        if self.check_pin(pin):
            print("\ntransaction history.")
            if not self.history:
                print("no transactions yet.")
            else:
                for h in self.history:
                    print("-",h)
        else:
            print("incorrect pin")
obj = BankAccount("pradeep", 100000,2345)

obj.deposit(100000)
obj.withdraw(10000,2345)
obj.check_balance(2345)
obj.show_history(2345)