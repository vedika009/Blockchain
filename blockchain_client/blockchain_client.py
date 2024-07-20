from flask import Flask, jsonify, request, render_template
from wallet import *
from transaction import Transaction
import requests

wallet_list = [Wallet()]

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/make/transaction')
def make_transaction():
    wallet_list_json = [x.to_dict() for x in wallet_list]
    return render_template('make_transaction.html', wallet_list = wallet_list_json)

@app.route('/view/transactions')
def view_transaction():
    return render_template('./view_transactions.html')

@app.route('/wallet/new', methods=['GET'])
def new_wallet():
    wallet = Wallet()
    wallet_list.append(wallet)
    return jsonify(wallet.to_dict()), 200

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
    sender_address = request.form['sender_address']
    sender_private_key = request.form['sender_private_key']
    recipient_address = request.form['recipient_address']
    value = request.form['amount']
    balance = initial_balance
    res = requests.get('http://127.0.0.1:5000' + '/balance/' + sender_address)

    if res.status_code == 200:
        balance = res.json()['sender_balance']
    print(res.json())

    transaction = Transaction(sender_address, sender_private_key, recipient_address, value, balance)

    response = {
        'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()
    }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port,debug=True)