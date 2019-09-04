#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
rate = input("rate:")
try:
    r = float(rate)
    h = float(hrs)
except:
    print("輸入錯誤，請再次輸入數字")
    quit()

if h > 40:
    pay = (h-40)*1.5*r + 40*r
else:
    pay = h * r
print("You have to pay:",pay)
