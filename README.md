# Blockchain
Blockchain from Scratch
This GitHub repository contains a comprehensive implementation of a blockchain and its client from scratch. The project showcases a blockchain system with essential functionalities and a user-friendly interface for interacting with it.

**Features**

-Blockchain
* Wallet Generation: Create blockchain wallets with a unique address, public key, and private key.
* Transaction Management: Send coins, generate transactions, and view all transactions on the blockchain.
* Node Management: Add multiple blockchain nodes and configure them.
* Conflict Resolution: Simple mechanisms to resolve conflicts between nodes.
* Transaction Confirmation: Confirm transactions by interacting with a blockchain node.
  
- Blockchain Client 
The client interface includes:
* The client interface includes:
1.	Wallet Generator
    * Generate Wallet: Create a new blockchain wallet with an address, public key, and private key.
2.	Make Transactions
    * Send Coins: Enter transaction details to generate and send a transaction.
4.	View Transactions
    * Check Transactions: Enter a blockchain node URL to view all transactions with filtering and search options.
5.	Blockchain Frontend
    * Mine: Interface for mining operations.
    * Configure: Manage blockchain node configurations

Screenshots
1.	Blockchain Client Interface
    * Buttons: Wallet Generator, Make Transactions, View Transactions
    


2.	Make Transactions
    * Fields: Sender Address, Sender Private Key, Recipient Address, Amount to Send
    * Button: Generate Transaction
    
![IMG-20240719-WA0014](https://github.com/user-attachments/assets/4374624f-1f81-44be-92b9-eb2dc5f5fc0e)

3.	Wallet Generator
   	* Button: Generate Wallet
    * Fields: Address, Public Key, Private Key

![IMG-20240719-WA0013](https://github.com/user-attachments/assets/564ffc3f-24a9-46f0-9c64-edba5e225897)

4.	View Transactions
    * Fields: Node URL
    * Button: View Transactions
    * Options: Show (dropdown 10 entries), Search Bar
    * Buttons: Resolve Conflict

![IMG-20240719-WA0010](https://github.com/user-attachments/assets/ebacc728-e6fe-4be8-93a4-29242fab08a5)

5.	Blockchain Frontend
    * Add Blockchain Nodes: Enter node URLs and add them to the list.

![IMG-20240719-WA0008](https://github.com/user-attachments/assets/c23b3712-7444-4b27-8068-89c65c5a5601)

   * Mining

![IMG-20240719-WA0015](https://github.com/user-attachments/assets/23b572b7-9a1d-4812-b1f3-1fde5701a17e)


   * Confirm Transaction: Enter transaction details and confirm.

![IMG-20240719-WA0007](https://github.com/user-attachments/assets/d8486ae1-0721-4e51-9cf6-1f4c94ca8718)

   * Choose recipient from list of wallets

![IMG-20240719-WA0006](https://github.com/user-attachments/assets/908d35dc-dc82-457d-894e-bb0e8c3fb29a)

**SETUP AND USAGE**

Create a Virtual Environment

•	Use the following command to create a new virtual environment

    *python -m venv venv
  
Install Requirements: 

•	Install the necessary packages by running

    *pip install -r requirements.txt

Run the Application

•	For the Blockchain Frontend, run

    *python app.py

•	For the Blockchain Client, run

    *python blockchain_client.py 
    
