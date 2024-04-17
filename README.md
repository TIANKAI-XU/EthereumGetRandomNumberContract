# EthereumGetRandomNumberContract
Get random number on chain through ChainLink, and listen to events released by the contract.

## Deploy and Run
The contracts/VRFv2Consumer.sol should be deployed to Ethereum Sepolia so as to get two random numbers offchain.

And main1.py can be runed to listen to events releaded by the contract. It can listen events after the contract is deployed. Remeber to modify the full node address first.
