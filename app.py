from flask import Flask
from martsales.logger import logging
from martsales.exception import martsalesException
import sys
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("we are testing Exception")
        logging.info("exception test")
    except Exception as e:
        martsales=martsalesException(e,sys)
        logging.info(martsales.error_message)
        logging.info("this logging test")
    return "starting Machine learning"



if __name__ =="__main__":
    app.run(debug=True)