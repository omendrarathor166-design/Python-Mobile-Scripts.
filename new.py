class Student:
    def __init__(self, student_name, target_exam):
        self.name = student_name
        self.exam = target_exam

    def give_mock_test(self):
        print(f"{self.name} is giving a full mock test for {self.exam} today!")

my_profile = Student("Prashant", "SSC CHSL")

print(f"Candidate Profile: {my_profile.name}")
my_profile.give_mock_test()

class BankAccount:
    def __init__(self, owner_name, starting_balance):
        self.name = owner_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Rs {amount} deposited. New balance is Rs {self.balance}")

my_account = BankAccount("Prashant", 1000)

print(f"Account Owner: {my_account.name}")

my_account.deposit(500)

class Car:
    # 1. Clerk ko variables dijiye
    def __init__(self, brand_name, car_color):
        self.brand = brand_name
        self.color = car_color

    # 2. Action banaiye
    def start_engine(self):
        print(f"Vroom! The {self.color} {self.brand} is starting.")

    # 3. Object banaiye
my_car = Car("Tata", "Black")

# 4. Action ko call kijiye
my_car.start_engine()