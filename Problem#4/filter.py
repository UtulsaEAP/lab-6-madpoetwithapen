

def process_and_print(input_string):
      # Split into separate strings
    numbers = input_string.split()
    # Convert strings to integers and filter out negative values
    nums = [int(number) for number in numbers if int(number) < 0]
    
    nums.sort(reverse=True)

    for x in nums: 
       print(x, end=' ')



if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)






    # Convert strings to integers and filter out negative values

    

