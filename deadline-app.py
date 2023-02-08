import datetime


# user enters date
# project returns how many days/hours/minutes the user has exactly
# logic: deadline date - current date

def deadline_counter(deadline_input):
    current_date = datetime.datetime.today() #module.class.method()

    converted_day = datetime.datetime.strptime(deadline_input, '%Y/%m/%d')

    num_of_days = converted_day - current_date

    return f"you have {num_of_days} until your deadline"


answer = deadline_counter(input("Enter your deadline in the format yyyy/mm/dd \n"))

print(answer)
