import csv
import os
from constants import WALLETS_FILE
import typer

from rich.progress import track
import time

def load_wallets():
    """Loads wallet data from the CSV file into a dictionary."""
    wallets = {}
    if os.path.exists(WALLETS_FILE):
        with open(WALLETS_FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                name, address, private_key = row
                wallets[name] = {"address": address, "private_key": private_key}
    return wallets

def save_wallet_to_csv(name: str, address: str, privkey: str):
    """Saves wallet data to the CSV file."""
    with open(WALLETS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, address, privkey])


def save_wallets(wallets):
    """Save the wallet data in the CSV file"""

    with open(WALLETS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for name, data in wallets.items():
            address = data['address']
            privkey = data['private_key']
            writer.writerow([name, address, privkey])


def delete_wallet_by_name(name: str):
    """Deletes a wallet with the specified name from the CSV file."""
    wallets = load_wallets()

    del wallets[name]
    typer.echo(f"Wallet deleted successfully.")
    save_wallets(wallets)

def delete_all_wallets():
    """Deletes all wallet data from the CSV file."""
    if os.path.exists(WALLETS_FILE):
        os.remove(WALLETS_FILE)
        typer.echo(f"All wallets deleted successfully.")
    else:
        typer.echo(f"Wallets file does not exist.")

def validate_wallet (wallet_name):
    wallets = load_wallets()
    if wallet_name in wallets:
        typer.echo(f"Wallet with name '{wallet_name}' already exists.", err=True)
        return True
    

def format_transaction_info(transaction_info):
    formatted_info = ""
    tx_result = transaction_info.get("result", {})
    stamps_used = tx_result.get("tx_result", {}).get("data", "").get("stamps_used", "")
    result = tx_result.get("tx_result", {}).get("data", "").get("result", "")
    
    formatted_info += f"Stamps Used: {stamps_used}\n"
    formatted_info += f"Result: {result}\n"
    
    return formatted_info

def fake_progress():
    total = 0
    for _ in track(range(100), description="Processing..."):
        time.sleep(0.01)
        total += 1
    typer.echo(f"Processed {total}%.")