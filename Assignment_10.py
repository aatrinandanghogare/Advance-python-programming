Experiment 10: NumPy
Create a 1-D array of numbers 1 to 10, perform slicing, compute statistics
(sum, mean, max, min) and apply broadcasting.
"""

import numpy as np

arr = np.arange(1, 11)


def show_array():
    print("Array:", arr)
    print("Shape:", arr.shape, "| Data type:", arr.dtype)


def slicing_operations():
    print("Original array      :", arr)
    print("First 5 elements    :", arr[:5])
    print("Last 3 elements     :", arr[-3:])
    print("Elements 3rd to 7th :", arr[2:7])
    #Om Kutwal Sy-12 Roll no. 70
    print("Every 2nd element   :", arr[::2])
    print("Reversed array      :", arr[::-1])


def custom_slice():
    try:
        start = int(input("Enter start index: ").strip())
        stop = int(input("Enter stop index: ").strip())
        step = int(input("Enter step: ").strip())
        print("Result:", arr[start:stop:step])
    except ValueError:
        print("Invalid input. Please enter integers.")


def statistics():
    print("Sum     :", arr.sum())
    print("Mean    :", arr.mean())
    print("Maximum :", arr.max())
    print("Minimum :", arr.min())
    print("Std Dev :", round(arr.std(), 4))


def broadcasting():
    print("Original array       :", arr)
    print("Add 5 (arr + 5)      :", arr + 5)
    print("Multiply 2 (arr * 2) :", arr * 2)
    print("Square (arr ** 2)    :", arr ** 2)
    print("Miles to km (arr*1.6):", arr * 1.6)


def custom_broadcasting():
    try:
        value = float(input("Enter a scalar value: ").strip())
    except ValueError:
        print("Invalid number.")
        return
    op = input("Choose operation (+, -, *, /): ").strip()
    if op == "+":
        print("Result:", arr + value)
    elif op == "-":
        print("Result:", arr - value)
    elif op == "*":
        print("Result:", arr * value)
    elif op == "/":
        if value == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", arr / value)
    else:
        print("Invalid operation.")


def print_menu():
    print("\n===== NUMPY OPERATIONS =====")
    print("1. Display the array (1 to 10)")
    print("2. Slicing operations")
    print("3. Custom slice (start, stop, step)")
    print("4. Statistical measures")
    print("5. Broadcasting examples")
    print("6. Custom broadcasting (array op scalar)")
    print("7. Exit")
    print("============================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            show_array()
        elif choice == "2":
            slicing_operations()
        elif choice == "3":
            custom_slice()
        elif choice == "4":
            statistics()
        elif choice == "5":
            broadcasting()
        elif choice == "6":
            custom_broadcasting()
        elif choice == "7":
            print("Exiting the NumPy Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
