# 1. Mathematical Functions banate hain
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y # Blank 1: Yahan x aur y ko multiply karne ka code likhiye

def divide(x, y):
    if y == 0:
        return "Error! 0 se divide nahi kar sakte."
    return x / y

# 2. User ko menu dikhate hain
print("🧮 Mera Pehla Calculator 🧮")
print("1. Jodna (+)")
print("2. Ghatana (-)")
print("3. Guna karna (*)")
print("4. Bhaag dena (/)")

# 3. User se input lete hain
choice = input("Apna operation chuniye (1, 2, 3, ya 4): ")

num1 = float(input("Pehla number daliye: "))
num2 = float(input("Dusra number daliye: "))

# 4. Conditionals (Faisla karna)
if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':  # Blank 2: Guna (Multiply) karne ke liye user kya number dabayega?
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Galat choice! Kripya 1, 2, 3 ya 4 chuniye.")
