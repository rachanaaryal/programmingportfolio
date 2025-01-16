'''thos program finds out what operating system we are working on'''

import sys

def module():
    platform = sys.platform

    print(f"the operating system platform is: {platform}")

if __name__ == "__main__":
    module() 