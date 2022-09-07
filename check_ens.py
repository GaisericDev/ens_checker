import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

INFURA_API_KEY = os.getenv("INFURA_API_KEY")
infura_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
web3 = Web3(Web3.HTTPProvider(infura_url))
test_address = "elonmusk.eth"

print("isConnected:", web3.isConnected())

balance = web3.eth.getBalance(test_address)
print("balance:", web3.fromWei(balance, "ether"))

