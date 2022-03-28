from glob import glob
import os.path
import sys

LC = os.path.join(os.path.dirname(__file__), "lc")

def add_main():
    end_lines = """\

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

"""
    numbered_dir = os.path.join(LC, "numbered")
    ignore = {"__init__.py"}
    for pyfile in os.listdir(numbered_dir):
        if not pyfile[-3:] == ".py":
            continue
        if pyfile in ignore:
            continue
        if not pyfile[:-3].isdigit():
            continue
        with open(os.path.join(numbered_dir, pyfile), encoding='utf-8') as fd:
            text = fd.read()
        if "__main__" not in text:
            with open(os.path.join(numbered_dir, pyfile), "a") as fd:
                fd.write(end_lines)
            print(f"added __main__ to {pyfile}")
            # sys.exit()

add_main()
