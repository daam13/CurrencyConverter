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
