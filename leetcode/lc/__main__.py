if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "report":
        from lc.study_plans.report import main
        sys.exit(main())

    if len(sys.argv) >= 2 and sys.argv[1].isnumeric():
        from importlib import import_module
        p = import_module(f"lc.numbered.{sys.argv[1]}")
        sys.exit(p.test())


    sys.exit()
