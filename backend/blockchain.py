from collections import OrderedDict
import requests
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from helper import *
from block import Block

class Blockchain:
    
    def __init__(self):
        
        self.transactions = []
        self.chain = [ Block(0, '00',1,[]) ] #genesis block
        self.nodes = set()
        #Generate random number to be used as node_id
        self.node_id = str(uuid4()).replace('-', '')


    def register_node(self, node_url):
        """
        Add a new node to the list of nodes
        """
        #Checking node_url has valid format
        parsed_url = urlparse(node_url)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def submit_transaction(self, sender_address, recipient_address, value, signature,balance):
        """
        Add a transaction to transactions array if the signature verified
        """
        if balance is None:
            balance = initial_balance
        transaction = OrderedDict({'sender_address': sender_address, 
                                    'sender_balance': balance,
                                    'recipient_address': recipient_address,
                                    'value': value})

        #Reward for mining a block
        if sender_address == MINING_SENDER:
            self.transactions.append(transaction)
            return len(self.chain) + 1
        #Manages transactions from wallet to another wallet
        else:
            transaction_verification = verify_transaction_signature(sender_address, signature, transaction)
            if transaction_verification:
                transaction['sender_balance'] = transaction['sender_balance'] - int(value)
                self.transactions.append(transaction)
                return len(self.chain) + 1
            else:
                return False


    def create_block(self, nonce, previous_hash):
        """
        Add a block of transactions to the blockchain
        """
        block = Block(nonce,previous_hash,len(self.chain)+1,self.transactions)
        self.transactions = []

        self.chain.append(block)
        return block

    def proof_of_work(self):
        """
        Proof of work algorithm
        """
        last_block = self.chain[-1]
        last_hash = last_block.hash()

        nonce = 0
        while valid_proof(self.transactions, last_hash, nonce) is False:
            nonce += 1

        return nonce

    def resolve_conflicts(self):
        """
        Resolve conflicts between blockchain's nodes
        by replacing our chain with the longest one in the network.
        """
        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            print('http://' + node + '/chain')
            response = requests.get('http://' + node + '/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and valid_chain(chain):
                    max_length = length
                    new_chain = [Block(block['nonce'], block['previous_hash'],
                                block['block_num'], block['transactions'],block['timestamp']) for block in chain]

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
