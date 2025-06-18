import json

dict_data = {
    "name": "Ali",
    "age": 12
}

json_data = json.dumps(dict_data, indent=4)


f = open("output.json", 'w')
f.write(json_data)
f.close()

