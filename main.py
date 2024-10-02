# main.py
from threading import Thread
from file_handler import read_file, write_file
from transaction_manager import begin_transaction, commit_transaction, rollback_transaction

def perform_operations(transaction_id, filename):
    begin_transaction(transaction_id)
    try:
        write_file(filename, f"Data from {transaction_id}\n")
        read_file(filename)
        commit_transaction(transaction_id)
    except Exception as e:
        print(f"Error in transaction {transaction_id}: {e}")
        rollback_transaction(transaction_id)

if __name__ == "__main__":
    threads = []
    filename = 'data.txt'
    
    # Create threads for transactions
    for i in range(5):
        t = Thread(target=perform_operations, args=(f"tx_{i}", filename))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
