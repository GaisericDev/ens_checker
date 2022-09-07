import os
from tabnanny import check
from dotenv import load_dotenv
from web3 import Web3
from ens import ENS

from utils.name_to_addr import name_to_addr
from utils.get_balance import get_balance
from utils.get_ens_names import get_ens_names

load_dotenv()

INFURA_API_KEY = os.getenv("INFURA_API_KEY")
INFURA_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
PROVIDER = Web3.HTTPProvider(INFURA_URL)
WEB3 = Web3(PROVIDER)
NS = ENS(PROVIDER)
CWD = os.getcwd()

def main():
    # list with all ens names that are available, sorted alphabetically - ens names are not case sensitive so no need to remove capitals
    available = []
    # list with all unavaible ens names - can come in handy for filtering sets on future attempts as not to perform duplicate searches
    not_available = []
    # ens names set from i.e. txt file
    filter_options = {
        "use_filter": False,
        "filter_filepath": f"{CWD}/output/not_available.txt"
    }
    ens_names = get_ens_names(filter_options)
    # check if we can connect
    if(WEB3.isConnected()):
        print("connected")
        # loop through all ens names in the list 
        for name in ens_names:
            print(name)
            # get eth address
            # eth_address = name_to_addr(NS, name)
            # if address is available it will be a NoneType, add to list corresponding to availability
            # available.append(name) if eth_address == None else not_available.append(name)
    # # write list of available ens names to txt file
    # with open(f"{CWD}/output/available.txt", "w") as f:
    #     for item in available:
    #         f.write("%s\n" %item)
    # # write list of unavailable ens names to txt file
    # with open(f"{CWD}/output/not_available.txt", "w") as f:
    #     for item in not_available:
    #         f.write("%s\n" %item)
    
if __name__ == '__main__':
     main()

