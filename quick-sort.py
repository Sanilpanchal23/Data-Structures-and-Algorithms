def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
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
    sorted_array = quick_sort(arr)
    print("Sorted array:", sorted_array)
