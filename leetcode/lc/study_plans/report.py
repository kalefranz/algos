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
    with open(plan_fn) as fd:
        text = fd.read()
    prob_nums_descriptions = dict(re.findall(r'([0-9]+)\. (.*)\n', text))

    return prob_nums_descriptions


def print_plan_status(plan_fn, prob_nums_descriptions):
    plan_name = os.path.basename(plan_fn)[:-3]
    builder = []
    builder.append(plan_name)
    for prob_num, prob_desc in sorted(prob_nums_descriptions.items()):
        if prob_num in SOLUTION_NUMBERS:
            builder.append(f"  ✓  {prob_num:>5}. {prob_desc}")
        else:
            builder.append(f"  X  {prob_num:>5}. {prob_desc}")
    builder.append("\n\n")
    print("\n".join(builder))


if __name__ == "__main__":
    plan_fns = get_plan_fns()
    for plan_fn in plan_fns:
        prob_nums_descriptions = get_problems(plan_fn)
        print_plan_status(plan_fn, prob_nums_descriptions)
