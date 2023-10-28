import json

def is_valid_json(my_string):
    try:
        json.loads(my_string)
        return True 
    except ValueError:
        return False
    
json_string = '{"name": "John", "age": 30, "cty": "New York"}'
if is_valid_json(json_string):
    print("Valid JSON object")
else:
    print("Not a valid JSON object")