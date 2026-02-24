# Task 2: Demonstrate List Slicing 
'''Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

# list of numbers from 1 to 10
nums1 = [1,2,3,4,5,6,7,8,9,10]
# Extracts the first five elements from the list.
nums2 = nums1[0:5]
# Reverse extracted list
reverse_nums2 = nums2[::-1]
# printing outputs
print(f"Original list: {nums1}")
print(f"Extracted first five elements: {nums2}")
print(f"Reversed extracted elements: {reverse_nums2}")