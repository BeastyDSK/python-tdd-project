import re

def retrieve_delimiter(s):
  # Try to match the custom delimiter pattern (e.g. "//;\n")
  match = re.match(r'^\/\/(.)\n', s)
  return match.group(1) if match else ','

def add(num_strs):
  # Provided input is not of type string.
  if not isinstance(num_strs, str):
    return 0

  # Handle both empty and none values
  if not num_strs:
    return 0

  # Retrieve the delimiter if present
  delimiter = retrieve_delimiter(num_strs)
  
  # Escape special regex characters in the delimiter
  escaped_delimiter = re.escape(delimiter)
  
  # Create regex to split by the provided delimiter or newline
  regex = r'[{}|\n]'.format(escaped_delimiter)

  # Split the input string by the custom delimiter or newline character
  number_list = re.split(regex, num_strs)

  # Parse the string values to integers and filter only the valid numbers
  parsed_number_list = []
  negative_numbers = []

  for index in range(0, len(number_list)):
    # Check if the number is valid
    num_stripped = number_list[index].strip()
    if num_stripped:
      temp_num = num_stripped.lstrip('+EO')

      if temp_num.startswith('-'):
        # Collect negative numbers
        negative_numbers.append(temp_num)

      # ignore numbers that are greater than 1000 inclusive
      if temp_num.isdigit():
        temp_num_parsed = int(temp_num)
        if temp_num_parsed < 500 or temp_num_parsed > 1000:
          is_even_str = num_strs.startswith('E')
          is_odd_str = num_strs.startswith('O')

          if is_even_str or is_odd_str:
            if is_even_str and index % 2 == 0:
              parsed_number_list.append(temp_num_parsed)
            if is_odd_str and index % 2 == 1:
              parsed_number_list.append(temp_num_parsed)
          else:
            parsed_number_list.append(temp_num_parsed)

  # If there are negative numbers, raise an error with all of them
  if negative_numbers:
    raise ValueError(f"Negative numbers not allowed: {','.join(negative_numbers)}")


  # Calculate the sum
  total_sum = sum(parsed_number_list)
  
  # Return the sum
  return total_sum
