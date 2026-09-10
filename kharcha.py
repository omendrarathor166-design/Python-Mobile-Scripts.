print("💸 Mera Daily Expense Tracker 💸")

# 1. User se input lete hain
item_name = input("Aaj aapne kya kharida?: ")
item_cost = input("Kitne rupey kharch hue?: ")

# 2. Ek Dictionary banate hain data ko format karne ke liye
expense_dict = {"item": item_name, "cost": item_cost}

# 3. File Handling: Data ko .txt file mein save karna
# Blank 1: File ko "append" mode mein open karne ke liye 'a', 'w', ya 'r' mein se kya aayega?
my_file = open("kharche.txt", "a")

# Data ko file mein likhte hain
line_to_save = f"Kharcha: {expense_dict['item']} - Rs {expense_dict['cost']}\n"

# Blank 2: File mein data 'likhne' ke liye kaunsa command use hota hai? (hint: read ka ulta)
my_file.write(line_to_save)

# File ko close karna bohot zaroori hota hai
my_file.close()

print(f"Done! Aapka '{item_name}' ka kharcha save ho gaya hai.")
