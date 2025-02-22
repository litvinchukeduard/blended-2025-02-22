'''
Complete the function which returns the weekday according to the input number:

    1 returns "Sunday"
    2 returns "Monday"
    3 returns "Tuesday"
    4 returns "Wednesday"
    5 returns "Thursday"
    6 returns "Friday"
    7 returns "Saturday"
    Otherwise returns "Wrong, please enter a number between 1 and 7"
'''

def whatday(num: int) -> str:
    # Задати словник в якому будуть відповідати числа - дням
    days_dict = {
        1: "Sunday", 
        2: "Monday", 
        3: "Tuesday", 
        4: "Wednesday", 
        5: "Thursday", 
        6: "Friday", 
        7: "Saturday"
    }

    # Дістати з цього словника значення по ключу

    # days_dict.get(1)
    return days_dict.get(num, "Wrong, please enter a number between 1 and 7")

    # if num == 1:
    #     return "Sunday"
    # elif num == 2:
    #     return "Monday"

print(whatday(0)) # "Wrong, please enter a number between 1 and 7"
print(whatday(1)) # Sunday
print(whatday(4)) # Wednesday
print(whatday(7)) # Saturday
print(whatday(9)) # "Wrong, please enter a number between 1 and 7"
