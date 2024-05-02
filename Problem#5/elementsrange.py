def filter_and_print_range(input_list, min_val, max_val):
    #write your code here

    filtered_numbers = []

    for number in input_list: 

        if min_val<= number <= max_val: 
            filtered_numbers.append(number)

    print(','.join(map(str,filtered_numbers)), end=',')


if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(num) for num in user_input.split()]



    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int,user_input.split())


    filter_and_print_range(integer_list, min_val,max_val)

   
