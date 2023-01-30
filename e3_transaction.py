from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

blockNumber = web3.eth.block_number
print(blockNumber)

account_1= "0x5779A2C700EAfad0Df3ee551C483A09e8Eaf8b84"
account_2= "0xBdaFC7960fb7187d5daA47Baee394274e1a4437B"
private_key="38ac5b36ebd4beda3f51f6676c48a24db81c1e8457efd04278c9130b7ec33479"

#send crytp currency from actn1 to acunt2

##STEPS
#get the nonce  
nonce = web3.eth.getTransactionCount(account_1)
#build transaction
n= 20
ts= {
    'nonce': nonce, #nonce prevents u from sending transaction twice on ethereum 
    'to': account_2,
    'value': web3.toWei(n,'ether'),
    'gas': 2000000, #units of gas but not ethereum #compensation/cryptocurrency for miners on blockchain network
    'gasPrice': web3.toWei('50', 'gwei')
}
#sign transaction
signed_ts = web3.eth.account.signTransaction(ts,private_key)
#send transaction
ts_hash = web3.eth.sendRawTransaction(signed_ts.rawTransaction)
#get transaction hash
print(ts_hash) #binary format
print(web3.toHex(ts_hash)) #Hex Format
