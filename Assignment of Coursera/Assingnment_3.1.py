# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
#  the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
#  of 10.50 per hour to test the program (the pay should be 498.75). You should
#  use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types
# numbers properly.

# =====================================================================
hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour=input("Enter rate per hour")
r_p_h = float(rate_per_hour)
total_Upto_40 = h * r_p_h
total_above_40 = ((h-40)*1.5*r_p_h)+40*r_p_h
if(h>40) :
	print(total_above_40)

else :
    print(total_Upto_40)
