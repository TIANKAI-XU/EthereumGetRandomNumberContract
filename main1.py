# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from web3 import Web3


def VRFv2Consumer():
    # 链接全节点
    web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/47af0aba2b874825bc193dee5c5c2d50'))

    # 获取智能合约和ABI地址
    contract_address = "0x4721891B98781edb6903F7c67d2B0b7B9f7E9147"
    contract_abi = [
        {
            "inputs": [],
            "name": "acceptOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint64",
                    "name": "subscriptionId",
                    "type": "uint64"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "have",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "want",
                    "type": "address"
                }
            ],
            "name": "OnlyCoordinatorCanFulfill",
            "type": "error"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferRequested",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "requestId",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256[]",
                    "name": "randomWords",
                    "type": "uint256[]"
                }
            ],
            "name": "rawFulfillRandomWords",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "requestId",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "uint256[]",
                    "name": "randomWords",
                    "type": "uint256[]"
                }
            ],
            "name": "RequestFulfilled",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "requestRandomWords",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "requestId",
                    "type": "uint256"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "requestId",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "uint32",
                    "name": "numWords",
                    "type": "uint32"
                }
            ],
            "name": "RequestSent",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_requestId",
                    "type": "uint256"
                }
            ],
            "name": "getRequestStatus",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "fulfilled",
                    "type": "bool"
                },
                {
                    "internalType": "uint256[]",
                    "name": "randomWords",
                    "type": "uint256[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "lastRequestId",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "requestIds",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "s_requests",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "fulfilled",
                    "type": "bool"
                },
                {
                    "internalType": "bool",
                    "name": "exists",
                    "type": "bool"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]

    # 使用Web3.py加载智能合约
    contract = web3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )


    # block_number = 5583261
    # block_number = 5580000
    # block_range = {"fromBlock": block_number, "toBlock": 'latest'}
    event_filter = contract.events.RequestSent.create_filter(fromBlock='latest')

    # 持续侦听，获取最新的
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)


# 订阅事件
def handle_event(event):
    print(event)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    VRFv2Consumer()
