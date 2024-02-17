import json
import pathlib

DATA_FOLDER = pathlib.Path("./data/strategy_qa/")
OUTPUT_FILE = "facts.txt"
INPUT_FILES  = ["strategyqa_train.json"]

data = []
for filename in INPUT_FILES:
    with open(DATA_FOLDER / filename, encoding="utf-8", mode="r") as f:
        data = json.loads(f.read())

with open(DATA_FOLDER / OUTPUT_FILE, encoding="utf-8", mode="w") as f:
    for line in data:
        for fact in line["facts"]:
            f.write(f"{fact}\n")
