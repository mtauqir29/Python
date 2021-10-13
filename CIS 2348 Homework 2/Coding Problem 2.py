"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

#Part A

def abstract_date(date):
    correct_date = 0
    latest_date = ""

    if date.find(",") != -1:
        month_day, year = date.split(',')
        if month_day.find(" ") != -1:
            month, day = month_day.split(" ")
            correct_date = 1
            day = day.strip()
            month = month.strip()
            year = year.strip()

            if month == "January":
                latest_date = "1" + "/"
            elif month == "February":
                latest_date = "2" + "/"
            elif month == "March":
                latest_date = "3" + "/"
            elif month == "April":
                latest_date = "4" + "/"
            elif month == "May":
                latest_date = "5" + "/"
            elif month == "June":
                latest_date = "6" + "/"
            elif month == "July":
                latest_date = "7" + "/"
            elif month == "August":
                latest_date = "8" + "/"
            elif month == "September":
                latest_date = "9" + "/"
            elif month == "October":
                latest_date = "10" + "/"
            elif month == "November":
                latest_date = "11" + "/"
            elif month == "December":
                latest_date = "12" + "/"
            else:
                correct_date = 0

            latest_date += day + "/"
            latest_date += year

    if correct_date == 1:
        return latest_date
    else:
        return ""

file = open('inputDates.txt', 'r')
file_dates = []
file_dates = file.readlines()
file.close()

for i in range(len(file_dates) - 1):
    file_dates[i] = file_dates[i][:-1]

file = open('parsedDates.txt', 'w')

for i in file_dates:
    if i == "-1":
        break
    else:
        latest_date = abstract_date(i)
        if latest_date != "":
            file.write(latest_date + "\n")


file.close()

file = open('parsedDates.txt', 'r')
file_parsed_dates = []
file_parsed_dates = file.readlines()
file.close()

# Main program
print("Input file content:\n")
for i in file_dates:
    print(i)

print("\nOutput file content:\n")
for i in file_parsed_dates:
    print(i)
