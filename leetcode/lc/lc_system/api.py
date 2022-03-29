import json
import os
import os.path

from conda.common.serialize import json_dump, json_load
import requests


# curl -sSL https://leetcode.com/api/problems/algorithms/ -v --cookie "LEETCODE_SESSION=" | jq '.stat_status_pairs[] | {status}'

# print(os.system("env | sort"))


# del d["stat_status_pairs"]  # huge data structure
# print(json_dump(d))


def get_api_response():
    from lc.lc_system._local import LEETCODE_SESSION
    path = "https://leetcode.com/api/problems/algorithms/"
    resp = requests.get(path, cookies={"LEETCODE_SESSION": LEETCODE_SESSION})
    d = resp.json()
    return d


def extract(prob_metadata):
    record = {
        "question_id": prob_metadata["stat"]["frontend_question_id"],
        "slug": prob_metadata["stat"]["question__title_slug"],
        "title": prob_metadata["stat"]["question__title"],
        "status": prob_metadata["status"] or "_",
    }
    return record["question_id"], record


def parse_api_response(resp: dict):
    top_level = resp.copy()
    problems_raw = top_level.pop("stat_status_pairs")

    """
    {'stat': {
      'question_id': 1,
      'question__article__live': True,
      'question__article__slug': 'two-sum',
      'question__article__has_video_solution': True,
      'question__title': 'Two Sum',
      'question__title_slug': 'two-sum',
      'question__hide': False,
      'total_acs': 6270372,
      'total_submitted': 12952806,
      'frontend_question_id': 1,
      'is_new_question': False
    },
    'status': 'ac',
    'difficulty': {'level': 1},
    'paid_only': False,
    'is_favor': False,
    'frequency': 6.505639487084667,
    'progress': 100.0
    }
    {'stat': {
      'question_id': 2249,
      'question__article__live': None,
      'question__article__slug': None,
      'question__article__has_video_solution': None,
      'question__title': 'Count the Hidden Sequences',
      'question__title_slug': 'count-the-hidden-sequences',
      'question__hide': False,
      'total_acs': 11053,
      'total_submitted': 31529,
      'frontend_question_id': 2145,
      'is_new_question': False
    },
    'status': None,
    'difficulty': {'level': 2},
    'paid_only': False,
    'is_favor': False,
    'frequency': 2.3718362814078016,
    'progress': 36.45815735895747
    }
    """

    # k = stat["frontend_question_id"]
    # v = {"title": stat["question__title"], "slug": stat["question__title_slug"]}

    records = dict(extract(prob) for prob in problems_raw)
    return records


def format_records(records):
    builder = [
        "{question_id:>5}. {slug:30} {status:>5}".format(**rec)  # also have {title}
        for rec in records.values()
    ]
    return "\n".join(builder)

print(format_records(parse_api_response(get_api_response())))










from base64 import b64decode
# # print(b64decode(LEETCODE_SESSION.split('.')[0]))
# print(json_dump(json_load(b64decode(LEETCODE_SESSION.split('.')[1]))))
# # print(b64decode(LEETCODE_SESSION.split('.')[2]))



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
# print([
#     diff for q in range(1, len(prob_nums)) if (diff := prob_nums[q] - prob_nums[q-1])
# ])
