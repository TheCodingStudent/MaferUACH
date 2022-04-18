import json

def get_style():
    with open('style.json') as f:
        data = json.load(f)
    return data