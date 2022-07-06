def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Please enter a month between 1 and 12"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  number_of_days = month_days[month-1]
  if month == 2:
    if is_leap(year) == True:
      number_of_days = 29
  
  return f"{month}/{year} has {number_of_days} days in it!"
  
carry_on = "y"

while carry_on == "y":
  year = int(input("Enter a year: "))
  month = int(input("Enter a month: "))
  days = days_in_month(year, month)
  print(days)
  carry_on = input("Would you like to go again? y/n ")
