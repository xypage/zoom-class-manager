#filler for all days of week
week = [[],[],[],[],[]]

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
    desc = contents[i]
    link = "\"" + contents[i + 1] + "\""
    desc = desc.split(" ")
    print(link)
    
    daysString = desc[0]
    days = []
    for letter in daysString:
        days.append(dayLetters.index(letter.lower()))


    startHour = desc[1][:-2]
    startMinute = desc[1][-2:]
    endHour = desc[2][:-2]
    endMinute = desc[2][-2:]
    times = [[int(startHour), int(startMinute)], [int(endHour), int(endMinute)]]

    
    name = "\""
    for chunk in desc[3:]:
        name += chunk + " "
    name += "\""
    for day in days:
        week[day].append([times, link, name])
    

# sorting
for day in week:
    for i in range(len(day)):
        minVal = day[i][0][0]
        minInd = i
        for j in range(i, len(day)):
            if(day[j][0][0] < minVal):
                minInd = j
                minVal = day[j][0][0]
        temp = day[i]
        day[i] = day[minInd]
        day[minInd] = temp

# write it to a file
with open("output.txt", "w") as text_file:
    text_file.write("[")
    for dayInd in range(5):
        text_file.write("[")
        dayLen = len(week[dayInd])
        for classInd in range(dayLen):
            curr = week[dayInd][classInd]
            text_file.write(f"[[[{curr[0][0][0]},{curr[0][0][1]}],[{curr[0][1][0]},{curr[0][1][1]}]],{curr[1]},{curr[2]}]")
            
            # If it's last class, don't put comma after closing bracket
            if(classInd != dayLen - 1):
                text_file.write(",")
            else:
                text_file.write("")
                
        # If it's the last day, don't put comma after closing bracket
        if(dayInd != 4):
            text_file.write("],")
        else:
            text_file.write("]]")
