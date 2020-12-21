import requests

# API from etherscan. Limit: 5 requests/sec
API = "7KAXFQ7Q6ZUAQZU9S9ITS2HKSXQXMV8VGE"

# 80/20 pool = 4x multiplier, 98/2 = 49
claim_multiplier = 4
noclaim_multiplier = 49

myDefiList = [
	{
    'name':'Augur',
    'claim_pool':'0x0077732357ac0f29e26ea629b79ab3b266ddb796',
    'noclaim_pool':'0x98ad8d1dfd7d4ac0850e24ff8fa8f41b69a60de0',
    'claim_token':'0xd85ca69e58e9367D72B04D5902b6fdbe39cA4cF1',
    'noclaim_token':'0x6AA0a667507e02bFE86182AD9f74f69299D1A27c'
	},
	{
    'name':'Balancer',
		'claim_pool':'0x72a250ee19c0f8cc5772f9a33e1e330cde39e023',
    'noclaim_pool':'0x6c701226204f7937750671b041996a73180a47d6',
    'claim_token':'0x47788BD0b95Dd8e1A063843af731286c3904ec71',
    'noclaim_token':'0xE78C9Fe794e5f85906c574F7cfEb3647AD91cB87'
	},
]

def generate_url(claim_pool, noclaim_pool, claim_token, noclaim_token):
  # Get the balance of Claim token in the pool
  claim_cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={claim_token}&address={claim_pool}&tag=latest&apikey={API}"
  # Get the balance of Dai token in the pool
  claim_dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={claim_pool}&tag=latest&apikey={API}"
  
  noclaim_cover_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={noclaim_token}&address={noclaim_pool}&tag=latest&apikey={API}"
  noclaim_dai_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x6b175474e89094c44da98b954eedeac495271d0f&address={noclaim_pool}&tag=latest&apikey={API}"
  
  return claim_cover_url, claim_dai_url, noclaim_cover_url, noclaim_dai_url


for defi in myDefiList:
  claim_cover_url, claim_dai_url, noclaim_cover_url, noclaim_dai_url = generate_url(defi['claim_pool'],defi['noclaim_pool'],defi['claim_token'],defi['noclaim_token'])

  claim_cover_balance = int(requests.get(claim_cover_url).json()["result"])
  claim_dai_balance = int(requests.get(claim_dai_url).json()["result"])

  claim_price = round(claim_dai_balance / claim_cover_balance * claim_multiplier, 4)


  noclaim_cover_balance = int(requests.get(noclaim_cover_url).json()["result"])
  noclaim_dai_balance = int(requests.get(noclaim_dai_url).json()["result"])

  noclaim_price = round(noclaim_dai_balance / noclaim_cover_balance * noclaim_multiplier, 4)

  print(defi['name'], "Claim price =", claim_price, "NoClaim price =", noclaim_price, "Total =", claim_price+noclaim_price)