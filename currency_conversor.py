from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from threading import Lock
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

# Global variables inter-trhead
mutex = Lock()
thread_id = 0


def log_into_file(initial: str = 'USD', amount: float = 1.0, final: str = 'USD'):
    global mutex
    with mutex:
        with open('log.txt', 'a') as logfile:
            global thread_id
            thread_id = thread_id + 1
            logfile.write(
                f'Thread #{thread_id} logged: Someone requested currency conversion from {initial} {amount} to {final}\n')

def convert_currency(initial: str = 'USD', amount: float = 1.0, final: str = 'USD'):
    return amount / currencies[initial] * currencies[final]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/convert', methods=['GET'])
def convert():
    args = request.args
    initial_currency = args.get('from', default='USD', type=str)
    amount_to_convert = args.get('amount', default=1, type=float)
    final_currency = args.get('to', default='CRC', type=str)

    log_into_file(initial_currency, amount_to_convert, final_currency)

    return {'result': convert_currency(initial_currency, amount_to_convert, final_currency)}


if __name__ == '__main__':
    app.run(debug=True)
