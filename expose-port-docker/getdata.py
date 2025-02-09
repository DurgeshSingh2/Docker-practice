import pandas as pd
import numpy as np
import os
import sys
import pymupdf

from  flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    print("Hello World")
    app.run(host="0.0.0.0", port=5000, debug=True)
    