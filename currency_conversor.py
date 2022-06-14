from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
app = Flask(__name__, static_folder='static/')

# Needed functions and data structures for the currecy converter
currencies = {
    'USD': 1,
    'CRC': 691.54,
    'JPY': 134.42,
    'EUR': 0.95,
    'GBP': 0.81,
    'MXN': 19.98,
    'VEF': 5.25
}


def convert_currency(initial: str = 'USD', amount: float = 1.0, final: str = 'USD'):
    return amount / currencies[initial] * currencies[final]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert():
    args = request.args

    # result = thread.Thread(target = converter.convert_currency, args = (args.get('from', default='USD', type=str), args.get('amount', default=1, type=float), args.get('to', default='CRC', type=str)), daemon = True)
    # result.start()

    return {'result': convert_currency(args.get('from', default='USD', type=str), args.get('amount', default=1, type=float), args.get('to', default='CRC', type=str))}
    # return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)