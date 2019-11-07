import json
from web3 import Web3
from solcx import compile_standard


with open('vote.sol', 'r') as fichier:
    ficVal = fichier.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "Vote.sol": {
                "content": ficVal
            }
        },
        "settings":
            {
                "outputSelection": {
                    "*": {
                        "*": [
                            "metadata", "evm.bytecode"
                            , "evm.bytecode.sourceMap"
                        ]
                    }
                }
            }
    }
)

# web3 = Web3(Web3.EthereumTesterProvider())
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

web3.eth.defaultAccount = web3.eth.accounts[0]

bytecode = compiled_sol['contracts']['Vote.sol']['Vote']['evm']['bytecode']['object']

abi = json.loads(compiled_sol['contracts']['Vote.sol']['Vote']['metadata'])['output']['abi']

Vote = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Vote.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

vote = web3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi
)

print(vote.functions.helloWorld().call())