from reqecho import echo
from flask import *
import time
import os

context_path = '/'
if os.environ['CONTEXT_PATH']:
    context_path = os.environ['CONTEXT_PATH']

@echo.route(context_path, methods=['POST','GET'])
def list_header():
    print("context path:" + context_path)
    timeout = time.time() + 20
    test_post = """
        <form action="/" method="POST">
        Post Test: <input name="num"></input>
        </form>"""
    while True:
        if time.time() < timeout:
            break
        else:
            return 'TIMEOUT',500
    print(request.headers)
    print("-"*20)
    print(request.cookies)
    if request.method == "GET":
        return test_post
    else:
        try:
            resp = flask.make_response("OK")
            resp.set_cookie("appside_cookie", "hello")
            return 'resp
        except:
            return test_post
