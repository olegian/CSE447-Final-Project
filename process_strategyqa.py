import json
import pathlib

DATA_FOLDER = pathlib.Path("./data/strategy_qa/")
OUTPUT_FILE = "facts.txt"
INPUT_FILE  = "strategyqa_train.json"

data = []
with open(DATA_FOLDER / INPUT_FILE, encoding="utf-8", mode="r") as f:
    data = json.loads(f.read())

with open(DATA_FOLDER / OUTPUT_FILE, encoding="utf-8", mode="w") as f:
    for line in data:
        for fact in line["facts"]:
            f.write(f"{fact}\n")
