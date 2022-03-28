from glob import glob
import os.path
import re

STUDY_PLANS_DIR = os.path.dirname(__file__)
LC_DIR = os.path.abspath(os.path.join(STUDY_PLANS_DIR, ".."))

SOLUTION_NUMBERS = set(
    os.path.basename(fn[:-3]) for fn in
    glob(os.path.join(LC_DIR, "numbered", "*.py"))
)


def get_plan_fns():
    return glob(os.path.join(STUDY_PLANS_DIR, "*.md"))


def get_problems(plan_fn):
    # returns Dict[prob_num, Tuple[title, topics]]
    with open(plan_fn) as fd:
        text = fd.read()
    split_problem = lambda x: (x[0], (x[1], x[2].split(", ")))
    prob_nums_descriptions = dict(map(split_problem, re.findall(r'([0-9]+)\. (.*)\nTopics: (.*)', text)))
    # prob_num: (title, topics)
    return prob_nums_descriptions


def print_plan_status(plan_fn, prob_nums_descriptions):
    plan_name = os.path.basename(plan_fn)[:-3]
    builder = []
    builder.append(plan_name)
    completed = total = 0
    for prob_num, (title, topics) in prob_nums_descriptions.items():
        total += 1
        if prob_num in SOLUTION_NUMBERS:
            completed += 1
            builder.append(f"  ✓  {prob_num:>5}. {title}")
        else:
            builder.append(f"  X  {prob_num:>5}. {title}")
        builder.append(f"            {', '.join(topics)}")
    builder.append(f"\nCOMPLETED  {completed} / {total}")
    builder.append("\n")
    print("\n".join(builder))
    return plan_name, completed, total


if __name__ == "__main__":
    summary = []
    plan_fns = get_plan_fns()
    for plan_fn in plan_fns:
        prob_nums_descriptions = get_problems(plan_fn)
        plan_name, completed, total = print_plan_status(plan_fn, prob_nums_descriptions)
        pct = round(completed/total*100)
        summary.append(f"{plan_name:<25}{completed:>6}/{total:<6}{pct:>8}%")
    print("\n".join(summary))
