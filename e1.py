#smart contracts- prgrms that run on blkchain
# it is publicly accesible to everyone on blkchain
# it's more like a microservice n looks like a class
# 

import json
from web3 import Web3
infura_url= "https://mainnet.infura.io/v3/262cdcdd779247d28b35bb2b7bf854a8"
web3= Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)