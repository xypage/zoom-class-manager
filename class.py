import webbrowser
import time
import json
from scheduleFormatter import scheduleFormatter

try:
    f = open("output.json")
except FileNotFoundError:
    sf = scheduleFormatter("input.txt")
    sf.makeOutput()
    f = open("output.json")
except:
    print("Unknwon error in try except block")
schedule = json.load(f)
f.close()


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

todaysClasses = schedule[str(weekday)]
upcomingCourse = ""
for course in todaysClasses:
    end = {"hour": int(course["end"]["hour"]), "minute": int(course["end"]["minute"])}
    # Since the courses are sorted, we're iterating chronologically which means once we hit a class that ends after the current time, that's
    # the next, or current (if we're late) class.
    if((end["hour"] > hour) or (end["hour"] == hour and end["minute"] > minute)):
        upcomingCourse = course
        break

if(upcomingCourse == "" and weekday != 4):
    print("Done for the day!")
    print("Tomorrow you have:")
    tomorrowsClasses = schedule[str((weekday + 1) % 5)]
    for course in tomorrowsClasses:
        print(f'\t{course["name"]} from {course["start"]["hour"]}:{course["start"]["minute"]} to {course["end"]["hour"]}:{course["end"]["minute"]}')

elif(upcomingCourse == "" and weekday == 4):
    print("Done for the week!")

else:
    #print(weekday, hour, minute, upcomingCourse)
    start = {"hour": int(upcomingCourse["start"]["hour"]), "minute": int(upcomingCourse["start"]["minute"])}
    end = {"hour": int(upcomingCourse["end"]["hour"]), "minute": int(upcomingCourse["end"]["minute"])}
    if((start["hour"] < hour) or (start["hour"] == hour and start["minute"] < minute)):
        print("Class has already started, opening ", upcomingCourse["name"], sep="")

        hoursRemaining = end["hour"] - hour
        minutesRemaining = end["minute"] - minute
        if(end["hour"] > hour and end["minute"] < minute):
            minutesRemaining += 60
            hoursRemaining -= 1
        
        print("You'll be in class for another", hoursRemaining, "hours and", minutesRemaining, "minutes.")
    else:
        hoursTill = start["hour"] - hour
        minutesTill = start["minute"] - minute
        if(start["hour"] > hour and start["minute"] < minute):
            minutesTill += 60
            hoursTill -= 1

        hoursLong = end["hour"] - start["hour"]
        minutesLong = end["minute"] - start["minute"]
        if(end["minute"] < start["minute"]):
            minutesLong += 60
            hoursLong -= 1
        
        print("You have", hoursTill, "hours and", minutesTill, "minutes till", upcomingCourse["name"], "starts.")
        print("This class is", hoursLong, "hours and", minutesLong, "minutes long.")

    
    webbrowser.open(upcomingCourse["link"])
        
# input is here so it'll pause when this opens in terminal, if running in IDLE then
# comment it out
input("Got it?\n")
