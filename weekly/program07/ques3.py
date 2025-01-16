'''this program a list of countries and their capital cities'''

def main():
    country_capitals = {}

    print("Welcome to the Country-Capital Manager!")
    print("Type 'exit' to stop the program.\n")

    while True:
        country = input("Enter the name of a country: ").strip().capitalize()

        if country.lower() == 'exit':
            print("Goodbye!")
            break

        if country in country_capitals:
            print(f"The capital of {country} is {country_capitals[country]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip().capitalize()
            country_capitals[country] = capital
            print(f"{capital} has been saved as the capital of {country}.")

        print()  

main()
