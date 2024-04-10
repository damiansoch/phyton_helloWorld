import csv

csv_file_path = "test.csv"

# writing csv file
with open(csv_file_path, "w", newline='', encoding='utf-8') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerow(["user_id", "user_name", "comments_qty"])
    writer.writerow(["1", "damiansoch", 20])
    writer.writerow(["2", "kingasoch", 55])
    writer.writerow(["3", "milenasoch", 84])
    writer.writerow(["4", "szymonsoch", 35])
    writer.writerow(["5", "oreosoch", 0])


# reading form csv file
def print_csv_file():
    with open(csv_file_path, newline='', encoding='utf-8') as csv_f:
        row_num = 0
        reader1 = csv.reader(csv_f)
        for row in reader1:
            print(f"{row_num}: {row}")
            row_num += 1


print_csv_file()

# modifying the id
# Read the existing CSV file into a list of rows (each row as a list)
with open(csv_file_path, mode="r", newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    # Use a list comprehension to read and store all rows
    rows = [row for row in reader]

for row in rows[1:]:  # Skip the header row with [1:]
    # Convert the user_id to int, modify it, and convert back to str
    row[0] = str(int(row[0]) + 100)

# Write the modified list of rows back to the CSV file
with open(csv_file_path, mode="w", newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)

print("CSV file has been updated.")
print_csv_file()
