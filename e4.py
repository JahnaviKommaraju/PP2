#build a smart contract -> instead of setting up truffle project we use remix
import json
from web3 import Web3


ganache_url = "HTTP://127.0.0.1:7545"

web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())


# get json from contract after compiling in compiler section 
  # cmpilation details -> web3Deploy 
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

address = web3.toChecksumAddress('0x4e99CecBcc260D547742646A76035597fD230973')

contract  = web3.eth.contract(address=address, abi=abi)

old_greet=contract.functions.greet().call()
print(old_greet)

# to send a transaction
web3.eth.defaultAccount = web3.eth.accounts[0]  # transaction is being sent to this account
ts_hash=contract.functions.setGreeting("Hiiii helloooo").transact()

web3.eth.waitForTransactionReceipt(ts_hash)  #wait until transaction is done
print(ts_hash) #binary format

print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))