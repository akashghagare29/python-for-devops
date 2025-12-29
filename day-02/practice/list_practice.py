# list = [1, "akash", 3.14, True]
# print("Original List:", list)
# print("Type of List:", type(list))
# print("Length of List:", len(list))
# print("First Element:", list[0])
# print("Last Element:", list[-1])
# list.append("aws")
# print("Updated List:", list)
# # print(dir(list))
# # print(list.extend.__doc__)
# list.remove(3.14)
# print("Updated List:", list)
# list.reverse()
# print("Reversed List:", list)

# # Iterate through the list and print type of each item
# for item in list:
#     if isinstance(item, str):
#         print(f"{item} is a string")
#     elif isinstance(item, bool):
#         print(f"{item} is a boolean")
#     elif isinstance(item, float):
#         print(f"{item} is a float")
#     elif isinstance(item, int):
#         print(f"{item} is an integer")

# items = input("Enter the item to search in the list: ")

# # Check the items found in the list or not
# if items in list:
#     print(f"{items} found in the list")
# else:
#     print(f"{items} not found in the list")

# print("Updated List:", list)

list = [6, 1, 7, 8, 9, 4]
print("Original List:", list)   # Print the original list  
print("Type of List:", type(list))  # Print the type of the list
print("Length of List:", len(list)) # Print the length of the list
print("First Element:", list[0])    # Print the first element of the list
print("Last Element:", list[-1])    # Print the last element of the list
list.append(10)                  # Append 10 to the end of the list
print("Updated List:", list)    # Print the updated list
print(f"Sum of the list: {sum(list)}")  # Print the sum of all elements in the list
print(f"Max of the list: {max(list)}")    # Maximum element in the list
print(f"Min of the list: {min(list)}")    # Minimum element in the list
print(f"Sorted List: {sorted(list)}")  # Print the sorted version of the list
# print(dir(list))               # Print the directory of list methods

search_num = int(input("Enter the number to search in the list: "))  # Input number to search
# Check if the number is in the list
if search_num in list:
    print(f"{search_num} found in the list")
else:
    print(f"{search_num} not found in the list")