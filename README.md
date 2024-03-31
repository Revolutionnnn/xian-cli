# Xian Wallet CLI

This command-line interface (CLI) allows you to interact with the Xian blockchain and manage wallet information.

### Run xian-cli:
```bash
pipx install xian-cli
```

## Requirements

- Python 3.9 or newer
- Xian Python library (`xian-py`)
- Typer library (`typer`)
- Questionary library (`questionary`)

## Installation

### Install the required libraries:
```bash
pip install xian-py typer questionary
```

## Available Commands:

### Wallet Commands:

- **create**: Creates a new wallet and saves its information in a CSV file.
```bash
wallet create
```
- **import**: Imports a private key and saves it as a wallet.
```bash
wallet create <private key>
```
- **balance**: Retrieves the balance of a wallet or a specific address.
```bash
wallet balance
```
```bash
wallet balance --address <address>
```
- **delete**: Deletes a single wallet or all wallets.
```bash
wallet delete
```
```bash
wallet delete --all
```

### Send Commands:
- **simple**: Send xians.
```bash
send simple <amount> <address>
```
- **token**: Send tokens on xian blockchain.
```bash
send token <amount> <contract> <address> <stamp: optional>
```
- **advance**: Made a advance trasaction.
```bash
send token <contract> <function> <stamp: optional>
Then the kwargs will be required from the transaction.
```

### Contract Commands:
- **approve**: Aprove the contract.
```bash
contract aprove <contract>
```
- **get_approve**: Get aprove the contract.
```bash
contract get-aprove <contract>
```
- **submit**: Submit smart contract.
```bash
contract submit <contract_name>
Then it will be necessary to place the file path where the smart contract is located.
```

## Tasks to be Completed

- [x] Create wallet
- [x] Import wallet with private key
- [x] Create CSV with wallets
- [x] Verify balance of wallets in the CSV
- [x] Verify balance with an address
- [x] Delete wallets from the CSV
- [x] Delete all information from the CSV
- [x] Perform transaction from Xian CLI
- [x] Create advanced transaction to send any token
- [x] Interact with contracts
- [x] Load smart contract using CLI
- [ ] Create template to create tokens and NFTs using CLI (pending)
- [ ] Create simple games with CLI (pending)
- [ ] Create connection with node to verify information (pending)

Many more ideas to be implemented

## Additional Notes

- The CLI interacts with the Xian testnet by default.
- Wallet information is stored in a CSV file (ensure proper security for sensitive data).

Feel free to contribute to this project!
