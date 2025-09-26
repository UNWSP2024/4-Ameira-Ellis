# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    total_rainfall = 0
    number_years = int(input("Enter number of years: "))
    months = number_years * 12
    for n in range(number_years):
        print(f"Year {n+1}:")
        for m in range(12):
            rainfall = float(input(f"Enter the rainfall for month {m+1} (in inches): "))
            total_rainfall += rainfall
    average_rainfall = total_rainfall / months
    print(f"\nNumber of months: {months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    ######################    


if __name__ == '__main__':
    main()