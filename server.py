import flask
from flask import request, jsonify
from functions import get_crypto_price_in_usd, get_fiat_price_is
from logger import _log_entry

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def crypt_to_fiat(crypt, fiat):
    crypto_price = get_crypto_price_in_usd(crypt)
    match fiat:
        case "USD":
            return crypto_price 
    return crypto_price * get_fiat_price_is("USD", fiat)

def crypto_to_crypto(from_crypt, to_crypt):
    fr = get_crypto_price_in_usd(from_crypt)
    to = get_crypto_price_in_usd(to_crypt)
    return fr/to

def fiat_to_crypto(fiat, crypto):
    return get_fiat_price_is(fiat, "USD") / get_crypto_price_in_usd(crypto)

@app.route('/exchange', methods=['GET'])
def home():
    from_c = request.args["from"]
    to_c = request.args["to"]

    if from_c in ["BTC", "ETH"]:
        if to_c in ["BTC", "ETH"]:
            _log_entry(from_c, to_c)
            return str(round(crypto_to_crypto(from_c, to_c),4))
        else:
            _log_entry(from_c, to_c)
            return str(round(crypt_to_fiat(from_c, to_c), 4))
    else:
        if to_c in ["BTC", "ETH"]:
            _log_entry(from_c, to_c)
            return str(round(fiat_to_crypto(from_c, to_c), 4))
        else:
            _log_entry(from_c, to_c)
            return str(round(get_fiat_price_is(from_c, to_c), 4))
        

app.run()