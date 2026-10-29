
from datetime import datetime, timezone
from utils import calculate_hash


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_block_hash()

    def calculate_block_hash(self):
        block_data = {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }

        return calculate_hash(block_data)

    def mine_block(self, difficulty):
        target = "0" * difficulty

        print(f"Mining block {self.index}...")

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_block_hash()

        print(f"Block mined! Hash: {self.hash}")
        print(f"Nonce: {self.nonce}")
