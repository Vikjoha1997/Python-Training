from datetime import datetime

name = input("What is your name?")
age = int(input("Age??"))
current_year = datetime.now().year
birth_year = current_year - age
year_100 = birth_year + 100
years_till_100 = year_100 - current_year


print(f"You were born in {birth_year}.") 
print(f"You will be 100 in {year_100}.")

result = f"you will be 100 in {year_100}."
print(f"you have {years_till_100} years left. Enjoy")




