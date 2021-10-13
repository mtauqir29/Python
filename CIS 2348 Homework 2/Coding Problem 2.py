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


# Main program
date = input()

while (date != "-1"):
    latest_date = abstract_date(date)

    if latest_date != "":
        print(latest_date)

    print()
    date = input()