def num_of_days_in_hours(days, conversion_unit):
    try:
        if conversion_unit == "hours":
            return f"{days} days is {days * 24} {conversion_unit} "
        elif conversion_unit == "minutes":
            return f"{days} days is {days * 24 * 60} {conversion_unit}"
        else:
            return "not accurate unit"
    except ValueError:
        return "something is wrong with your input"


def validate_conversion():
    user_input = input("Enter your number of days \n")
    user_unit = input("Enter your unit \n")

    if int(user_input) <= 0:
        return "Please enter a valid input"

    else:
        return num_of_days_in_hours(int(user_input), user_unit)