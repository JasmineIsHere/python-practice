from calendar import monthcalendar
import datetime

DAYS = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
MONTHS = ("JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER")

print("Calendar Maker")

while True:
    response = input("Enter the year for the calendar > ")
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    
    print("Invalid year. Please enter a numeric year, e.g. 2022.")
    continue

while True:
    response = input("Enter the month for the calendar (1-12) > ")
    if not response.isdecimal():
        print("Please enter a numeric month, e.g. 1 means January")
    month = int(response)
    
    if 1 <= month <= 12:
        break

    print("Please enter a number from 1 to 12")

def getCalendarFor(year, month):
    calendarText = ""
    calendarText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    #week labels
    for day in DAYS:
        calendarText += ".." + day + ".."
    
    calendarText += "\n"

    #horizontal line to separate the weeks
    weekSeparator = ('+----------' * 7) + "+\n"

    #bank rows have 10 spaces between | day separators:
    blankRow = ('|          ' * 7) + "|\n"

    currentDate = datetime.date(year,month,1)

    #that week's sunday's date
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True:
        calendarText += weekSeparator

        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" "*8)
            currentDate += datetime.timedelta(days=1)

        dayNumberRow += "\n"

        calendarText += dayNumberRow
        for i in range(3):
            calendarText += blankRow
        
        if currentDate.month != month:
            break
    
    calendarText += weekSeparator
    return calendarText

calendarText = getCalendarFor(year,month)
print(calendarText)

# calendarFileName = "calendar_{}_{}.txt".format(year,month)
# with open(calendarFileName, "w") as fileObj:
#     fileObj.write(calendarText)

print("Saved to " + calendarFileName)