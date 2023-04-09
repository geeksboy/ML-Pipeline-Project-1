from flask import Flask
from visa.logger import logging
from visa.exception import CustomException
import os,sys
app = Flask(__name__)

@app.route('/', method=['GET',"POST"])
def index():
    try:
        raise Exception("We ")
    except Exception as e:
        visa = CustomException(e, sys)
        return "hello World"

if __name__=="__main__":
    app.run(debug=True)