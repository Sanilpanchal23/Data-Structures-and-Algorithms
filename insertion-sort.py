def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
    sorted_array = insertion_sort(arr)
    print("Sorted array:", sorted_array)
