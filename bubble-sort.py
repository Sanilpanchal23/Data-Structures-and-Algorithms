def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    # Get input from the user
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert input string to list of integers
    try:
        arr = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        exit(1)

    print("Original array:", arr)
    sorted_array = bubble_sort(arr)
    print("Sorted array:", sorted_array)
