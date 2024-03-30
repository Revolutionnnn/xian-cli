
# BLOCKCHAIN
from xian_py.wallet import Wallet
from xian_py.xian import Xian
from xian_py.transactions import get_nonce, create_tx, broadcast_tx

# LOCAL FILES
from utils import delete_all_wallets, delete_wallet_by_name, fake_progress, format_transaction_info, validate_wallet, load_wallets, save_wallet_to_csv
from constants import TESNET_ID, TESNET_CHAIN

#CLI
import typer
import questionary
from rich.progress import track



app = typer.Typer()
wallet_app = typer.Typer()
send_app = typer.Typer()
contract_app = typer.Typer()

app.add_typer(wallet_app, name="wallet")
app.add_typer(send_app, name="send")
app.add_typer(contract_app, name="contract")

@wallet_app.command("create")
def create ():
    """
    Creates a new wallet and saves its information on csv.
    """
    wallet_name = typer.prompt("What's your name wallet?")

    if validate_wallet(wallet_name):
        return

    wallet = Wallet()
    address = wallet.public_key
    privkey = wallet.private_key
    save_wallet_to_csv(wallet_name, address, privkey)
    typer.echo(f"Wallet created and saved.")
    typer.echo(f"Wallet name '{wallet_name}' information:")
    typer.echo(f" Public address: {address}")
    typer.echo(f" Private key address: {privkey}")


@wallet_app.command("import")
def import_key ():
    """
    Imports a private key and associates it with a wallet name, then saves the wallet information.
    """
    wallet_name = typer.prompt("What's your name wallet?")
    if validate_wallet(wallet_name):
        return

    private_key = typer.prompt("What's your private key?")

    wallet = Wallet(private_key)
    address = wallet.public_key
    privkey = wallet.private_key
    save_wallet_to_csv(wallet_name, address, privkey)
    typer.echo(f"Wallet imported and saved sucessfull.")
    typer.echo(f"Wallet name '{wallet_name}' information:")
    typer.echo(f" Public address: {address}")
    typer.echo(f" Private key address: {privkey}")


@wallet_app.command("balance")
def balance (address: bool = False):
    """
    Retrieves the balance of a wallet address or selected wallet and displays it.

    If '--address', prompts the user to input an address to retrieve its balance.
    Otherwise, prompts the user to select a wallet from the loaded wallets and retrieves its balance.
    """
    if address:
        address_wallet = typer.prompt("What's the address do you wanna get the balance?")
    else:
        wallets = load_wallets()
        selected_wallet = questionary.select("What wallet do you want to get the balance?", choices=list(wallets.keys())).ask()
        address_wallet = wallets[selected_wallet]["address"]

    xian = Xian(TESNET_CHAIN, TESNET_ID)
    balance = xian.get_balance(address_wallet)
    typer.echo(f"  Balance: {balance}")
    typer.echo(f"  Address: {address_wallet}")


@wallet_app.command("delete")
def delete (all: bool = False):
    """
    Deletes a single wallet or all wallets, based on user input.

    If '--all, prompts the user for confirmation before deleting all wallets.
    """
    if all:
        response = questionary.confirm("Are you sure of delete the wallets?").ask()
        if response:
            delete_all_wallets()
    else:
        wallets = load_wallets()
        selected_wallet = questionary.select("What wallet do you want to delete?", choices=list(wallets.keys())).ask()
        response = questionary.confirm(f"Are you sure of delete the wallet {selected_wallet}?").ask()
        if response:
            delete_wallet_by_name(selected_wallet)

@send_app.command()
def simple(amount: int, to: str):
    wallets = load_wallets()
    selected_wallet = questionary.select("What wallet do you want to use?", choices=list(wallets.keys())).ask()
    wallet_priv = wallets[selected_wallet]["private_key"]
    wallet = Wallet(wallet_priv)
    
    xian = Xian(TESNET_CHAIN, TESNET_ID, wallet)
    send = xian.send_tx(
        contract='currency',
        function='transfer',
        kwargs={
            'to': to,
            'amount': amount,
        }
    )
    formatted_transaction_info = format_transaction_info(xian.get_tx(send["tx_hash"]))
    typer.echo(f'success: {send["success"]}')
    typer.echo(f'tx_hash: {send["tx_hash"]}')
    typer.echo(f"{formatted_transaction_info}")

@send_app.command()
def advance(amount: int, contract: str, to: str, stamps: int = 500):
    wallets = load_wallets()
    selected_wallet = questionary.select("What wallet do you want to use?", choices=list(wallets.keys())).ask()
    wallet_priv = wallets[selected_wallet]["private_key"]
    wallet = Wallet(wallet_priv)
    
    xian = Xian(TESNET_CHAIN, TESNET_ID, wallet)
    send = xian.send_tx(
        contract=contract,
        function='transfer',
        kwargs={
            'to': to,
            'amount': amount,
        },
        stamps=stamps,
    )
    formatted_transaction_info = format_transaction_info(xian.get_tx(send["tx_hash"]))
    typer.echo(f'success: {send["success"]}')
    typer.echo(f'tx_hash: {send["tx_hash"]}')
    typer.echo(f"{formatted_transaction_info}")

@contract_app.command()
def approve(contract: str):
    wallets = load_wallets()
    selected_wallet = questionary.select("What wallet do you want to use?", choices=list(wallets.keys())).ask()
    wallet_priv = wallets[selected_wallet]["private_key"]
    wallet = Wallet(wallet_priv)
    xian = Xian(TESNET_CHAIN, TESNET_ID, wallet)
    approve = xian.approve(contract)

    typer.echo(f'success: {approve["success"]}')
    typer.echo(f'tx_hash: {approve["tx_hash"]}')

@contract_app.command()
def get_approve(contract: str):
    wallets = load_wallets()
    selected_wallet = questionary.select("What wallet do you want to use?", choices=list(wallets.keys())).ask()
    wallet_priv = wallets[selected_wallet]["private_key"]
    wallet = Wallet(wallet_priv)
    xian = Xian(TESNET_CHAIN, TESNET_ID, wallet)
    approved = xian.get_approved_amount(contract)

    typer.echo(f'approved: {approved}')

@contract_app.command()
def submit(contract_name: str):
    wallets = load_wallets()
    selected_wallet = questionary.select("What wallet do you want to use?", choices=list(wallets.keys())).ask()
    path = questionary.path("What's the path to the contract file?").ask()
    code = ""
    
    with open(path, "r") as file:
        code = file.read()

    wallet_priv = wallets[selected_wallet]["private_key"]
    wallet = Wallet(wallet_priv)
    xian = Xian(TESNET_CHAIN, TESNET_ID, wallet)

    submit = xian.submit_contract(contract_name, code)
    formatted_transaction_info = format_transaction_info(xian.get_tx(submit["tx_hash"]))
    fake_progress()
    typer.echo(f'success: {submit["success"]}')
    typer.echo(f'tx_hash: {submit["tx_hash"]}')
    typer.echo(f"{formatted_transaction_info}")

if __name__ == "__main__":
    app()
