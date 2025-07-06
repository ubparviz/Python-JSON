import json


with open("students.json", "r") as inputfile:
    students = json.load(inputfile)

sorted_by_score = sorted(students, key= lambda student: student['score'], reverse=True)

with open("rating.json", "w") as outputfile:

    for index, student in enumerate(sorted_by_score, start=1):
        student["rank"] = index

    json.dump(sorted_by_score, outputfile, indent=4)
