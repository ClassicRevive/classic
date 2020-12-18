import requests

# we can get a list of all NASA astronauts who are in space currently from this request:
people_in_space = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vTUJm6c76_ihFZRt9WBYpCR6fF7w7C2duKLMvc0xPaSzSuSFcF5V-TUI0zE9dTQ5Tw_iNIQoUr04hu1/pubhtml?gid=0&single=true").json
# convert response to native python json datatype
# print(people_json)

print(people_in_space)
