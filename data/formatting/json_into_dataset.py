import datasets
import json

INPUT_FILE = "./data/commonsense_qa/additional_qa.json"
dataset = datasets.DatasetDict.from_json(INPUT_FILE)
