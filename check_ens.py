import os
import time
from dotenv import load_dotenv
from web3 import Web3
from ens import ENS
from english_words import english_words_set

from utils.get_ens_names import get_ens_names
from utils.get_owner_of_name import get_owner_of_name

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
        "use_filter": True
        ,"filter_filepath": f"{CWD}/output/not_available.txt"
        ,"name_list": english_words_set
    }
    ens_names = get_ens_names(filter_options)
    # check if we can connect
    if(WEB3.isConnected()):
        print("connected")
        # loop through all ens names in the list 
        for index in range(10):
            name = ens_names[index]
            try:
                # add .eth to the name
                name += ".eth"
                # get eth address
                eth_address = get_owner_of_name(NS, name)
                # remove .eth from name
                name = name.replace(".eth", "")
                # if address is not claimed it will be "0x0000000000000000000000000000000000000000"
                not_claimed = "0x0000000000000000000000000000000000000000"
                available.append(name) if eth_address == not_claimed else not_available.append(name)
                time.sleep(1)
            except Exception as e:
                print(e)
                # if there is an error i.e. reached api limit then we just exit the loop and write all our collected data to file
                break
    # write list of available ens names to txt file
    with open(f"{CWD}/output/available.txt", "w") as f:
        for item in available:
            f.write("%s\n" %item)
    # write list of unavailable ens names to txt file
    with open(f"{CWD}/output/not_available.txt", "a") as f:
        for item in not_available:
            f.write("%s\n" %item)
    
if __name__ == '__main__':
     main()

