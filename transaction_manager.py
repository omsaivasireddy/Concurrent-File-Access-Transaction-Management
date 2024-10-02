# transaction_manager.py
import logging
from mysql_connector import log_transaction

# Configure logging
logging.basicConfig(filename='logs/transaction_logs.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def begin_transaction(transaction_id):
    log_transaction(transaction_id, "BEGIN")
    logging.info(f"Transaction {transaction_id} started.")
    print(f"Transaction {transaction_id} started.")

def commit_transaction(transaction_id):
    log_transaction(transaction_id, "COMMIT")
    logging.info(f"Transaction {transaction_id} committed.")
    print(f"Transaction {transaction_id} committed.")

def rollback_transaction(transaction_id):
    log_transaction(transaction_id, "ROLLBACK")
    logging.info(f"Transaction {transaction_id} rolled back.")
    print(f"Transaction {transaction_id} rolled back.")
