
from blockchain import Blockchain


def main():
    # Create a blockchain with mining difficulty 2.
    my_blockchain = Blockchain(
        difficulty=2,
        mining_reward=10
    )

    print("\n--- ADD TRANSACTIONS ---")

    my_blockchain.add_transaction(
        "Alice", "Bob", 10
    )

    my_blockchain.add_transaction(
        "Bob", "Charlie", 5
    )

    print("\n--- MINE BLOCK ---")

    my_blockchain.mine_pending_transactions(
        "Miner_1"
    )

    print("\n--- DISPLAY BLOCKCHAIN ---")
    my_blockchain.display_chain()

    print("\n--- TEST BLOCKCHAIN VALIDITY ---")
    print("Valid:", my_blockchain.is_chain_valid())

    print("\n--- SIMULATE TAMPERING ---")

    # Change transaction data in block 1.
    my_blockchain.chain[1].transactions[0]["amount"] = 1000

    print("Valid after tampering:",
          my_blockchain.is_chain_valid())

    print("\n--- RESTORE ORIGINAL TRANSACTION ---")

    my_blockchain.chain[1].transactions[0]["amount"] = 10

    print("Valid after restoration:",
          my_blockchain.is_chain_valid())


if __name__ == "__main__":
    main()
