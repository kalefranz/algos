if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "report":
        from lc.study_plans.report import main
        sys.exit(main())

    # from conda.common.serialize import json_dump
    # import os, json
    # print(json_dump(dict(os.environ)))

    sys.exit()
