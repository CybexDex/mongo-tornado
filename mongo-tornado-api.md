# account_history
## GET
* run ths cmd in shell:

```curl  http://39.105.55.115:8081/api/v1/account_history/1.2.2506 -X GET```
* result returned as tw parts, one is content *pending in node*, the other one is *lib already exist in mongodb*; althougn they're all json, they are of different format:
1. pending in node part:
```
{
	"id": 3,
	"jsonrpc": "2.0",
	"result": [{
		"id": "1.11.5024",
		"op": [5, {
			"fee": {
				"amount": 5610,
				"asset_id": "1.3.0"
			},
			"registrar": "1.2.7",
			"referrer": "1.2.7",
			"referrer_percent": 0,
			"name": "oph417",
			"owner": {
				"weight_threshold": 1,
				"account_auths": [],
				"key_auths": [
					["CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF", 1]
				],
				"address_auths": []
			},
			"active": {
				"weight_threshold": 1,
				"account_auths": [],
				"key_auths": [
					["CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF", 1]
				],
				"address_auths": []
			},
			"options": {
				"memo_key": "CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF",
				"voting_account": "1.2.5",
				"num_witness": 0,
				"num_committee": 0,
				"votes": [],
				"extensions": []
			},
			"extensions": {}
		}],
		"result": [1, "1.2.2506"],
		"block_num": 61364,
		"trx_in_block": 0,
		"op_in_trx": 0,
		"virtual_op": 5101
	}]
}
```
2. lib in mongo part:
```
[{
	"operation_history": {
		"operation_result": "[1,\"1.2.2506\"]",
		"trx_in_block": 0,
		"op_in_trx": 0,
		"op": "[5,{\"fee\":{\"amount\":5610,\"asset_id\":\"1.3.0\"},\"registrar\":\"1.2.7\",\"referrer\":\"1.2.7\",\"referrer_percent\":0,\"name\":\"oph417\",\"owner\":{\"weight_threshold\":1,\"account_auths\":[],\"key_auths\":[[\"CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF\",1]],\"address_auths\":[]},\"active\":{\"weight_threshold\":1,\"account_auths\":[],\"key_auths\":[[\"CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF\",1]],\"address_auths\":[]},\"options\":{\"memo_key\":\"CYB5eHye2t6XX5BkrgrdDRy7ydxZMvHhAAph76J75NVdxE41FQCUF\",\"voting_account\":\"1.2.5\",\"num_witness\":0,\"num_committee\":0,\"votes\":[],\"extensions\":[]},\"extensions\":{}}]",
		"virtual_op": 5101
	},
	"account_history": {
		"operation_id": "1.11.5024",
		"account": "1.2.2506",
		"next": "2.9.0",
		"id": "2.9.10004",
		"sequence": 1
	},
	"block_data": {
		"block_time": "2018-02-27T23:51:18",
		"trx_id": "92083f843f76a262d11b25fd5ba20c9a5c8e96b6",
		"block_num": 61364
	},
	"operation_type": 5,
	"_id": {
		"$oid": "5b7ba6ed55ef33729d072ce6"
	},
	"additional_data": {
		"transfer_data": {
			"to": "1.2.0",
			"amount": 0,
			"from": "1.2.0",
			"asset": "1.3.0"
		},
		"fee_data": {
			"amount": 0,
			"asset": "1.3.0"
		}
	}
}]
```

## POST
post is used as page split(分页), which is a common usage for front end.
* run ths cmd in shell:
```
 curl  http://39.105.55.115:8081/api/v1/account_history/1.2.7 -d limit=10 -d skip=40
```
skip means offset, limit means returned column size.
result are separated in two parts as above(same with get).

# account_name
this api is used to find account id with a known account name.
## GET
* run this cmd in shell:
```
curl  http://39.105.55.115:8081/api/v1/account_name/nathan -X GET
```
* result:
```
["1.2.25"]
```
# account_id
this api is used to find account name with a known account id.

## GET
* run this cmd in shell:

```
curl  http://39.105.55.115:8081/api/v1/account_id/1.2.2506 -X GET
```
* result:
```
["oph417"]
```

# block_num
this api is to find all the operations under specific block number.
## GET
* run this cmd in shell:
```
curl  http://39.105.55.115:8081/api/v1/block_num/4225083 -X GET
```
* result :
```
{
	"operation_history": {
		"operation_result": "[1,\"1.7.52711852\"]",
		"trx_in_block": 0,
		"op_in_trx": 0,
		"op": "[1,{\"fee\":{\"amount\":55,\"asset_id\":\"1.3.0\"},\"seller\":\"1.2.10378\",\"amount_to_sell\":{\"amount\":9498602,\"asset_id\":\"1.3.0\"},\"min_to_receive\":{\"amount\":6432036,\"asset_id\":\"1.3.9\"},\"expiration\":\"2018-07-23T09:36:29\",\"fill_or_kill\":false,\"extensions\":[]}]",
		"virtual_op": 54523
	},
	"account_history": {
		"operation_id": "1.11.138794141",
		"account": "1.2.10378",
		"next": "2.9.138909579",
		"id": "2.9.138910817",
		"sequence": 123270
	},
	"block_data": {
		"block_time": "2018-07-23T09:30:33",
		"trx_id": "1311c1185e405f8ef1c7e7bd72c62a9b28c3e0ec",
		"block_num": 4225083
	},
	"operation_type": 1,
	"_id": {
		"$oid": "5b7ca6a255ef33729d4ea233"
	},
	"additional_data": {
		"transfer_data": {
			"to": "1.2.0",
			"amount": 0,
			"from": "1.2.0",
			"asset": "1.3.0"
		},
		"fee_data": {
			"amount": 0,
			"asset": "1.3.0"
		}
	}
}
```

