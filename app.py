from flask import Flask
from credit.logger import logging
from credit.exception import creditException
import sys
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("we are testing Exception")
        logging.info("exception test")
    except Exception as e:
        credit=creditException(e,sys)
        logging.info(credit.error_message)
        logging.info("this logging test1")
        return "starting Machine learning"



if __name__ =="__main__":
    app.run(debug=True)