# Point 3: show the balance of both addresses.
# Usage: python balance.py "<seed words>"
import sys
from cryptos import Bitcoin

coin = Bitcoin(testnet=True)
wallet = coin.wallet(sys.argv[1])
for addr in (wallet.new_receiving_address(), wallet.new_receiving_address()):
    print(addr, coin.get_balance(addr))
