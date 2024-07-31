import json


# r - read mode
with open('my_data.json', 'r') as f:
    json_object = json.loads(f.read())  ## creating a object to load data and storing in 'json_object'
    f.read()
print(json_object)


# extracting data from json file to do operations

print(json_object['Unit'][0])


people = json_object['people'][1]['name']
age =  json_object['people'][1]['age']

print('person name:-', people)

print('person age:-',{age})



Branch = json_object['Unit'][1]

print(f"Branch Details:- {Branch}")