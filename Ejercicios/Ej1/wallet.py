# Point 1: generate a testnet wallet and show its seed and 2 receiving addresses.
import os
from cryptos import Bitcoin, entropy_to_words

words = entropy_to_words(os.urandom(16))
wallet = Bitcoin(testnet=True).wallet(words)
print("seed:", words)
print("addr1:", wallet.new_receiving_address())
print("addr2:", wallet.new_receiving_address())
