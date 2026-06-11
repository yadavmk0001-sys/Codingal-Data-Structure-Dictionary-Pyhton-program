student_data = {
    "id1" : {"name": "Sara", "class" : "V"},
    "id2" : {"name": "Zoya", "class": "V"},
    "id3" : {"name": "Sara", "class" : "V"},
    "id4" : {"name": "Aparna", "class" : "VII"},
}

result = {}
seen = []

for student_id, details in student_data.items():
    unique = (details["name"], details["class"])

    if unique not in seen:
        seen.append(unique)
        result[student_id] = details

for k, v in result.items():
    print(k, " : ", v)