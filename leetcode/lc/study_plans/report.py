from glob import glob
import os
import os.path
import re

STUDY_PLANS_DIR = os.path.dirname(__file__)
LC_DIR = os.path.abspath(os.path.join(STUDY_PLANS_DIR, ".."))

SOLUTION_NUMBERS = set(
    os.path.basename(fn[:-3]) for fn in
    glob(os.path.join(LC_DIR, "numbered", "*.py"))
)


def cls():
    if os.getenv("PWD") is None:
        # cmd.exe or PS
        os.system('cls')
    else:
        # posix
        os.system('clear')


def get_plan_fns():
    return glob(os.path.join(STUDY_PLANS_DIR, "*.md"))


def get_problems(plan_fn):
    # returns Dict[prob_num, Tuple[title, topics, difficulty]]
    with open(plan_fn) as fd:
        text = fd.read()
    split_problem = lambda x: (x[0], (x[1], x[2].split(", "), x[3]))
    prob_nums_descriptions = dict(
        map(split_problem, re.findall(r'([0-9]+)\. (.*)\nTopics: (.*)\n(Easy|Medium|Hard)', text)))
    # prob_num: (title, topics, difficulty)
    return prob_nums_descriptions


def format_plan_status(plan_fn, prob_nums_descriptions, flag='incomplete'):  # flag='all'
    plan_name = os.path.basename(plan_fn)[:-3]
    builder = []
    builder.append(plan_name)
    completed = total = 0
    for prob_num, (title, topics, difficulty) in prob_nums_descriptions.items():
        total += 1
        if prob_num in SOLUTION_NUMBERS:
            completed += 1
            if flag == 'all':
                builder.append(f"  ✓  {prob_num:>5}. {title:<55} [{difficulty}]")
                builder.append(f"            {', '.join(topics)}")
        else:
            builder.append(f"  X  {prob_num:>5}. {title:<55} [{difficulty}]")
            builder.append(f"            {', '.join(topics)}")
    builder.append(f"\nCOMPLETED  {completed} / {total}")
    builder.append("\n")
    text = "\n".join(builder)
    return text, plan_name, completed, total


def main(flag='incomplete'):  # flag='all'
    cls()
    text_builder = []
    summary_builder = []
    plan_fns = get_plan_fns()
    for plan_fn in plan_fns:
        prob_nums_descriptions = get_problems(plan_fn)
        text, plan_name, completed, total = format_plan_status(plan_fn, prob_nums_descriptions, flag=flag)
        text_builder.append(text)
        pct = round(completed / total * 100)
        summary_builder.append(f"{plan_name:<25}{completed:>6}/{total:<6}{pct:>8}%")
    print("\n".join(text_builder))
    print("\n".join(summary_builder))
    print()


if __name__ == "__main__":
    import sys
    sys.exit(main())
