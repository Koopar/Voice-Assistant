def frequency_sort(arr):
    # Count the frequency of each number in the array
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    # Create a list to store the frequency counts
    frequency_list = []
    for num, count in frequency_dict.items():
        frequency_list.extend([count] * count)

    # Sort the frequency list
    frequency_list.sort()

    return frequency_list


# Input processing
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array elements

# Perform frequency count, sorting, and display
result = frequency_sort(arr)
print(*result)
