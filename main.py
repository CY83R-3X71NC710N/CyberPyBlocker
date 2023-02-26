
#!/usr/bin/env python
# CY83R-3X71NC710N © 2023

# CyberPyBlocker is a lightweight encrypted blockchain framework with Python for secure data storage using cryptography.
# It utilizes libs such as cryptography, scrypt, hashlib to secure data.

# Importing necessary libraries
import hashlib
import cryptography
import scrypt

# Defining a class for the blockchain
class BlockChain:
    # Initializing the blockchain
    def __init__(self):
        self.chain = []
        self.current_data = []
    
    # Function to add data to the blockchain
    def add_data(self, data):
        self.current_data.append(data)
    
    # Function to create a new block
    def create_block(self):
        # Hashing the data
        hash_data = hashlib.sha256(str(self.current_data).encode())
        # Encrypting the data
        encrypted_data = cryptography.fernet.Fernet(hash_data).encrypt(str(self.current_data).encode())
        # Generating a random key
        key = scrypt.random_string(length=32)
        # Creating a new block
        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'data': self.current_data,
            'hash': hash_data.hexdigest(),
            'encrypted_data': encrypted_data,
            'key': key
        }
        # Resetting the current data
        self.current_data = []
        # Adding the block to the chain
        self.chain.append(block)
        return block
    
    # Function to get the previous block
    def get_previous_block(self):
        return self.chain[-1]
    
    # Function to check if the blockchain is valid
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block['hash'] != previous_block['hash']:
                return False
        return True
