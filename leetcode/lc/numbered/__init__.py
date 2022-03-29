import json
import os.path

HERE = os.path.dirname(__file__)


def load_json(problem_number):
    path = os.path.join(HERE, f"{problem_number}.json")
    try:
        with open(path) as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}
