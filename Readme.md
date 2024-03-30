
Here's a README.md file in English for the given code:

Xian Wallet CLI
This command-line interface (CLI) allows you to interact with the Xian blockchain and manage wallet information.

Requirements
Python 3.7 or newer
Xian Python library (xian-py)
Typer library (typer)
Questionary library (questionary)
Installation
Install the required libraries:
Bash
pip install xian-py typer questionary
Usa el código con precaución.
Usage
Run the CLI:
Bash
python main.py
Usa el código con precaución.
Choose a command:
Available commands:

wallet          Manage wallets
send            Send Xian transactions
Wallet Commands:

create: Creates a new wallet and saves its information in a CSV file.
import: Imports a private key and saves it as a wallet.
balance: Retrieves the balance of a wallet or a specific address.
delete: Deletes a single wallet or all wallets.
Send Commands:

simple: Sends Xian transactions within the currency contract.
Additional Notes
The CLI interacts with the Xian testnet by default.
Wallet information is stored in a CSV file (ensure proper security for sensitive data).
Contributions
Feel free to contribute to this project!