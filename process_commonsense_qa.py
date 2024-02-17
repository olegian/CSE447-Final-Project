import pandas as pd
import datasets
import json
import pathlib
import random

DATA_FOLDER = pathlib.Path("./data/commonsense_qa/")
OUTPUT_FILE = "additional_qa.json"
INPUT_FILES  = "train-00000-of-00001.parquet"

df = pd.read_parquet(DATA_FOLDER / INPUT_FILES)

data = []
for idx, row in df.iterrows():
    new_point = {"id": row["id"], 
                 "question_stem": row["question"], 
                 "answerKey": row["answerKey"]}

    choices_list = list(row["choices"]["text"])

    if new_point["answerKey"] == "E":
        possible = ["A", "B", "C", "D"]
        new_answer = random.choice(possible)
        new_idx = possible.index(new_answer)

        new_point["answerKey"] = new_answer
        choices_list[new_idx] = choices_list[-1]

    choices_list.pop()
    choices_map = {"text": choices_list , "label" : ["A", "B", "C", "D"]}

    new_point["choices"] = choices_map
    data.append(new_point)

with open(DATA_FOLDER / OUTPUT_FILE, mode="w") as f:
    json.dump(data, f)

datasets.DatasetDict.from_json()

   
   