#read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#The file name will be provided as a command line argument. You can download the sample data from http://www.py4e.com/code3/romeo.txt
#You can also use this file as a simple test for your program. The file contains a

import re
import sys

def sum_numbers_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        # Find all sequences of digits, optionally with a decimal point
        numbers = re.findall(r'\d+\.?\d*', text)
        # Convert to float and sum
        total = sum(float(num) for num in numbers if num)
        return total
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sum_numbers.py <filename>")
    else:
        result = sum_numbers_in_file(sys.argv[1])
        print(result)