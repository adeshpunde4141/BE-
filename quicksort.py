import random
import time

# Deterministic Quick Sort function
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Using the first element as the pivot
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return deterministic_quick_sort(lesser) + [pivot] + deterministic_quick_sort(greater)

# Randomized Quick Sort function
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Selecting a random pivot
        pivot = random.choice(arr)
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quick_sort(lesser) + equal + randomized_quick_sort(greater)

# Function to calculate time taken for deterministic quick sort
def analyze_deterministic_quick_sort(arr):
    start_time = time.time()
    sorted_arr = deterministic_quick_sort(arr)
    end_time = time.time()
    print(f"Sorted array (Deterministic): {sorted_arr}")
    print(f"Time taken by Deterministic Quick Sort: {end_time - start_time:.6f} seconds")

# Function to calculate time taken for randomized quick sort
def analyze_randomized_quick_sort(arr):
    start_time = time.time()
    sorted_arr = randomized_quick_sort(arr)
    end_time = time.time()
    print(f"Sorted array (Randomized): {sorted_arr}")
    print(f"Time taken by Randomized Quick Sort: {end_time - start_time:.6f} seconds")

def main():
    user_input = input("Enter the list of numbers to be sorted, separated by spaces: ")
    arr = list(map(int, user_input.split()))  # Convert input string to list of integers

    print("\nChoose the sorting method:")
    print("1. Deterministic Quick Sort (First element as pivot)")
    print("2. Randomized Quick Sort")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        analyze_deterministic_quick_sort(arr.copy())  
    elif choice == '2':
        analyze_randomized_quick_sort(arr.copy()) 
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
