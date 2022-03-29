import json
import os.path

from conda.common.serialize import json_dump, json_load
import requests

# curl -sSL https://leetcode.com/api/problems/algorithms/ | jq

# path = "https://leetcode.com/api/problems/algorithms/"
# resp = requests.get(path)
# d = resp.json()
# del d["stat_status_pairs"]  # huge data structure
# print(json_dump(d))


from ._local import LEETCODE_SESSION

from base64 import b64decode
# # print(b64decode(LEETCODE_SESSION[0]))
# print(json_dump(json_load(b64decode(LEETCODE_SESSION[1]))))
# # print(b64decode(LEETCODE_SESSION[2]))



def load_api_json():
    path = os.path.join(os.path.dirname(__file__), f"api_problems.json")
    try:
        with open(path) as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}

api_problems_algorithms = {  # without "stat_status_pairs"
  "ac_easy": 0,
  "ac_hard": 0,
  "ac_medium": 0,
  "category_slug": "algorithms",
  "frequency_high": 0,
  "frequency_mid": 0,
  "num_solved": 0,
  "num_total": 2008,
  "user_name": ""
}

data = load_api_json()
stat_status_pairs = data["stat_status_pairs"]  # huge data structure
# print(json_dump(stat_status_pairs))


stat_obj = """
      "frontend_question_id": 1,
      "question__article__slug": "two-sum",
      "question__title": "Two Sum",
      "question__title_slug": "two-sum",
      "question_id": 1,
"""  # partial
def summarize_problems():
    summaries = {}
    for d in stat_status_pairs:
        stat = d["stat"]
        k = stat["frontend_question_id"]
        v = {"title": stat["question__title"], "slug": stat["question__title_slug"]}
        summaries[int(k)] = v
    summaries = {k: summaries[k] for k in sorted(summaries)}
    return summaries


problems = summarize_problems()
# print(json_dump(problems))

prob_nums = list(problems)
# print(prob_nums)
print([
    diff for q in range(1, len(prob_nums)) if (diff := prob_nums[q] - prob_nums[q-1])
])
