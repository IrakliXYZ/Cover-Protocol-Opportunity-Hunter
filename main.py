import requests

# API from etherscan. Limit: 5 requests/sec
API = "7KAXFQ7Q6ZUAQZU9S9ITS2HKSXQXMV8VGE"

# 80/20 pool = 4x multiplier, 98/2 = 49
claim_multiplier = 4
noclaim_multiplier = 49

def claim(claim_token, claim_pool):
    # Get the balance of Claim token in the pool
    cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={claim_token}&address={claim_pool}&tag=latest&apikey={API}"

    cover_balance = int(
        requests.get(cover_url).json()["result"])

    # Get the balance of Dai token in the pool
    dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={claim_pool}&tag=latest&apikey={API}"

    dai_balance = int(
        requests.get(dai_url).json()["result"])

    return round(dai_balance / cover_balance * claim_multiplier, 4)


def noclaim(noclaim_token, noclaim_pool):
    # Get the balance of NoClaim token in the pool
    cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={noclaim_token}&address={noclaim_pool}&tag=latest&apikey={API}"

    cover_balance = int(
        requests.get(cover_url).json()["result"])

    # Get the balance of Dai token in the pool
    dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={noclaim_pool}&tag=latest&apikey={API}"

    dai_balance = int(
        requests.get(dai_url).json()["result"])

    # Testing only
    # print("dai:", dai_balance, "     cover:", cover_balance, "   dai_balance / cover_balance =", dai_balance / cover_balance)

    return round(dai_balance / cover_balance * noclaim_multiplier, 4)


def aave():
    return claim("0xd3866617f3ddc2953a969f831830b60f1603e14b", "0xb9efee79155b4bd6d06dd1a4c8babde306960bab") + noclaim("0x568c928953f9ee4d3e804e916a4d2b6907fa33bd", "0x0490b8bc5898eac3e41857d560f0a58aa393321e")

print(aave())