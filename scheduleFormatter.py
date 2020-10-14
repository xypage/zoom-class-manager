import json

#filler for all days of week
week = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: []
}

dayLetters = ["m", "t", "w", "r", "f"]

# The document should be in the following format, unless otherwise specified, assume no linebreaks
# Days: as mtwrf, whatever days that class occurs on, no spaces between them
# Times: The start and end times, with a space between, in 24 hour format with no colons
#    ex: class from 1:30PM to 2:20PM would be 1330 1420
# Class name: The name of the class, no specific format necessary, at the end of this put a new line
# Link to zoom: This should be the zoom link, make sure it's on a separate line from anything else
# Go to a new line again for the next entry, there should be no blank lines though,
#    should be description, link for that class, description for next class, link for next class
#    etc. with no blank lines anywhere

# Make sure you pick the name of the text document you're opening here
f = open("input.txt")
contents = f.read().split("\n")
for i in range(0, len(contents), 2):
    course = {}
    course["link"] = contents[i+1]


    desc = contents[i]
    desc = desc.split(" ")


    startHour = desc[1][:-2]
    startMinute = desc[1][-2:]
    endHour = desc[2][:-2]
    endMinute = desc[2][-2:]
    course["start"] = {"hour": startHour,
                        "minute": startMinute
                        }
    course["end"] = {"hour": endHour,
                        "minute": endMinute
                        }



    name = ""
    for chunk in desc[3:]:
        name += chunk + " "
    course["name"] = name

    daysString = desc[0]
    days = []
    for letter in daysString:
        days.append(dayLetters.index(letter.lower()))

    for day in days:
        week[day].append(course)
    

# sorting
for dayInd in range(5):
    day = week[dayInd]
    for i in range(len(day)):
        minVal = day[i]["start"]
        minInd = i
        for j in range(i, len(day)):
            if(day[j]["start"]["hour"] < minVal["hour"] or 
            (day[j]["start"]["hour"] == minVal["hour"] and day[j]["start"]["minute"] > minVal["minute"])):
                minInd = j
                minVal = day[j]["start"]
        temp = day[i]
        day[i] = day[minInd]
        day[minInd] = temp

# write it to a file
with open("output.json", "w") as text_file:
    JSONWeek = json.dumps(week)
    text_file.write(JSONWeek)
