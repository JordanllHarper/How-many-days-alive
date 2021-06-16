#Program telling you how long you have been alive

#Module
import math


#User inputs
today_input = input("Please give today's date in DDMMYYYY format: ")
birthday_input = input("Please give your birth date in DDMMYYYY format: ")

#Concatination of values
today_day = (today_input[0] + today_input[1])
today_day_integered = int(today_day)
today_month = (today_input[2] + today_input[3])
today_month_integered = int(today_month)
today_year = (today_input[4] + today_input[5] + today_input[6] + today_input[7])
today_year_integered = int(today_year)

birth_day = (birthday_input[0] + birthday_input[1])
birth_day_integered = int(birth_day)
birth_month = (birthday_input[2] + birthday_input[3])
birth_month_integered = int(birth_month)
birth_year = (birthday_input[4] + birthday_input[5] + birthday_input[6] + birthday_input[7])
birth_year_integered = int(birth_year)



#Dictionary with the days in each month
months_with_days = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31

}
#Calculation of today in days

today_year_integered_in_days = today_year_integered * 365


def compoundingMonths(currentMonth):
    values = months_with_days.values()
    values_list = list(values)
    values_list_spliced = values_list[:currentMonth - 1]

    total_days = 0
    for index in values_list_spliced:
        total_days += index
    return total_days

today_months_into_year = compoundingMonths(today_month_integered)

#leap year accounting

years_alive = today_year_integered - birth_year_integered

years_alive_divided_by4 = math.ceil(years_alive / 4)



today_in_days = today_year_integered_in_days + today_months_into_year + today_day_integered + years_alive_divided_by4








#Calculation of birthday in days
birth_year_integered_in_days = birth_year_integered * 365


birth_months_integered_compounded = compoundingMonths(birth_month_integered)

birth_day_in_days = birth_year_integered_in_days + birth_months_integered_compounded + birth_day_integered


days_alive = today_in_days - birth_day_in_days
print(days_alive)