import json
import hashlib
from time import time

class Block:
    
    def __init__(self, nonce, previous_hash, block_num, transactions,timestamp=None):
        """
        Add a block of transactions to the blockchain
        """
        self.block_num = block_num
        if timestamp is None:
            self.timestamp = time()
        else:
            self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash

    def hash(self):
        """
        Create a SHA-256 hash of a block
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        block = {'block_num': self.block_num,
                'timestamp': self.timestamp,
                'transactions': self.transactions,
                'nonce': self.nonce,
                'previous_hash': self.previous_hash}
        return block
    