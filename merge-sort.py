def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
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
    sorted_array = merge_sort(arr)
    print("Sorted array:", sorted_array)
