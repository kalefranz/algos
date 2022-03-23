"""
/leetcode/server.py

"""

import time
import traceback
from threading import Thread

import io_wrapper
import log
import pdb_wrapper
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


console = None
pdb = None


def frame_data():
    global console

    frame_data = console.get_frame_data()

    # Ugly sleep due to internal race conditions
    while not frame_data:
        time.sleep(0.05)
        frame_data = console.get_frame_data()

    frame_data.pop("dirname", None)
    frame_data.pop("file_listing", None)
    frame_data.pop("globals", None)

    exception = frame_data.pop("exception", None)
    if exception:
        log.error(exception)

    return frame_data


def run_debugger():
    global pdb

    from user_code.prog_joined import _driver

    pdb.debug()
    _driver()


@app.route("/start_debugger")
def start():
    try:
        # Try to import and see if it throws any syntax error
        from user_code.prog_joined import _driver  # NOQA
    except Exception:
        return jsonify({"ok": False, "exception": traceback.format_exc()})

    global console
    global pdb

    io_wrapper.override_input()
    std_out_wrapper = io_wrapper.get_stdout_wrapper()
    pdb = pdb_wrapper.get_pdb_instance(
        stdout=std_out_wrapper, stderr=std_out_wrapper
    )
    console = pdb.get_console()

    thread = Thread(target=run_debugger)
    thread.daemon = True
    thread.start()
    return jsonify({"ok": True})


@app.route("/run_command")
def run_command():
    command = request.args.get("command")
    console.send_pdb_command(command)
    return jsonify(frame_data())


@app.route("/add_expression")
def add_expression():
    expression = request.args.get("expression")
    pdb.add_expression(expression)
    return jsonify(frame_data())


@app.route("/remove_expression")
def remove_expression():
    expression = request.args.get("expression")
    pdb.remove_expression(expression)
    return jsonify(frame_data())


def main():
    app.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
