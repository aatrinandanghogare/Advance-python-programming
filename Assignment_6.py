"""
Experiment 6: Dynamic Programming
0/1 Knapsack Problem - Bottom-Up (Tabulation) and Top-Down (Memoization) approaches.
"""

import time


# ---------------- Bottom-Up Approach (Tabulation) ----------------
def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# ---------------- Top-Down Approach (Memoization) ----------------
def knapsack_top_down(values, weights, W):
    n = len(values)
    memo = {}

    def solve(i, w):
        if i == 0 or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]

        if weights[i - 1] > w:
            result = solve(i - 1, w)
        else:
            include = values[i - 1] + solve(i - 1, w - weights[i - 1])
            exclude = solve(i - 1, w)
            result = max(include, exclude)

        memo[(i, w)] = result
        return result

    return solve(n, W)


# ---------------- Naive Recursive Approach (for comparison) ----------------
def knapsack_recursive(values, weights, W, n=None):
    if n is None:
        n = len(values)
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return knapsack_recursive(values, weights, W, n - 1)
    include = values[n - 1] + knapsack_recursive(values, weights, W - weights[n - 1], n - 1)
    exclude = knapsack_recursive(values, weights, W, n - 1)
    return max(include, exclude)


def get_items_from_user():
    n = int(input("Enter number of items: ").strip())
    values, weights = [], []
    for i in range(n):
        v = float(input(f"Enter value of item {i + 1}: ").strip())
        w = float(input(f"Enter weight of item {i + 1}: ").strip())
        values.append(v)
        weights.append(int(w))
    capacity = int(input("Enter knapsack capacity (W): ").strip())
    return values, weights, capacity


def print_menu():
    # om kutwal SY12 Roll No.: 70 
    print("\n===== 0/1 KNAPSACK PROBLEM =====")
    print("1. Solve using Bottom-Up (Tabulation)")
    print("2. Solve using Top-Down (Memoization)")
    print("3. Compare Bottom-Up vs Top-Down vs Naive Recursive (time taken)")
    print("4. Run built-in example (values=[60,100,120], weights=[10,20,30], W=50)")
    print("5. Exit")
    print("==================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            values, weights, W = get_items_from_user()
            result = knapsack_bottom_up(values, weights, W)
            print(f"\nMaximum value (Bottom-Up): {result}")

        elif choice == "2":
            values, weights, W = get_items_from_user()
            result = knapsack_top_down(values, weights, W)
            print(f"\nMaximum value (Top-Down): {result}")

        elif choice == "3":
            values, weights, W = get_items_from_user()

            start = time.perf_counter()
            bu_result = knapsack_bottom_up(values, weights, W)
            bu_time = time.perf_counter() - start

            start = time.perf_counter()
            td_result = knapsack_top_down(values, weights, W)
            td_time = time.perf_counter() - start

            print(f"\nBottom-Up : {bu_result}   Time: {bu_time:.6f}s")
            print(f"Top-Down  : {td_result}   Time: {td_time:.6f}s")

            if len(values) <= 20:
                start = time.perf_counter()
                rec_result = knapsack_recursive(values, weights, W)
                rec_time = time.perf_counter() - start
                print(f"Recursive : {rec_result}   Time: {rec_time:.6f}s")
            else:
                print("Recursive : Skipped (too many items, would take too long)")

        elif choice == "4":
            values = [60, 100, 120]
            weights = [10, 20, 30]
            W = 50
            bu_result = knapsack_bottom_up(values, weights, W)
            td_result = knapsack_top_down(values, weights, W)
            print(f"\nvalues={values}, weights={weights}, W={W}")
            print(f"Bottom-Up result: {bu_result}")
            print(f"Top-Down result:  {td_result}")

        elif choice == "5":
            print("Exiting the Knapsack Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
