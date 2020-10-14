import webbrowser
import time
import json

with open("output.json") as f:
    schedule = json.load(f)["schedule"]

# schedule has a sub array for each day
#   each day has sub arrays for each class
#       each class aray has a time array at the start
#           Time array has start and end split by hour and minute, so [[startH, startM], [endH, endM]]
#       then the zoom link,
#       then the name of the class

localtime = time.localtime(time.time())
weekday = localtime.tm_wday
hour = localtime.tm_hour
minute = localtime.tm_min

hour = 11
minute = 30

todaysClasses = schedule[weekday]
upcomingCourse = ""
for course in todaysClasses:
    end = course[0][1]
    # Since the courses are sorted, we're iterating chronologically which means once we hit a class that ends after the current time, that's
    # the next, or current (if we're late) class.
    if((end[0] > hour) or (end[0] == hour and end[1] > minute)):
        upcomingCourse = course
        break

if(upcomingCourse == ""):
    print("Done for the day!")
else:
    start = upcomingCourse[0][0]
    end = upcomingCourse[0][1]
    if((start[0] < hour) or (start[0] == hour and start[1] < minute)):
        print("Class has already started, opening ", upcomingCourse[2], sep="")

        hoursRemaining = end[0] - hour
        minutesRemaining = end[1] - minute
        if(end[0] > hour and end[1] < minute):
            minutesRemaining += 60
            hoursRemaining -= 1
        
        print("You'll be in class for another", hoursRemaining, "hours and", minutesRemaining, "minutes.")
    else:
        hoursTill = start[0] - hour
        minutesTill = start[1] - minute
        if(start[0] > hour and start[1] < minute):
            minutesTill += 60
            hoursTill -= 1

        hoursLong = end[0] - start[0]
        minutesLong = end[1] - start[1]
        if(end[1] < start[1]):
            minutesLong += 60
            hoursLong -= 1
        
        print("You have", hoursTill, "hours and", minutesTill, "minutes till", upcomingCourse[2], "starts.")
        print("This class is", hoursLong, "hours and", minutesLong, "minutes long.")

    
    webbrowser.open(upcomingCourse[1])
        
# input is here so it'll pause when this opens in terminal, if running in IDLE then
# comment it out
input("Got it?\n")
