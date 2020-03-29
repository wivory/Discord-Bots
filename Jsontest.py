import json





MessagesData = {
    "Sue_Perb#7867": 0,
    "nib9888#6180": 0,
    "Houfin#5305": 0,
    "Tom Law#4317": 0,
    "Daniel Hogg#1751": 0
    }

with open('data.json', 'w+') as fp:
    json.dump(MessagesData, fp)

with open('data.json', 'w+') as fp:
    json.dump(MessagesData, fp)


with open('data.json', "r") as fp:
    dataformessages = json.load(fp)
    print(dataformessages)

print(dataformessages["Tom Law#4317"])





