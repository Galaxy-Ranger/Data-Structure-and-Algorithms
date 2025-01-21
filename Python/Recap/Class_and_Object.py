L = [1,2,3,4,5]

# Difference between Function and Methods

# Function - A function is a set of instructions that perform a task
len(L)

# Method - A method is a set of instructions that are associated with an object. Inshort, Function inside class is called methods.
L.append(6)


# Learning Classes and Object through ATM Question.
# Q. We need to create an ATM class which has some variables, also some function to perform some fucntionality.
class ATM:
    account_type = str() # class attribute - A class attribute shared by all instances(objects) of the class.
    pin = int()
    balance = int()
    def __init__(self, account_type):  # Initializes the account_type, pin and balance attributes when a new object is created.
        self.account_type = account_type  # Instance Attribute
        self.pin = int
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = 0
        while(user_input != 5):
            user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
    """)
            try:
                user_input = int(user_input)
            except ValueError:
                print("Invalid input, please enter a number.")
                return 
            if(user_input == 1):
                self.pin = int(input("Enter New Your Pin: "))
                print("Your New Pin is created...")
            elif(user_input == 2):
                self.balance = int(input("Enter the deposit amount: "))
                print("Amount Deposited...")
            elif(user_input == 3):
                self.withdrawal(int(input("Enter Your withdrawal amount: ")))
            elif(user_input == 4):
                self.check_balance()
    def withdrawal(self, wAmt):
        if(self.balance > wAmt):
            self.balance = self.balance - wAmt
            print("Withdrawal Successfull...")
            print(f"Your Current Balance is: {self.balance}")
        else:
            print(f"Your Current Balance is low!!")
    def check_balance(self):
        print(f"Your Current Balance is: {self.balance}")

# Creating an object of the ATM class
user1 = ATM("Saving")
# user1.check_balance()
# user1.withdrawal(5000)

# Key Point to Know
# Self Parameter - is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
# __init__ - is same as Java Constructor. (It is a special function and run automatically when an object is created.)