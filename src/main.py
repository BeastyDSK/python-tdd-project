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
  parsed_number_list = [int(num) for num in number_list if num.lstrip('+-').isdigit()]

  # Calculate the sum
  total_sum = sum(parsed_number_list)
  
  # Return the sum
  return total_sum
