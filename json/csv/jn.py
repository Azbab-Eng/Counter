import json

people = {
    "first":[
        {"name":"babalola"},
        {"age":24},
        {"status":"single"},
        {"gender":"male"},
        {"edu":True}
    ],
    "second":[
        {"name":"abdulazeez"},
        {"age":34},
        {"status":"married"},
        {"gender":"male"},
        {"edu":False}
    ],
    "third":[
        {"name":"tope"},
        {"age":29},
        {"status":"single"},
        {"gender":"female"},
        {"edu":True}
    ]
}

json_file = json.dumps(people, indent=2)
# print(people["first"])
for list in people["first"]:
    print(list[name])