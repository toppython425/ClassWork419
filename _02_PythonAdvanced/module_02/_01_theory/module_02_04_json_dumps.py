import json


def make_json_string(data):
    json_string = json.dumps(obj=data, ensure_ascii=False, indent=4)
    return json_string


data_to_json = {'Name': 'Alice', 'Age': 30, 'Навыки': ['Python', 'Data Analysis']}

if __name__ == '__main__':
    result = make_json_string(data_to_json)
    print(result)
    print(type(result))
