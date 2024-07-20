from collections import OrderedDict
import binascii
import time
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Transaction:
    
    def __init__(self, sender_address, sender_private_key, recipient_address, value, sender_balance=None):
        self.timestamp = time.time()
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value
        self.sender_balance = sender_balance

    def to_dict(self):
        return OrderedDict({
                            'sender_address': self.sender_address,
                            'sender_balance': self.sender_balance,
                            'recipient_address': self.recipient_address,
                            'value': self.value})

    def sign_transaction(self):
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')