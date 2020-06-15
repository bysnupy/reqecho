from flask import *

echo = Flask(__name__)

from reqecho import views
import os

context_path = os.environment['CONTEXT_PATH']

