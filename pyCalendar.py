from calendar import*

year = int(input("\nEnter the year for the calendar: "))

# 2 = 2 characters for days (Mo, Tu, etc)
# 1 = 1 line (row) for each week
# 8 = 8 rows for each month
# 2 = 2 columns for all months of the year
print(calendar(year, 2, 1, 8, 3))
