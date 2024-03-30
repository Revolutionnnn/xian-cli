# Xian Wallet CLI

This command-line interface (CLI) allows you to interact with the Xian blockchain and manage wallet information.

## Requirements

- Python 3.7 or newer
- Xian Python library (`xian-py`)
- Typer library (`typer`)
- Questionary library (`questionary`)

## Installation

### Install the required libraries:
pip install xian-py typer questionary

## Available Commands:

### Wallet Commands:

- **create**: Creates a new wallet and saves its information in a CSV file.
- **import**: Imports a private key and saves it as a wallet.
- **balance**: Retrieves the balance of a wallet or a specific address.
- **delete**: Deletes a single wallet or all wallets.

### Send Commands:

- **simple**: Sends Xian transactions within the currency contract.

## Additional Notes

- The CLI interacts with the Xian testnet by default.
- Wallet information is stored in a CSV file (ensure proper security for sensitive data).

Feel free to contribute to this project!
