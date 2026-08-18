Files the script creates or modifies
- `sales_data.txt`
- `products.txt`
- `discount_report.txt`

**Task 1 — Write Sales Records to a File**
- Purpose: Create a list of sales amounts and write them to `sales_data.txt`.
- Behavior: Writes each sale on a new line and appends a comma-separated line containing all sales.
- Notes: The script appends to the file; remove `sales_data.txt` for a fresh run.

**Task 2 — Read File in Different Ways**
- Purpose: Demonstrate `read()`, `readline()`, iterating lines, and conversion to integers.
- Behavior: Prints the whole file, prints first three lines, then parses numeric values into a Python list.
- Notes: Parsing supports one sale per line or a comma-separated line; whitespace and empty lines are ignored.

**Task 3 — Append New Sales**
- Purpose: Append new sales values (5000, 2500, 1700) to `sales_data.txt` and print updated contents.
- Behavior: Intended to append `new_sales` and then show the updated file and optionally the line count.
- Known issue: The original script appends the parsed `sales` list instead of `new_sales`, which can duplicate earlier entries. Consider changing the write loop to use `new_sales`.

**Task 4 — Generate Summary Report from File**
- Purpose: Read all sales values from `sales_data.txt`, convert to integers, and compute total, highest, lowest, and average.
- Behavior: Extracts numbers from line-separated or comma-separated formats and prints summary statistics.
- Notes: If `sales_data.txt` contains non-numeric text, integer conversion raises `ValueError`. Add input validation or try/except around conversion to harden the script.

**Task 5 — Create Product Info File (User Input)**
- Purpose: Prompt the user for 3 products and prices, store them in `products.txt`, and print the results.
- Behavior: Collects up to 3 product name/price pairs and appends them to `products.txt` in the format `Product Name | Price`.
- Known issue: The script uses nested double quotes in f-strings (e.g., `f"{product["product_name"]}"`) causing `SyntaxError`. Use single quotes inside or dictionary access with single-quoted keys: `product['product_name']`.

**Task 6 — Read File Safely (Error Handling)**
- Purpose: Ask the user for a filename, check existence with `os.path.exists()`, and print contents if present; otherwise show a friendly message.
- Behavior: Prints full path info and file contents when the file exists.

**Task 7 — Export Discounted Prices (Mini Project)**
- Purpose: Apply a user-provided discount to a predefined `prices` dictionary, write discounted prices to `discount_report.txt`, and print the report.
- Behavior: Prompts for a discount percentage (expected <= 80), computes discounted prices, writes a report, and appends a summary with total items and average discounted price.
- Notes: If `final_price_list` is empty, division by zero will occur when calculating the average—validate input before writing the summary.

Next steps
- I removed the separate `README_Task*.md` files and consolidated their content here. I can also:
	- Fix the `new_sales` append bug and the f-string quoting errors.
	- Add input validation and small unit tests.

Tell me which fixes you'd like me to apply next.
