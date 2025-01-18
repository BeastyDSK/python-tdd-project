def add(num_strs):
  # Provided input is not of type string.
  if not isinstance(num_strs, str):
    return 0

  # Handle both empty and undefined (None in Python) values
  if not num_strs:
    return 0

  # Handle two numbers in a comma-separated string
  
  # Split the input by comma to get the numbers as a list
  number_list = num_strs.split(',')

  # Parse the string values to integers and filter only the valid numbers
  parsed_number_list = [int(num) for num in number_list if num.lstrip('+-').isdigit()]

  # Calculate the sum
  total_sum = sum(parsed_number_list)
  
  # Return the sum
  return total_sum
