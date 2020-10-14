import json

class scheduleFormatter:
    dayLetters = ["m", "t", "w", "r", "f"]
    def __init__(self, fileName):
        self.fileName = fileName
        
    def makeOutput(self):
        week = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: []
        }
        f = open(self.fileName)
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
                days.append(self.dayLetters.index(letter.lower()))

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
