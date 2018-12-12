import time
from datetime import date

def within_3_days(filename):
    date = sanitized_date()
    assignment_list = []
    fin = open(filename, "r")
    for line in fin:
        if len(assignment_list) != 1:
            for i in range(len(line)):
                if line[i:i+6] == date:
                    assignment_list.append(line)
        assignment_list.append(line)
    fin.close()
    return assignment_list[0] + assignment_list[1]

def current_date():
    month = ["Nothing", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    today = str(date.today().strftime("%d%m%y"))
    month_integer = int(today[2] + today[3])
    final_date = today[0] + today[1] + month[month_integer] + today[4] + today[5]
    return final_date

def sanitized_date():
    unsanitized = current_date()
    if int(unsanitized[0]) == 0:
        return unsanitized[1::]
    else:
        return unsanitized

print(within_3_days("homework.txt"))
