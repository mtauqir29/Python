"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        high_nums = i
        for x in range(i + 1, len(numbers)):
            if numbers[x] > numbers[high_nums]:
                high_nums = x
        temp = numbers[i]
        numbers[i] = numbers[high_nums]
        numbers[high_nums] = temp
        for num in numbers:
            print(str(num), end=' ')
        print()

    return numbers
if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(nums) for nums in input().split()]
    selection_sort_descend_trace(numbers)
