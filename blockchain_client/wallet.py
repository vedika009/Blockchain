from collections import OrderedDict
import binascii
import Crypto
from Crypto.Hash import SHA
import Crypto.Random
from Crypto.PublicKey import RSA
import uuid
from Crypto.Signature import PKCS1_v1_5


initial_balance = 50

class Wallet:
    
    def __init__(self, initial_val=None):
        random_gen = Crypto.Random.new().read
        self.address = str(uuid.uuid4())[0:8]
        self.private_key = RSA.generate(1024, random_gen)
        self.public_key =  self.private_key.publickey()
        self.initial_value = initial_balance

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({
        'private_key': binascii.hexlify(self.private_key.exportKey(format='DER')).decode('ascii'),
        'public_key': binascii.hexlify(self.public_key.exportKey(format='DER')).decode('ascii'),
        'address': self.address
    });