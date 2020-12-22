import requests

# API from etherscan. Limit: 5 requests/sec
API = {YOUR API GOES HERE}  # Example: API = "7KAXFQ7Q6ZUAQZU9S9ITS2HKSXQXMV8VGE"

# 80/20 pool = 4x multiplier, 98/2 = 49
claim_multiplier = 4
noclaim_multiplier = 49

myDefiList = [
    {
        'name': 'Aave',
        'claim_pool': '0xb9efee79155b4bd6d06dd1a4c8babde306960bab',
        'noclaim_pool': '0x0490b8bc5898eac3e41857d560f0a58aa393321e',
        'claim_token': '0xd3866617f3ddc2953a969f831830b60f1603e14b',
        'noclaim_token': '0x568c928953f9ee4d3e804e916a4d2b6907fa33bd'
    },
    {
        'name': 'Augur',
        'claim_pool': '0x0077732357ac0f29e26ea629b79ab3b266ddb796',
        'noclaim_pool': '0x98ad8d1dfd7d4ac0850e24ff8fa8f41b69a60de0',
        'claim_token': '0xd85ca69e58e9367D72B04D5902b6fdbe39cA4cF1',
        'noclaim_token': '0x6AA0a667507e02bFE86182AD9f74f69299D1A27c'
    },
    {
        'name': 'Balancer',
        'claim_pool': '0x72a250ee19c0f8cc5772f9a33e1e330cde39e023',
        'noclaim_pool': '0x6c701226204f7937750671b041996a73180a47d6',
        'claim_token': '0x47788BD0b95Dd8e1A063843af731286c3904ec71',
        'noclaim_token': '0xE78C9Fe794e5f85906c574F7cfEb3647AD91cB87'
    },
    {
        'name': 'Barnbridge',
        'claim_pool': '0x533f1164facaf30bbe8cc5900fb4f505df3412f7',
        'noclaim_pool': '0xd9d5ed792a5d89cd73a0764ee263e4a5df2dd542',
        'claim_token': '0x9a3E9E7055a4552ae97C541242924D1E0c5588c9',
        'noclaim_token': '0x1B73F1e564C5c31E503efa8C0c50356876CC9614',
    },
    {
        'name': 'Corevault',
        'claim_pool': '0xa9d06f185f300c57fa54dc71678b225e4ce89407',
        'noclaim_pool': '0xf677ed557d321a225aed0f17e295146bb73a3c5b',
        'claim_token': '0x07AB6390bC4f105Dd2Ac24A7Cb1Dce9b3ec5c6AF',
        'noclaim_token': '0x352E4BBDDa1ed839ac07533ED9eebadC39a70963',
    },
    {
        'name': 'Cream',
        'claim_pool': '0x31c2507dfdbb7904201f28a7e18a70f2cb8cd03e',
        'noclaim_pool': '0xa36c6f854ef17238a6bdef7eec3b5af371006c16',
        'claim_token': '0xD82ac8d0fd8a5995C5fFd2B366999aB3D360A769',
        'noclaim_token': '0x8F843Ca7960575863beDb42d3CaFCf02c206fA8E',
    },
    {
        'name': 'Curve',
        'claim_pool': '0xdfe5ead7bd050eb74009e7717000eeadcf0f18db',
        'noclaim_pool': '0xd9b92e84b9f96267bf548cfe3a3ae21773872138',
        'claim_token': '0x2B8a2F0Bad1Ba4D72033B8475fB0CCC4921cb6Dc',
        'noclaim_token': '0x1F8Aa31E569Fcf22e21EB124Fdd46df1e990C36E',
    },
    {
        'name': 'Harvest',
        'claim_pool': '0x47c4a126bc45739c9087af3968c8e0d2354c5cf5',
        'noclaim_pool': '0x9a43e689dbe8f60ec12ba899d58b94a14d852e37',
        'claim_token': '0x7db8E29B9A107351A2255f5065A7405b49d95cAb',
        'noclaim_token': '0x0721211926c9b07a92D5E6D9043D0291b4B6364A',
    },
    {
        'name': 'Pickle',
        'claim_pool': '0xe7f5b65126dd3cfe341313d1e9fa5c6d8865c652',
        'noclaim_pool': '0x64dd4573297dd5ce7199a5d31a5be185e8d8c80d',
        'claim_token': '0x90cf010DaEA8f8E9F1e2300e4AFCADa0E2CC2E3F',
        'noclaim_token': '0x617758EC94e90Ef81431d6a209174fbc90FAB870',
    },
    {
        'name': 'Ren',
        'claim_pool': '0xd17c49ca3eaee2c935601a8ab432d3612279b788',
        'noclaim_pool': '0x33bc3abfabde8fceb0ced58e16184fb4cfc163ef',
        'claim_token': '0x4a6507c71393D9b55E654e6515494e26a2C982D3',
        'noclaim_token': '0x9c825d5Fdd376d32F8Cb44FD491522f7a32193de',
    },
    {
        'name': 'Sushi',
        'claim_pool': '0x3d910518d721a385fa8fc0ad95ad3de4255ba956',
        'noclaim_pool': '0xe093973b45d3ddfc7d789850ad5b5bbd6a59846f',
        'claim_token': '0x27d9C33D61b8a04c6c76270440A5B7CfeE06409E',
        'noclaim_token': '0xD8228f09105df9d8E22D3B445d115cfEfd49901d',
    },
    {
        'name': 'Yearn',
        'claim_pool': '0xaa6d172d0358b1612f1d99bb0d02c54949d2bcbc',
        'noclaim_pool': '0xf1469c0c8cde46466d6cbf0a1e0b03b98cbb301f',
        'claim_token': '0x95F2b40fD723Da8E2937776920EAB91aBF87aa54',
        'noclaim_token': '0x034655E8808f6dD8715CB2D58CfA94a15D6e1835',
    }
]

