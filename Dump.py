# python has inbult lib of json -- java script Object Notation

import json

# lets create a dictionary for key and value pair --  "myDict"

myDict = {
    "people": [
        {
            "name": "Bem", "age": "23", "hight": 5.6
        },

        {
            "name": "jony", "age": "44", "hight": 5.0
        },

        {
            "name": "Bobber", "age": "38", "hight": 53
        }
    ],

    "Unit":[
        {
            "BranchCode":2101,
            "Branch lead": 'Prasad Rao',
            "State":"Andhra pradesh"
        },

        {
            "BranchCode":12412,
            "Branch lead": 'Hindho',
            "State":"Uthara Knand"
        }
    ]

}


# import modules in json "LOADS" - to load data & "Dumps" -  dumping the data from program into Json file

json_string = json.dumps(myDict, indent= 4)    ## it convert "myDict" dictionary values in to string, spacing with 2

#File handling
#Dumping data into 'my_data.json' file

with open('my_data.json', 'w') as f:
    f.write(json_string)

print("Dumping json successful")

