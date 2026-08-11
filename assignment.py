'''
Task 1: Write Sales Records to a File

1. Create a list of sales amounts:
2. sales = [1200, 450, 980, 1500, 3000]
3. Open a file named sales_data.txt in write mode.
4. Write each sale on a new line in the file.
5. Close the file, then reopen it and print its contents.

Extra (optional): Write the data in comma-separated format instead of separate lines.
'''
sales = [1200, 450, 980, 1500, 3000]

for sale in sales:
    with open('sales_data.txt', 'a') as sale_data:
        sale_data.writelines(f"\n {sale} \n")

with open('sales_data.txt', 'a') as sales_data:
    sales_data.write(', '.join(map(str, sales)))

with open('sales_data.txt', 'r') as sales:
    print(f"{sales.read()}");

'''
Task 2: Read File in Different Ways
Using the same sales_data.txt:
1. Read the entire file using read() and print it.
2. Read the first line using readline().
3. Read all lines using readlines() and convert them into a list of integers.
Ensure proper formatting and cleanup of newline characters.
'''

with open("sales_data.txt", "r") as file:
    print(f"\n\n The file data is: {file.read()}")

with open("sales_data.txt", "r") as file:
    print(f"First line {file.readline().strip()}")
    print(f"Second line {file.readline().strip()}")
    print(f"Third line {file.readline().strip()}")

# def string_to_int(sales):
#     print(sales)
#     if ", " in sales:
#         print(f"sale {list(map(int,sales.split(", ")))}")
#     else:
#         sales.strip()
#     print(f"new sales {sales}")
#     return sales

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
    file.writelines(f"{sale}\n" for sale in sales)

with open("sales_data.txt", "r") as file:
    line = file.readlines()
    print(f"Number of line in the sales-data.txt file is: {len(line)}")