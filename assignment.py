# '''
# Task 1: Write Sales Records to a File

# 1. Create a list of sales amounts:
# 2. sales = [1200, 450, 980, 1500, 3000]
# 3. Open a file named sales_data.txt in write mode.
# 4. Write each sale on a new line in the file.
# 5. Close the file, then reopen it and print its contents.

# Extra (optional): Write the data in comma-separated format instead of separate lines.
# '''
sales = [1200, 450, 980, 1500, 3000]

for sale in sales:
    with open('sales_data.txt', 'a') as sale_data:
        sale_data.writelines(f"\n {sale} \n")

with open('sales_data.txt', 'a') as sales_data:
    sales_data.write(', '.join(map(str, sales)))

with open('sales_data.txt', 'r') as sales:
    print(f"{sales.read()}");

# '''
# Task 2: Read File in Different Ways
# Using the same sales_data.txt:
# 1. Read the entire file using read() and print it.
# 2. Read the first line using readline().
# 3. Read all lines using readlines() and convert them into a list of integers.
# Ensure proper formatting and cleanup of newline characters.
# '''

with open("sales_data.txt", "r") as file:
    print(f"\n\n The file data is: {file.read()}")

with open("sales_data.txt", "r") as file:
    print(f"First line {file.readline().strip()}")
    print(f"Second line {file.readline().strip()}")
    print(f"Third line {file.readline().strip()}")

# # def string_to_int(sales):
# #     print(sales)
# #     if ", " in sales:
# #         print(f"sale {list(map(int,sales.split(", ")))}")
# #     else:
# #         sales.strip()
# #     print(f"new sales {sales}")
# #     return sales

with open("sales_data.txt", "r") as file:
    # content = list(map(int, filter(lambda sales: string_to_int(sales), file.readlines())))
    # print(f"All sales from string to integer: {content}")
    sales = []
    for line in file:
        line = line.strip()
        # print(f"line {line}")
        if not line:
            # print(f"not line {line}")
            continue
        if ", " in line:
            sales.extend(map(int, line.split(",")))
        else: 
            sales.append(int(line))
print(sales)
new_sales = [5000, 2500, 1700]
with open("sales_data.txt", "a") as file:
    file.writelines(f"\n {sale}\n" for sale in sales)

with open("sales_data.txt", "r") as file:
    line = file.readlines()
    print(f"Number of line in the sales-data.txt file is: {len(line)}")


# '''
# Task 4: Generate Summary Report from File
# Using only file reading operations:
# 1. Read all sales values from sales_data.txt.
# 2. Convert them into integers.
# 3. Calculate and print:
# • Total Sales
# • Highest Sale
# • Lowest Sale
# • Average Sale
# Do not use any advanced libraries.
# '''

with open('sales_data.txt', 'r') as sales:
    lines = sales.readlines()
    sales = []
    for line in lines:
        line = line.strip()
        print(line)
        if not line:
            continue

        if ", " in line:
            sales.extend(map(int, line.split(',')))
        else: 
            sales.append(int(line))

    print(f"Total Sales: {sum(sales)}")
    print(f"Highest sale: {max(sales)}")
    print(f"Lowest sale: {min(sales)}")
    print(f"Average Sale:{sum(sales)} and {len(sales)} {sum(sales)/len(sales)}")

'''
Task 5: Create Product Info File (User Input)
1. Ask the user for 3 product names & their prices.
2. Write them into a new file products.txt in this format:
3. ProductName | Price
4. Read the file and print each line with proper formatting.
'''

product_list = []

for product in range(0,3):
    try:
        product_name = str(input("Please enter product name? "))
        if product_name.strip() == "":
            print("Please enter the product name not empty...")
            break
        product_price = int(input(f"What is the price of {product_name}? "))
        if product_price <= 0:
            print("Price greater than zero...")
            break
        print(f"{product_name}:{product_price}")
        product_list.append({
            "product_name": product_name,
            "product_price": product_price
        })
    except ValueError as error:
        print(f"Your are facing in this error {error}.")
        break
print(f"Product list => {product_list}")

for product in product_list:
    print(f"{product["product_name"]}: 💲{product["product_price"]}")

with open('products.txt', "a") as file:
    file.write(f"Product Name | Price \n")
    file.writelines(f"{product["product_name"]} : 💲{product["product_price"]} \n" for product in product_list)

'''
Task 6: Read File Safely (Error Handling Inside File Handling Only)
You must not use exceptions beyond file-related safeguards here.
1. Ask the user for a filename to open.
2. If the file exists, read and print it.
3. If it does not exist, print:
"File not found. Please check the filename."
Use simple condition checks with os.path.exists() (allowed).
'''
import os
file_name = str(input("Please enter the file name? "))
if os.path.exists(file_name):
    print(f"Full path: {os.getcwd()}")
    print(f"Full path: {os.path.abspath(file_name)}")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"File not found. Please check the {file_name}.")

'''
Task 7: Mini Project - Export Discounted Prices
Create a dictionary:
prices = {
"Mouse": 500,
"Keyboard": 800,
"Monitor": 7000,
"Pendrive": 400,
"Camera": 5000
}
Ask the user for a discount percentage.
Write discounted prices into discount_report.txt using:
Product | Original Price | Discounted Price
After writing, read the file and print it to the terminal.
Extra (optional): Write a summary at the bottom of the file:
Total Items: X
Average Discounted Price: Y
'''
prices = {
"Mouse": 500,
"Keyboard": 800,
"Monitor": 7000,
"Pendrive": 400,
"Camera": 5000
}
discount_percentage = int(input("Please give your discounted percentage but less than 80%?  "))
final_price_list = []
if discount_percentage <= 80:
    for name,price in prices.items():
        final_price = price - price * (discount_percentage/100)
        print(f"{name}:{price} and discount percentage {discount_percentage}% and final price {final_price}")
        final_price_list.append({
            "product_name": name,
            "product_price": price,
            "asked_discount_percentage": discount_percentage,
            "final_price": final_price
        })
else:
    print("Please provide a percentage less than 80%.")

with open("discount_report.txt", 'w') as file:
    file.write(f"\nProduct | Original Price | Discounted Price")
total_discounted_price = 0
for item in final_price_list:
    print(f"item: {item}")
    total_discounted_price +=  round(item['final_price'], 2)
    with open("discount_report.txt", 'a') as file:
        file.writelines(f"\n{item['product_name']} | {item['product_price']} | {item['final_price']:.2f}")

with open("discount_report.txt", 'a') as file:
    file.writelines(f"\nTotal Items: {len(final_price_list)} | Average Discounted Price: {total_discounted_price/len(final_price_list)}")

with open("discount_report.txt", 'r') as file:
    lines = file.readlines()
    print(f"lines: {lines}")