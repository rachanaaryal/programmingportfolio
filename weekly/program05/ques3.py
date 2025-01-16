'''this program takes bunch of command lines and find out the shortest'''


import sys

def shortest_argument(arguments):
    if not arguments:
        return None
    
    return sorted(arguments, key=len)[0]

arguments = sys.argv[1:]

if arguments:
    shortest = shortest_argument(arguments)
    print(f"the shortest argument is:{shortest}")

else:
    print("no arguments were provided.")