import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Makes all characters in an input string upper case or lower case based on arguments given")

# Add arguments
parser.add_argument("-i", "--input", help="The input string to transform.", default="default_value")
parser.add_argument("-c", "--case", help="Specify the case transformation: 'upper' for uppercase or 'lower' for lowercase.")

# Parse arguments
args = parser.parse_args()

# Access arguments
if args.case.lower() == 'lower':
    print(args.input.lower())
elif args.case.lower() == 'upper':
    print(args.input.upper())
else:
    print(f"User entered {args.case.lower()}, please provide 'upper' or 'lower")