
from block import Block


class Blockchain:
    def __init__(self, difficulty=2, mining_reward=10):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = difficulty
        self.mining_reward = mining_reward

        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        if not sender or not receiver:
            raise ValueError("Sender and receiver are required.")

        if sender == receiver:
            raise ValueError("Sender and receiver must differ.")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }

        self.pending_transactions.append(transaction)
        print("Transaction added:", transaction)

    def mine_pending_transactions(self, miner_address):
        if not miner_address:
            raise ValueError("Miner address is required.")

        reward_transaction = {
            "sender": "NETWORK",
            "receiver": miner_address,
            "amount": self.mining_reward
        }

        transactions = self.pending_transactions.copy()
        transactions.append(reward_transaction)

        new_block = Block(
            len(self.chain),
            transactions,
            self.get_latest_block().hash
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        # Clear transactions only after successful mining.
        self.pending_transactions.clear()

        print(f"Mining reward: {self.mining_reward} coins")
        return new_block

    def is_chain_valid(self):
        for index, block in enumerate(self.chain):
            # Detect changes to a block's contents.
            if block.hash != block.calculate_block_hash():
                return False

            # Verify proof-of-work.
            if not block.hash.startswith("0" * self.difficulty):
                return False

            if index > 0:
                previous_block = self.chain[index - 1]

                # Verify the link to the previous block.
                if block.previous_hash != previous_block.hash:
                    return False

                # Verify the sequence of block indexes.
                if block.index != previous_block.index + 1:
                    return False

        return True

    def display_chain(self):
        for block in self.chain:
            print("\n" + "=" * 50)
            print(f"Block Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}")

        print("\n" + "=" * 50)
        print("Total blocks:", len(self.chain))
        print("Pending transactions:", len(self.pending_transactions))
        print("Blockchain valid:", self.is_chain_valid())
