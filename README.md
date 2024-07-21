# Blockchain from Scratch

This GitHub repository contains a comprehensive implementation of a blockchain and its client from scratch. The project showcases a blockchain system with essential functionalities and a user-friendly interface for interacting with it.

## Features

### Blockchain

- **Wallet Generation:** Create blockchain wallets with a unique address, public key, and private key.
- **Transaction Management:** Send coins, generate transactions, and view all transactions on the blockchain.
- **Node Management:** Add multiple blockchain nodes and configure them.
- **Conflict Resolution:** Simple mechanisms to resolve conflicts between nodes.
- **Transaction Confirmation:** Confirm transactions by interacting with a blockchain node.

### Blockchain Client

The client interface includes:

- **Wallet Generator**
  - **Generate Wallet:** Create a new blockchain wallet with an address, public key, and private key.
  
- **Make Transactions**
  - **Send Coins:** Enter transaction details to generate and send a transaction.
  
- **View Transactions**
  - **Check Transactions:** Enter a blockchain node URL to view all transactions with filtering and search options.
  
### Blockchain Frontend

- **Mine:** Interface for mining operations.
- **Configure:** Manage blockchain node configurations.

## Screenshots

### Blockchain Client Interface

- **Buttons:** Wallet Generator, Make Transactions, View Transactions

### Make Transactions

- **Fields:** Sender Address, Sender Private Key, Recipient Address, Amount to Send
- **Button:** Generate Transaction

![IMG-20240719-WA0014](https://github.com/user-attachments/assets/396435b3-5902-410f-99fa-71fa9cd026e6)

### Wallet Generator

- **Button:** Generate Wallet
- **Fields:** Address, Public Key, Private Key

![IMG-20240719-WA0013](https://github.com/user-attachments/assets/38e11a7d-064c-4a4c-9497-311e3b2fd8b5)


### View Transactions

- **Fields:** Node URL
- **Button:** View Transactions
- **Options:** Show (dropdown 10 entries), Search Bar
- **Buttons:** Resolve Conflict

![IMG-20240719-WA0010](https://github.com/user-attachments/assets/27b3afe9-588c-4c30-a43f-00656d357a98)

### Blockchain Frontend

- **Add Blockchain Nodes:** Enter node URLs and add them to the list.

![IMG-20240719-WA0008](https://github.com/user-attachments/assets/44c17b34-2ae4-408f-8ccc-49550a03dce8)

### Mining

![IMG-20240719-WA0015](https://github.com/user-attachments/assets/c1c34680-f649-4b38-9381-36bc506fe6b5)

- **Confirm Transaction:** Enter transaction details and confirm.

![IMG-20240719-WA0007](https://github.com/user-attachments/assets/8794ec47-ed55-45e6-8064-fd2768408bb3)

- **Choose recipient from list of wallets**

![IMG-20240719-WA0006](https://github.com/user-attachments/assets/09d1dc67-2cdb-4507-9a8a-8cc3a7eb8fc4)

## Setup and Usage

### Create a Virtual Environment

Use the following command to create a new virtual environment:

```bash
python -m venv venv
```

### Install Requirements

Install the necessary packages by running:

```bash
pip install -r requirements.txt
```

### Run the Application

- For the Blockchain Frontend, run:

  ```bash
  python app.py
  ```

- For the Blockchain Client, run:

  ```bash
  python blockchain_client.py
  ```

---
