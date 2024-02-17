import datasets
import json

INPUT_FILE = "./data/commonsense_qa/additional_qa.json"

json_file = None

with open(INPUT_FILE, mode='r') as f:
    json_file = json.load(f)

dataset = datasets.DatasetDict.from_json(INPUT_FILE)
