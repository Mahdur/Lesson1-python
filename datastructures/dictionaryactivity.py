student_data = {
"id1": {'name': 'Mahdur', 'class': 8, 'Age': 14 },
"id2": {"name": "Sara", "class": "V", "Age": 15},
"id3": {"name": "David", "class": "V", "Age": 13},
"id4": {"name": "Surya", "class": "V", "Age": 14},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["Age"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)


country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : ' 00977'}

print("Country code for India -")
print(country_code.get('India', 'Not Found'))