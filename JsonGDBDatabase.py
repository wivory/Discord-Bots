import json

with open("data2.json", "r")as fp:
    gdbdata = json.load(fp)
    print(gdbdata)
    print(gdbdata)
    print(gdbdata)
    print(gdbdata)
with open("data2.json", "w") as fp:
    gdbdata["conversationstage"] = 1
    json.dump(gdbdata, fp)
    print(gdbdata)
    
