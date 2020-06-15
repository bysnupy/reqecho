from reqecho import echo
from flask import *
import time
import os

context_path = os.environ['CONTEXT_PATH']
if not context_path:
    context_path = '/'


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
            return 'OK',200
        except:
            return test_post
