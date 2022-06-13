from app import app
from flask import request
from flask import url_for
from flask import render_template
from logic import *
import concurrent.futures
import threading as thread

  
@app.route('/convert', methods=['GET'])
def convert():
    args = request.args
    
    # result = thread.Thread(target = converter.convert_currency, args = (args.get('from', default='USD', type=str), args.get('amount', default=1, type=float), args.get('to', default='CRC', type=str)), daemon = True)
    # result.start()

    return {'result': converter.convert_currency(args.get('from', default='USD', type=str), args.get('amount', default=1, type=float), args.get('to', default='CRC', type=str))}
    # return {'result': result}
