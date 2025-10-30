import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    {
      "name": "Илона"
    }
  ],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}
"""
parsed_data = json.loads(json_data)

print(parsed_data)

data = {
    "name": "Мария",
    "age": 30,
    "is_student": False,
}

json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data_ = json.load(file)
    print(data_)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)