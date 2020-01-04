import requests

# we can get a list of all NASA astronauts who are in space currently from this request:
people_in_space = requests.get("http://api.open-notify.org/astros.json")
# convert response to native python json datatype
people_json = people_in_space.json()
# print(people_json)

# excessive nesting in order to clean data format
for key in people_json:
    if type(people_json[key]) is list:
        print(key)
        for elements in people_json[key]:
            for index in elements:
                print(index + ":", elements[index])
            print("---")
    else:
        print(key + ":", str(people_json[key]) + "\n---")
