

import sys

def arguments():
    argument_count = len(sys.argv) - 1

    print(f"number of arguments provided: {argument_count}")

if __name__ == "__main__":
    arguments()