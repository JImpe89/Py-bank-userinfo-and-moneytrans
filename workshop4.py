# Task 1
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# Task 2
    def change_name(self):
        self.name = str(input("Enter to change name: "))
        print("Name has been change", self.name)

    def change_pin(self):
        self.pin = int(input("Enter to change pin: "))
        print("Pin has been change to: ", self.pin)

    def change_password(self):
        self.password = str(input("Enter to change password: "))
        print("Password Change")

# Task3


class BankUser(User):
    def __init__(self, name, pin, password):
        super(BankUser, self).__init__(name, pin, password)
        self.balance = 0
# Task 4

    def show_balance(self):
        print(self.name, "has an account balance of: ", self.balance)

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdraw):
        self.balance -= withdraw

# Task 5

    def transfer_money(self, other_user, amount_to_transfer):
        print("Transferring $" + str(amount_to_transfer), "to", other_user.name)
        print("Authentication required")
        user_pin = input("Enter pin: ")
        self.balance -= amount_to_transfer
        other_user.balance += amount_to_transfer
        if user_pin == str(self.pin):
            print("Authentication successfull!", amount_to_transfer)
            return True
        elif user_pin != self.pin:
            print("PIN does not match, Transaction Canceled")
            return False

    def request_money(self, other_user, requested_money):
        print("Request to Tranfer Money $", str(
            requested_money), "from", other_user.name)
        print("User authentication required.")
        check_other_user = input("Enter" + other_user.name + "PIN: ")
        if check_other_user == str(other_user.pin):
            check_self = input("Enter your password: ")
        else:
            print("Invalid PIN. Exit Transaction..")
            return False
        if check_self == self.password:
            print("Requested Money Authorize")
            print(other_user.name, "sent", "$" + str(requested_money))
            self.balance += requested_money
            other_user.balance -= requested_money
            return True
        else:
            print("Invald Password. Exit Transaction..")
            return False


# """Driver code for task 1 """
# user_details=User("Bob", 1234, "password")
# print(user_details.name, user_details.pin, user_details.password)
# """Driver code for task 2 """
# user_details=User("Bob", 1234, "password")
# user_details.change_name()
# user_details.change_pin()
# user_details.change_password()
# """"Driver code for task 3 """"
# user_details=BankUser("Bob", 1234, "password")
# print(user_details.name, user_details.pin,
#      user_details.password, user_details.balance)
# """"Driver code for task 4 """"
# user_details = BankUser("Bob", 1234, "password")
# user_details.show_balance()
# user_details.deposit(1000)
# user_details.show_balance()
# user_details.withdraw(500)
# user_details.show_balance()
# """"Driver code for task 5 """"
user_details = BankUser("Bob", 1234, "password")
user_details2 = BankUser("Bobby", 4321, "pass")
user_details2.deposit(1000)
user_details2.show_balance()
user_details.show_balance()
user_details2.transfer_money(user_details, 500)
user_details2.show_balance()
user_details.show_balance()
user_details2.request_money(user_details, 200)
user_details2.show_balance()
user_details.show_balance()
