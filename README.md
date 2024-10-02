
# Concurrent File Access with Transaction Management

## Introduction
This project demonstrates the concepts of both **Operating Systems (OS)** and **Database Management Systems (DBMS)** using Python and MySQL. It simulates a real-world scenario where multiple users access the same file concurrently, while ensuring data consistency and transaction management. The project handles concurrent file access using threading and locking mechanisms, and manages transaction logging in a MySQL database with ACID (Atomicity, Consistency, Isolation, Durability) properties.

## Features
- **Concurrent File Access**: Multiple threads can read from and write to the same file using Python's threading module and locking mechanisms to ensure mutual exclusion.
- **Transaction Management**: Each file operation is treated as a transaction, logged in MySQL, and follows ACID properties.
- **Deadlock Prevention**: Includes a timeout mechanism to prevent deadlocks during concurrent file access.
- **Logging**: Transaction logs are maintained both in a MySQL database and in local log files for easy tracking.
- **Error Handling**: Includes rollback mechanisms for failed transactions.

## Project Structure
```
concurrent_file_access/
├── mysql_connector.py      # MySQL connection and transaction logging
├── file_handler.py             # File read/write with concurrency control
├── transaction_manager.py      # Transaction management (BEGIN, COMMIT, ROLLBACK)
├── main.py                     # Main script to simulate and test the system
├── logs/
│   └── transaction_logs.txt    # Log file to store transaction statuses
├── .env                        # Environment variables (ignored in Git)
├── .gitignore                  # Specifies files and folders to be ignored by Git
└── README.md                   # Project documentation
```

## Technologies Used
- **Python**: Core programming language for handling file operations and concurrency.
- **MySQL**: Database used for transaction logging and maintaining ACID properties.
- **Threading**: Python’s threading module to simulate concurrent file access.
- **Locking Mechanisms**: Used for mutual exclusion in concurrent file operations.
- **Logging**: Python's logging module for tracking transactions locally and in MySQL.
  
## Installation and Setup

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- MySQL

### Steps to Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omsaivasireddy/Concurrent-File-Access-Transaction-Management.git
   cd Concurrent-File-Access-Transaction-Management
   ```

2. **Install Python dependencies**:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up MySQL**:
   - Create a MySQL database and table for logging transactions.
   - Update the `.env` file with your MySQL credentials.

   **Example MySQL setup**:
   ```sql
   CREATE DATABASE file_transaction_db;
   USE file_transaction_db;

   CREATE TABLE transaction_log (
     id INT AUTO_INCREMENT PRIMARY KEY,
     transaction_id VARCHAR(255) NOT NULL,
     status ENUM('BEGIN', 'COMMIT', 'ROLLBACK') NOT NULL,
     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory and add your MySQL credentials:

   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=file_transaction_db
   ```

5. **Run the Project**:
   To start testing concurrent file access and transactions, run the `main.py` file:

   ```bash
   python main.py
   ```

## How it Works

### 1. **Concurrent File Access**:
   - Threads are spawned in the `main.py` script to perform simultaneous read and write operations on a shared file (`data.txt`).
   - A lock is used to ensure only one thread can modify the file at any given time.

### 2. **Transaction Management**:
   - Each file operation (read/write) is treated as a transaction with the following steps:
     - `BEGIN`: Start of the transaction.
     - `COMMIT`: Successful completion of the transaction, changes are written to the file.
     - `ROLLBACK`: If an error occurs, the transaction is aborted, and no changes are made to the file.
   - The transaction’s status is logged both in the MySQL database and the log file (`logs/transaction_logs.txt`).

### 3. **Deadlock Prevention**:
   - A timeout mechanism is implemented to prevent deadlocks. If a thread cannot acquire a lock within a specified time, it aborts the transaction and rolls back any changes.

## Usage

This project can be used to simulate and learn about:
- **Concurrency**: Handling simultaneous file access in multi-threaded environments.
- **Transaction Management**: Ensuring ACID properties in file and database operations.
- **Deadlock Prevention**: Implementing strategies to avoid deadlocks in concurrent systems.

### Sample Output
Upon running the system, the output will display the transaction status for each thread, like so:

```bash
Transaction tx_1 started.
Transaction tx_1 committed.
Transaction tx_2 started.
Transaction tx_2 could not acquire lock, aborting.
```

Logs and database entries will reflect these operations.

## Future Enhancements
- **Asynchronous I/O**: Use `asyncio` to improve the performance of file access and transaction logging.
- **Batch Transactions**: Implement batch processing for logging multiple transactions at once to reduce overhead.
- **Enhanced Error Handling**: Add more sophisticated error handling and retry mechanisms for failed transactions.
  
## Contributing
Feel free to open issues or submit pull requests for any improvements or features you would like to see in this project.

## License
This project is licensed under the None.

---

This README will provide a clear and structured overview of your project on GitHub. Let me know if you need any changes or additions!