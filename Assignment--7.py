Read an input file, count lines, extract the first two lines and
write them into a new file.
"""

import os

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def create_sample_input():
    lines = [
        "Line 1: This is the first line.\n",
        "Line 2: This is the second line.\n",
        "Line 3: This is the third line.\n",
        "Line 4: This is the fourth line.\n",
    ]
    with open(INPUT_FILE, "w") as f:
        f.writelines(lines)
    print(f"Sample '{INPUT_FILE}' created with {len(lines)} lines.")


def write_custom_input():
    print("Enter lines of text (type END on a new line to stop):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line + "\n")
    with open(INPUT_FILE, "w") as f:
        f.writelines(lines)
    print(f"'{INPUT_FILE}' saved with {len(lines)} lines.")


def read_all_lines():
    with open(INPUT_FILE, "r") as f:
        return f.readlines()


def count_lines():
    return len(read_all_lines())


def extract_and_write():
    lines = read_all_lines()
    first_two = lines[:2]
    #Om Kutwal Sy-12 Roll no. 70
    with open(OUTPUT_FILE, "w") as f:
        f.writelines(first_two)
    return first_two


def display_file(filename):
    print(f"\n--- Content of {filename} ---")
    with open(filename, "r") as f:
        print(f.read())


def print_menu():
    print("\n===== FILE HANDLING PROGRAM =====")
    print("1. Create sample input file")
    print("2. Write your own input file")
    print("3. Display input file")
    print("4. Count total lines")
    print("5. Extract first two lines and write to output file")
    print("6. Display output file")
    print("7. Exit")
    print("=================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            create_sample_input()

        elif choice == "2":
            write_custom_input()

        elif choice in ("3", "4", "5") and not os.path.exists(INPUT_FILE):
            print(f"'{INPUT_FILE}' not found. Create it first (option 1 or 2).")

        elif choice == "3":
            display_file(INPUT_FILE)

        elif choice == "4":
            print(f"Total number of lines: {count_lines()}")

        elif choice == "5":
            extracted = extract_and_write()
            print(f"Extracted {len(extracted)} line(s) written to {OUTPUT_FILE}")

        elif choice == "6":
            if os.path.exists(OUTPUT_FILE):
                display_file(OUTPUT_FILE)
            else:
                print(f"'{OUTPUT_FILE}' not found. Run option 5 first.")

        elif choice == "7":
            print("Exiting the File Handling Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
