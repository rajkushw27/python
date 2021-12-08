import json
import requests

source = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(source.text)

todos = dict()

for index, todo in enumerate(data):
    todos[data[index]['title']] = data[index]['completed']

with open('todos_status.json', 'w') as f:
    json.dump(todos, f, indent=2)

# refer https://docs.python.org/3/library/json.html for json object to python object
# my_dict = {
#     "people": [
#         {
#             "Name": "Rajani",
#             "Age": 29,
#             "Weight": 79
#         },
#         {
#             "Name": "Riaz",
#             "Age": 27,
#             "Weight": 56
#         },
#         {
#             "Name": "Ankit",
#             "Age": 30,
#             "Weight": 89
#         },
#         {
#             "Name": "Riya",
#             "Age": 28,
#             "Weight": 55
#         }
#     ]
# }
#
# json_string = json.dumps(my_dict, indent=4)
# with open("json_update.txt", 'w') as f:
#     f.write(json_string)
