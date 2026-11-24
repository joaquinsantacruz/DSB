# Point 2: restore the wallet from the seed and send sat from addr1 to addr2.
# Usage: python send.py "<seed words>"
import sys
from cryptos import Bitcoin

# The spec asks for 20 sat, but nodes reject it ("dust, tx with dust output must be 0-fee").
# 546 sat is the dust limit for P2PKH outputs.
AMOUNT = 546

coin = Bitcoin(testnet=True)
wallet = coin.wallet(sys.argv[1])
addr1, addr2 = wallet.new_receiving_address(), wallet.new_receiving_address()
# The lib returns a txid even if the broadcast is rejected: check it on an explorer.
print(coin.send(wallet.privkey(addr1), addr1, addr2, AMOUNT))
