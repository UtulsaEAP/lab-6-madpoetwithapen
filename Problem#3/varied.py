def process_input(input_string):
    tokens = input_string.split()

    nums = [float(token) for token in tokens]

    if len(nums) == 0:
        return None, None

    max_value = max(nums)
    average_value = sum(nums)/len(nums)
    return max_value, average_value


if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')

    if max_value is not None and average_value is not None:

        print(f'Max Value:{max_value:.2f}')

        print(f'Average Value: {average_value:.2f}')

    else:

        print("No numbers provided.")
