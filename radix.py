def radix_sort(nums):
    # Find the maximum number to know the number of digits
    max_num = max(nums)

    # Perform counting sort for each digit, starting from the least significant
    # digit and moving towards the most significant digit.
    exp = 1
    while max_num // exp > 0:

        # Initialize the count array for this digit
        count = [0] * 10

        # Count the occurrences of each digit in the input array
        for num in nums:
            digit = (num // exp) % 10
            count[digit] += 1

        # Compute the cumulative counts of digits
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted array by iterating over the input array in reverse
        # order and placing each element in its correct position in the output array
        output = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            digit = (nums[i] // exp) % 10
            output[count[digit] - 1] = nums[i]
            count[digit] -= 1

        # Update the original array with the sorted values
        for i in range(len(nums)):
            nums[i] = output[i]

        # Print the operations being performed at each digit
        print(f'Radix sort (digit={exp}):', end=' ')
        for num in nums:
            print(f'pb pa ' * (num // exp), end='')
        print()

        # Move to the next digit
        exp *= 10

nums = [170, 45, 75, 90, 802, 24, 2, 66, 9999]
radix_sort(nums)
print(nums)
