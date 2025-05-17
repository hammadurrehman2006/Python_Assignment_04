def access_element(lst, index):
# Access an element at a specific index
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify_element(lst, index, new_value):
# Modify an element at a specific index
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
# Return a slice of the list from start to end (exclusive)
    if start < 0 or end > len(lst) or start > end:
        return "Invalid indices"
    return lst[start:end]

def main():
# Initialize a list with 5 different elements
    game_list = ['apple', 42, 'banana', 3.14, 'grape']
    
    print("Welcome to the List Index Game!")
    print("Initial list:", game_list)
    
    while True:
# Prompt the user for an operation
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
# Access element
            index = int(input("Enter the index of the element to access: "))
            print("Accessed element:", access_element(game_list, index))
        
        elif choice == '2':
# Modify element
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            print("Updated list:", modify_element(game_list, index, new_value))
        
        elif choice == '3':
# Slice list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced list:", slice_list(game_list, start, end))
        
        elif choice == '4':
            print("====Thanks for playing! Goodbye!====")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Start the game
if __name__ == "__main__":
    main()
