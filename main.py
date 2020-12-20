import requests

# API from etherscan. Limit: 5 requests/sec
API = "7KAXFQ7Q6ZUAQZU9S9ITS2HKSXQXMV8VGE"

def aave():
  # 80/20 pool = 4x multiplier, 98/2 = 49
  claim_multiplier = 4
  noclaim_multiplier = 49

  # Here are the addresses for pools and tokens. (Dai token address isn't here because it's same for all pools
  claim_pool = "0xb9efee79155b4bd6d06dd1a4c8babde306960bab"
  noclaim_pool = "0x0490b8bc5898eac3e41857d560f0a58aa393321e"
  claim_token = "0xd3866617f3ddc2953a969f831830b60f1603e14b"
  noclaim_token = "0x568c928953f9ee4d3e804e916a4d2b6907fa33bd"

  def claim():
      # Get the balance of Claim token in the pool
      cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={claim_token}&address={claim_pool}&tag=latest&apikey={API}"

      cover_balance = int(
          requests.get(cover_url).json()["result"]) / 1000000000000000000 # Dividing because there are 18 decimals in this token

      # Get the balance of Dai token in the pool
      dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={claim_pool}&tag=latest&apikey={API}"

      dai_balance = int(
          requests.get(dai_url).json()["result"]) / 1000000000000000000

      return round(dai_balance / cover_balance * claim_multiplier, 4)


  def noclaim():
      # Get the balance of NoClaim token in the pool
      cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={noclaim_token}&address={noclaim_pool}&tag=latest&apikey={API}"

      cover_balance = int(
          requests.get(cover_url).json()["result"]) / 1000000000000000000

      # Get the balance of Dai token in the pool
      dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={noclaim_pool}&tag=latest&apikey={API}"

      dai_balance = int(
          requests.get(dai_url).json()["result"]) / 1000000000000000000

      # print("dai:", dai_balance, "     cover:", cover_balance, "   dai_balance / cover_balance =", dai_balance / cover_balance)

      return round(dai_balance / cover_balance * noclaim_multiplier, 4)

  claim = claim()
  noclaim = noclaim()
  total = noclaim + claim

  return claim, noclaim, total

def augur():
  # 80/20 pool = 4x multiplier, 98/2 = 49
  claim_multiplier = 4
  noclaim_multiplier = 49

  # Here are the addresses for pools and tokens. (Dai token address isn't here because it's same for all pools
  claim_pool = "0x0077732357ac0f29e26ea629b79ab3b266ddb796"
  noclaim_pool = "0x98ad8d1dfd7d4ac0850e24ff8fa8f41b69a60de0"
  claim_token = "0xd85ca69e58e9367D72B04D5902b6fdbe39cA4cF1"
  noclaim_token = "0x6AA0a667507e02bFE86182AD9f74f69299D1A27c"

  def claim():
      # Get the balance of Claim token in the pool
      cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={claim_token}&address={claim_pool}&tag=latest&apikey={API}"

      cover_balance = int(
          requests.get(cover_url).json()["result"]) / 1000000000000000000 # Dividing because there are 18 decimals in this token

      # Get the balance of Dai token in the pool
      dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={claim_pool}&tag=latest&apikey={API}"

      dai_balance = int(
          requests.get(dai_url).json()["result"]) / 1000000000000000000

      return round(dai_balance / cover_balance * claim_multiplier, 4)


  def noclaim():
      # Get the balance of NoClaim token in the pool
      cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={noclaim_token}&address={noclaim_pool}&tag=latest&apikey={API}"

      cover_balance = int(
          requests.get(cover_url).json()["result"]) / 1000000000000000000

      # Get the balance of Dai token in the pool
      dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={noclaim_pool}&tag=latest&apikey={API}"

      dai_balance = int(
          requests.get(dai_url).json()["result"]) / 1000000000000000000

      # print("dai:", dai_balance, "     cover:", cover_balance, "   dai_balance / cover_balance =", dai_balance / cover_balance)

      return round(dai_balance / cover_balance * noclaim_multiplier, 4)

  claim = claim()
  noclaim = noclaim()
  total = noclaim + claim
  
  return claim, noclaim, total




print(augur())