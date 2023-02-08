from datetime import date
from datetime import datetime
import csv

def markAttendance(name, filename):

    list_column=["Name","Time"]
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    column_A= name
    column_B= dtString
    list_row = []
    for i in range(len(column_A)):
        list_temp=[column_A[i],column_B]
        list_row.append(list_temp)       
    with open (filename, 'w', newline="") as entry:
        writer=csv.writer(entry)
        writer.writerow(list_column)
        writer.writerows(list_row)
        entry.close()
