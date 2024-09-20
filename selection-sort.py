def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
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
    sorted_array = selection_sort(arr)
    print("Sorted array:", sorted_array)
