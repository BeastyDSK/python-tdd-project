def add(num_strs):
  # Provided input is not of type string.
  if not isinstance(num_strs, str):
    return 0

  # Handle both empty and undefined (None in Python) values
  if not num_strs:
    return 0

  # Handle two numbers in a comma-separated string
  
  # Split the input by comma to get the numbers as a list
  num_list = num_strs.split(',')

  # Parse the numbers
  num_one = int(num_list[0])

  # Check if there is a second number
  if len(num_list) < 2 or not num_list[1].lstrip('-+').isdigit():
    return num_one

  num_two = int(num_list[1])

  # Return the sum of the two numbers
  return num_one + num_two
