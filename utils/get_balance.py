def get_balance(WEB3, addr):
    return WEB3.eth.getBalance(addr)