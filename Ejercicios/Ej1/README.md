# Ej1: Bitcoin Testnet wallet

Three scripts using [pybitcointools](https://github.com/primal100/pybitcointools) (`cryptos` on PyPI) on Bitcoin **testnet3**.

| Script | Assignment point | What it does |
|--------|------------------|--------------|
| `wallet.py` | 1 | Generates a seed phrase and prints 2 receiving addresses |
| `send.py` | 2 | Restores the wallet from the seed and sends 546 sat from address 1 to address 2 |
| `balance.py` | 3 | Restores the wallet from the seed and prints the balance of both addresses |

## Setup

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/pip install -r Ejercicios/Ej1/requirements.txt
```

If your global pip config points to a private index, add `--index-url https://pypi.org/simple`.

## Run

All commands run from the repository root.

1. Generate the wallet and write down the seed:

   ```bash
   .venv/bin/python Ejercicios/Ej1/wallet.py
   ```

2. Request test coins for `addr1` from a **testnet3** faucet, e.g. [coinfaucet.eu](https://coinfaucet.eu/en/btc-testnet/). Testnet4 faucets (e.g. bitcoinfaucet.uo1.net) accept the same address format, but `cryptos` only talks to testnet3 servers, so those coins never show up.

3. Wait until the coins appear (`unconfirmed` or `confirmed` above 0):

   ```bash
   .venv/bin/python Ejercicios/Ej1/balance.py "<seed words>"
   ```

4. Send from address 1 to address 2. It prints the txid:

   ```bash
   .venv/bin/python Ejercicios/Ej1/send.py "<seed words>"
   ```

5. Once the transaction confirms, check both balances again with `balance.py`.

The same seed always restores the same two addresses, in the same order.

## Notes

- **546 sat instead of 20.** The assignment asks for 20 sat, but nodes reject it with `dust, tx with dust output must be 0-fee`. 546 sat is the dust limit for these legacy (P2PKH) addresses.
- **A printed txid doesn't mean the transaction went through.** `cryptos` prints a txid even when the network rejects the transaction. Check it on an explorer: `https://mempool.space/testnet/tx/<txid>`.
- **Timeouts.** `cryptos` connects to a random server from its built-in list, and some are offline. If a script fails with `TimeoutError`, run it again.
