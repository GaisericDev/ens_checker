import os
from dotenv import load_dotenv
from web3 import Web3
from ens import ENS

load_dotenv()

INFURA_API_KEY = os.getenv("INFURA_API_KEY")
infura_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
provider = Web3.HTTPProvider(infura_url)
web3 = Web3(provider)
ns = ENS(provider)
ens_name = "elonmusk.eth"

if(web3.isConnected()):
    print("connected")
    eth_address = ns.address(ens_name)
    print("eth address:", eth_address)
    balance = web3.eth.getBalance(eth_address)
    print("balance:", web3.fromWei(balance, "ether"))
else:
    print("connection error")