print("{:<12} {:<8} {:<8} {:<8}".format('Name', 'Claim', 'NoClaim', 'Total'))

def generate_url(claim_pool, noclaim_pool, claim_token, noclaim_token):
    # Get the balance of Claim token in the pool
    claim_cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={claim_token}&address={claim_pool}&tag=latest&apikey={API}"
    # Get the balance of Dai token in the pool
    claim_dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={claim_pool}&tag=latest&apikey={API}"

    noclaim_cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={noclaim_token}&address={noclaim_pool}&tag=latest&apikey={API}"
    noclaim_dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={noclaim_pool}&tag=latest&apikey={API}"

    return claim_cover_url, claim_dai_url, noclaim_cover_url, noclaim_dai_url


for defi in myDefiList:
    # Calls generate_url functio and assigns returned urls to variables
    claim_cover_url, claim_dai_url, noclaim_cover_url, noclaim_dai_url = generate_url(defi['claim_pool'], defi['noclaim_pool'], defi['claim_token'], defi['noclaim_token'])

    # Makes an API call and gets the pool's token balance from the blockchain
    claim_cover_balance = int(requests.get(claim_cover_url).json()["result"])
    claim_dai_balance = int(requests.get(claim_dai_url).json()["result"])

    # Calculates the token price using balances, rounds to 4 decimals
    claim_price = claim_dai_balance / claim_cover_balance * claim_multiplier

    noclaim_cover_balance = int(requests.get(noclaim_cover_url).json()["result"])
    noclaim_dai_balance = int(requests.get(noclaim_dai_url).json()["result"])

    noclaim_price = noclaim_dai_balance / noclaim_cover_balance * noclaim_multiplier

    # Calculates the total price. If total > 1 there is an opportunity
    total = claim_price + noclaim_price
    print("{:<12} {:<8} {:<8} {:<8}".format(defi['name'], "{:.3f}".format(claim_price), "{:.3f}".format(noclaim_price), "{:.3f}".format(total)))
