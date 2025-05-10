
def get_first_and_last_element(lst):

    if len(lst) == 0:
        print("The list is empty.")
        return None, None
    elif len(lst) == 1:
        print("The list has only one element.")
        return lst[0], lst[0]
    else:
        first_element = lst[0]
        last_element = lst[-1]
        return first_element, last_element



def get_lst():
    
    
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    first_element, last_element = get_first_and_last_element(lst)
    if first_element is not None and last_element is not None:
        print(f"The first element is: {first_element}")
        print(f"The last element is: {last_element}")
    else:
        print("The list is empty or has only one element.")


if __name__ == '__main__':
    main()

