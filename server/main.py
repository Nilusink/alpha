import json


data = json.load(open("questions.json", "r"))

data = [
    {"question": "In welche klasse gehe ich?", "type": 0, "answer": ["4AHEL", "4BHEL", "4AHBT", "4AHET"]}
]

message = json.dumps(data[0])
