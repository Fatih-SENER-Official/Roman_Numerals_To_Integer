def roman_to_integer(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_value = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
        prev_value = value

    return integer_value


# Main program
while(1 == 1):
    try:
        if __name__ == "__main__":
            user_input = input("Enter a Roman numeral: ")
            result = roman_to_integer(user_input.upper())
            print(f"The integer value of {user_input} is {result}")

    except Exception as e:
        print("Error:", "Enter a valid Roman Numeral or Integer from 1 to 5000")

