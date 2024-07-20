from collections import OrderedDict
import binascii
import hashlib
import json
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

MINING_SENDER = "BLOCKCHAIN MINING REWARD"
MINING_REWARD = 1
MINING_DIFFICULTY = 2
initial_balance = 100

def find_balance(blockchain, public_key):
    if blockchain is None or len(blockchain.chain) == 1:
        return initial_balance
    
    balance = 0
    flag = 0

    for blocks in blockchain.chain[::-1]:
        for transaction in blocks.transactions:
            if transaction['sender_address'] == public_key:
                balance = int(transaction['sender_balance'])
                flag = 1
                break
            elif transaction['recipient_address'] == public_key:
                balance += int(transaction['amount'])
                flag = 1
    
    if flag == 0:
        return initial_balance
    return balance

def verify_transaction_signature(sender_address, signature, transaction):
    """
    Check that the provided signature corresponds to transaction
    signed by the public key (sender_address)
    """
    public_key = RSA.importKey(binascii.unhexlify(sender_address))
    verifier = PKCS1_v1_5.new(public_key)
    h = SHA.new(str(transaction).encode('utf8'))
    return verifier.verify(h, binascii.unhexlify(signature))

def valid_proof(transactions, last_hash, nonce, difficulty=MINING_DIFFICULTY):
    """
    Check if a hash value satisfies the mining conditions. This function is used within the proof_of_work function.
    """
    guess = (str(transactions)+str(last_hash)+str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == '0'*difficulty

def hash(last_block):
    """
    Create a SHA-256 hash of a block
    """
    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(last_block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def valid_chain(chain):
    """
    check if a bockchain is valid
    """
    last_block = chain[0]
    current_index = 1

    while current_index < len(chain):
        block = chain[current_index]
        #print(last_block)
        #print(block)
        #print("\n-----------\n")
        # Check that the hash of the block is correct
        if block['previous_hash'] != hash(last_block):
            return False

        # Check that the Proof of Work is correct
        #Delete the reward transaction
        transactions = block['transactions'][:-1]
        # Need to make sure that the dictionary is ordered. Otherwise we'll get a different hash
        transaction_elements = ['sender_address', 'recipient_address', 'value']
        transactions = [OrderedDict((k, transaction[k]) for k in transaction_elements) for transaction in transactions]

        if not valid_proof(transactions, block['previous_hash'], block['nonce'], MINING_DIFFICULTY):
            return False

        last_block = block
        current_index += 1

    return True
