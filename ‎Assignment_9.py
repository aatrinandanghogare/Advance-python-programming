Experiment 9: File Handling and I/O - Reading/writing files (CSV and JSON)
Read data from a CSV file, convert it to JSON and write it to a .json file.
"""

import csv
import json
import os

CSV_FILE = "input.csv"
JSON_FILE = "output.json"


def create_sample_csv():
    rows = [
        ["id", "name", "age"],
        ["1", "John Doe", "30"],
        ["2", "Jane Smith", "25"],
        ["3", "Bob Johnson", "40"],
    ]
    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"Sample '{CSV_FILE}' created with {len(rows) - 1} records.")


def add_csv_from_user():
    fields = input("Enter column names (comma-separated): ").split(",")
    fields = [f.strip() for f in fields]
    n = int(input("Enter number of records: ").strip())
    rows = []
    for i in range(n):
        values = input(f"Enter values for record {i + 1} (comma-separated): ").split(",")
        rows.append([v.strip() for v in values])
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)
    print(f"'{CSV_FILE}' saved with {n} records.")


def display_csv():
    print(f"\n--- Content of {CSV_FILE} ---")
    with open(CSV_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(", ".join(row))


def csv_to_json(csv_path, json_path):
    json_array = []
    with open(csv_path, encoding="utf-8") as csvf:
        reader = csv.DictReader(csvf)
        #Om Kutwal Sy-12 Roll no. 70
        for row in reader:
            json_array.append(row)
    with open(json_path, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(json_array, indent=4))
    return len(json_array)


def display_json():
    print(f"\n--- Content of {JSON_FILE} ---")
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))


def print_menu():
    print("\n===== CSV TO JSON CONVERTER =====")
    print("1. Create sample CSV file")
    print("2. Enter your own CSV data")
    print("3. Display CSV file")
    print("4. Convert CSV to JSON")
    print("5. Display JSON file")
    print("6. Exit")
    print("=================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            create_sample_csv()

        elif choice == "2":
            try:
                add_csv_from_user()
            except ValueError:
                print("Invalid input. Please enter a valid number of records.")

        elif choice in ("3", "4") and not os.path.exists(CSV_FILE):
            print(f"'{CSV_FILE}' not found. Create it first (option 1 or 2).")

        elif choice == "3":
            display_csv()

        elif choice == "4":
            count = csv_to_json(CSV_FILE, JSON_FILE)
            print(f"{count} record(s) converted and written to {JSON_FILE}")

        elif choice == "5":
            if os.path.exists(JSON_FILE):
                display_json()
            else:
                print(f"'{JSON_FILE}' not found. Run option 4 first.")

        elif choice == "6":
            print("Exiting the CSV to JSON Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
