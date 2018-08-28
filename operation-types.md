
# transfer_operation (op_id : 0)

```
{
	"_id": ObjectId("5b7ba6d455ef33729d0705d3"),
	"account_history": {
		"id": "2.9.1",
		"account": "1.2.18",
		"operation_id": "1.11.1",
		"sequence": 1,
		"next": "2.9.0"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 78,
		"op": "[0,{\"fee\":{\"amount\":1067,\"asset_id\":\"1.3.0\"},\"from\":\"1.2.25\",\"to\":\"1.2.18\",\"amount\":{\"amount\":2000000000,\"asset_id\":\"1.3.0\"},\"memo\":{\"from\":\"CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ\",\"to\":\"CYB6Qz6VMiANXtjopYmX7XQHB22A56qbHnEmmFnpabtdnarYtZAyM\",\"nonce\":\"7711682153452573748\",\"message\":\"1f08c7449b3bb418335e235c4ae186d86a9b21835f3d14b43cf0a3d435b7e852eb795be8a4ea48145a032508ba8a84c6\"},\"extensions\":[]}]"
	},
	"operation_type": 0,
	"block_data": {
		"block_num": 171,
		"block_time": "2018-02-25T20:43:15",
		"trx_id": "cd56fa65c9ac783dde952576e2a4954bf9c50827"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format:
```
{
	"fee": {
		"amount": 1067,
		"asset_id": "1.3.0"
	},
	"from": "1.2.25",
	"to": "1.2.18",
	"amount": {
		"amount": 2000000000,
		"asset_id": "1.3.0"
	},
	"memo": {
		"from": "CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ",
		"to": "CYB6Qz6VMiANXtjopYmX7XQHB22A56qbHnEmmFnpabtdnarYtZAyM",
		"nonce": "7711682153452573748",
		"message": "1f08c7449b3bb418335e235c4ae186d86a9b21835f3d14b43cf0a3d435b7e852eb795be8a4ea48145a032508ba8a84c6"
	},
	"extensions": []
}
```

# limit_order_create_operation (op_id : 1)
```
{
	"_id": ObjectId("5b7ba6db55ef33729d070d50"),
	"account_history": {
		"id": "2.9.1918",
		"account": "1.2.368",
		"operation_id": "1.11.975",
		"sequence": 4,
		"next": "2.9.1589"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[1,\"1.7.0\"]",
		"virtual_op": 1052,
		"op": "[1,{\"fee\":{\"amount\":55,\"asset_id\":\"1.3.0\"},\"seller\":\"1.2.368\",\"amount_to_sell\":{\"amount\":100000,\"asset_id\":\"1.3.0\"},\"min_to_receive\":{\"amount\":1000000,\"asset_id\":\"1.3.2\"},\"expiration\":\"2023-02-26T11:54:25\",\"fill_or_kill\":false,\"extensions\":[]}]"
	},
	"operation_type": 1,
	"block_data": {
		"block_num": 18352,
		"block_time": "2018-02-26T11:54:45",
		"trx_id": "a9b63ae6518e2f192e3fc2eeee60bd5e79911617"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format:
```
{
	{
		"amount": 55,
		"asset_id": "1.3.0"
	}, "seller": "1.2.368", "amount_to_sell": {
		"amount": 100000,
		"asset_id": "1.3.0"
	}, "min_to_receive": {
		"amount": 1000000,
		"asset_id": "1.3.2"
	}, "expiration": "2023-02-26T11:54:25", "fill_or_kill": false, "extensions": []
}

```

# limit_order_cancel_operation (op_id : 2)


```
{
	"_id": ObjectId("5b7ba6db55ef33729d070d57"),
	"account_history": {
		"id": "2.9.1925",
		"account": "1.2.368",
		"operation_id": "1.11.979",
		"sequence": 5,
		"next": "2.9.1918"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[2,{\"amount\":100000,\"asset_id\":\"1.3.0\"}]",
		"virtual_op": 1056,
		"op": "[2,{\"fee\":{\"amount\":5,\"asset_id\":\"1.3.0\"},\"fee_paying_account\":\"1.2.368\",\"order\":\"1.7.0\",\"extensions\":[]}]"
	},
	"operation_type": 2,
	"block_data": {
		"block_num": 18368,
		"block_time": "2018-02-26T11:55:33",
		"trx_id": "c59feb60c66b21e00863078b8ebbc17e3b3ce2b4"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format:
```
{
	"fee": {
		"amount": 5,
		"asset_id": "1.3.0"
	},
	"fee_paying_account": "1.2.368",
	"order": "1.7.0",
	"extensions": []
}
```

# call_order_update_operation (op_id : 3)
```
{
	"_id": ObjectId("5b7bc06955ef33729dad39a0"),
	"account_history": {
		"id": "2.9.10892238",
		"account": "1.2.31449",
		"operation_id": "1.11.10802147",
		"sequence": 3,
		"next": "2.9.10723683"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 54335,
		"op": "[3,{\"fee\":{\"amount\":55,\"asset_id\":\"1.3.0\"},\"funding_account\":\"1.2.31449\",\"delta_collateral\":{\"amount\":1000000,\"asset_id\":\"1.3.0\"},\"delta_debt\":{\"amount\":1000000,\"asset_id\":\"1.3.58\"},\"extensions\":[]}]"
	},
	"operation_type": 3,
	"block_data": {
		"block_num": 2965695,
		"block_time": "2018-06-09T10:14:33",
		"trx_id": "4ca97b15211a29a5bfa5599b4b394ae963f52e2e"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op fromat
```
{
	"fee": {
		"amount": 55,
		"asset_id": "1.3.0"
	},
	"funding_account": "1.2.31449",
	"delta_collateral": {
		"amount": 1000000,
		"asset_id": "1.3.0"
	},
	"delta_debt": {
		"amount": 1000000,
		"asset_id": "1.3.58"
	},
	"extensions": []
}
```

# fill_order_operation (op_id : 4)
```
{
	"_id": ObjectId("5b7ba72f55ef33729d075176"),
	"account_history": {
		"id": "2.9.19364",
		"account": "1.2.904",
		"operation_id": "1.11.9934",
		"sequence": 7,
		"next": "2.9.19363"
	},
	"operation_history": {
		"trx_in_block": 2,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 10013,
		"op": "[4,{\"fee\":{\"amount\":0,\"asset_id\":\"1.3.2\"},\"order_id\":\"1.7.110\",\"account_id\":\"1.2.904\",\"pays\":{\"amount\":2600000,\"asset_id\":\"1.3.0\"},\"receives\":{\"amount\":13000,\"asset_id\":\"1.3.2\"},\"fill_price\":{\"base\":{\"amount\":13000,\"asset_id\":\"1.3.2\"},\"quote\":{\"amount\":2600000,\"asset_id\":\"1.3.0\"}},\"is_maker\":false}]"
	},
	"operation_type": 4,
	"block_data": {
		"block_num": 204745,
		"block_time": "2018-03-05T08:16:03",
		"trx_id": "b791ccadaba35499ea8b1a99d93c0078aa0ebf1b"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 0,
		"asset_id": "1.3.2"
	},
	"order_id": "1.7.110",
	"account_id": "1.2.904",
	"pays": {
		"amount": 2600000,
		"asset_id": "1.3.0"
	},
	"receives": {
		"amount": 13000,
		"asset_id": "1.3.2"
	},
	"fill_price": {
		"base": {
			"amount": 13000,
			"asset_id": "1.3.2"
		},
		"quote": {
			"amount": 2600000,
			"asset_id": "1.3.0"
		}
	},
	"is_maker": false
}
```

# account_create_operation (op_id : 5)
```
{
	"_id": ObjectId("5b7ba6d555ef33729d0705fb"),
	"account_history": {
		"id": "2.9.41",
		"account": "1.2.7",
		"operation_id": "1.11.21",
		"sequence": 2,
		"next": "2.9.19"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[1,\"1.2.28\"]",
		"virtual_op": 98,
		"op": "[5,{\"fee\":{\"amount\":5611,\"asset_id\":\"1.3.0\"},\"registrar\":\"1.2.7\",\"referrer\":\"1.2.7\",\"referrer_percent\":0,\"name\":\"ldw-format\",\"owner\":{\"weight_threshold\":1,\"account_auths\":[],\"key_auths\":[[\"CYB5VtvbiF9j6ULvCq91BU1uHVroKnpGAhsEC8shaUFnM6KNrxqHh\",1]],\"address_auths\":[]},\"active\":{\"weight_threshold\":1,\"account_auths\":[],\"key_auths\":[[\"CYB7Bg5P7tnDVt42EH5SPP9eLkn5BvfLp99DYK9DzmT31CRxt4AFx\",1]],\"address_auths\":[]},\"options\":{\"memo_key\":\"CYB7Bg5P7tnDVt42EH5SPP9eLkn5BvfLp99DYK9DzmT31CRxt4AFx\",\"voting_account\":\"1.2.5\",\"num_witness\":0,\"num_committee\":0,\"votes\":[],\"extensions\":[]},\"extensions\":{}}]"
	},
	"operation_type": 5,
	"block_data": {
		"block_num": 273,
		"block_time": "2018-02-25T20:48:21",
		"trx_id": "fc7ea15551db4c7cb13bd98ba22b750960653faf"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 5611,
		"asset_id": "1.3.0"
	},
	"registrar": "1.2.7",
	"referrer": "1.2.7",
	"referrer_percent": 0,
	"name": "ldw-format",
	"owner": {
		"weight_threshold": 1,
		"account_auths": [],
		"key_auths": [
			["CYB5VtvbiF9j6ULvCq91BU1uHVroKnpGAhsEC8shaUFnM6KNrxqHh", 1]
		],
		"address_auths": []
	},
	"active": {
		"weight_threshold": 1,
		"account_auths": [],
		"key_auths": [
			["CYB7Bg5P7tnDVt42EH5SPP9eLkn5BvfLp99DYK9DzmT31CRxt4AFx", 1]
		],
		"address_auths": []
	},
	"options": {
		"memo_key": "CYB7Bg5P7tnDVt42EH5SPP9eLkn5BvfLp99DYK9DzmT31CRxt4AFx",
		"voting_account": "1.2.5",
		"num_witness": 0,
		"num_committee": 0,
		"votes": [],
		"extensions": []
	},
	"extensions": {}
}
```

# account_update_operation (op_id : 6)
```
{
	"_id": ObjectId("5b7ba6d555ef33729d070611"),
	"account_history": {
		"id": "2.9.63",
		"account": "1.2.20",
		"operation_id": "1.11.32",
		"sequence": 3,
		"next": "2.9.27"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 109,
		"op": "[6,{\"fee\":{\"amount\":55,\"asset_id\":\"1.3.0\"},\"account\":\"1.2.32\",\"active\":{\"weight_threshold\":1,\"account_auths\":[[\"1.2.20\",1],[\"1.2.28\",1],[\"1.2.29\",1],[\"1.2.31\",3]],\"key_auths\":[[\"CYB6MSU5EKoavzZfFgrWiAFznEniTWVMBMMN2bxkmFmDnn3MvXjfZ\",1]],\"address_auths\":[]},\"extensions\":{}}]"
	},
	"operation_type": 6,
	"block_data": {
		"block_num": 674,
		"block_time": "2018-02-25T21:08:33",
		"trx_id": "96f2230055755f00908913f6dff15cb7bc7c0269"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op foramt
```
{
	"fee": {
		"amount": 55,
		"asset_id": "1.3.0"
	},
	"account": "1.2.32",
	"active": {
		"weight_threshold": 1,
		"account_auths": [
			["1.2.20", 1],
			["1.2.28", 1],
			["1.2.29", 1],
			["1.2.31", 3]
		],
		"key_auths": [
			["CYB6MSU5EKoavzZfFgrWiAFznEniTWVMBMMN2bxkmFmDnn3MvXjfZ", 1]
		],
		"address_auths": []
	},
	"extensions": {}
}
```
# account_whitelist_operation (op_id : 7)
```
{
	"_id": ObjectId("5b7ba78155ef33729d077c2b"),
	"account_history": {
		"id": "2.9.30297",
		"account": "1.2.4697",
		"operation_id": "1.11.17127",
		"sequence": 9,
		"next": "2.9.30296"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 17209,
		"op": "[7,{\"fee\":{\"amount\":5555,\"asset_id\":\"1.3.0\"},\"authorizing_account\":\"1.2.4697\",\"account_to_list\":\"1.2.4697\",\"new_listing\":1,\"extensions\":[]}]"
	},
	"operation_type": 7,
	"block_data": {
		"block_num": 369283,
		"block_time": "2018-03-11T01:50:54",
		"trx_id": "f674b5975c95ae7c87e862522b5a0d8fdcbc1432"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 5555,
		"asset_id": "1.3.0"
	},
	"authorizing_account": "1.2.4697",
	"account_to_list": "1.2.4697",
	"new_listing": 1,
	"extensions": []
}
```
# account_upgrade_operation (op_id : 8)
```
{
	"_id": ObjectId("5b7ba6dc55ef33729d0712b2"),
	"account_history": {
		"id": "2.9.3296",
		"account": "1.2.754",
		"operation_id": "1.11.1665",
		"sequence": 6,
		"next": "2.9.3265"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 1742,
		"op": "[8,{\"fee\":{\"amount\":100000000,\"asset_id\":\"1.3.0\"},\"account_to_upgrade\":\"1.2.754\",\"upgrade_to_lifetime_member\":true,\"extensions\":[]}]"
	},
	"operation_type": 8,
	"block_data": {
		"block_num": 20329,
		"block_time": "2018-02-26T13:33:57",
		"trx_id": "a59238fc7d586f2c2c4b3e324971fb9b8b797e1b"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 100000000,
		"asset_id": "1.3.0"
	},
	"account_to_upgrade": "1.2.754",
	"upgrade_to_lifetime_member": true,
	"extensions": []
}
```

# account_transfer_operation (op_id : 9)
```

```



# asset_create_operation (op_id : 10)

```
{
	"_id": ObjectId("5b7ba6d555ef33729d07063d"),
	"account_history": {
		"id": "2.9.107",
		"account": "1.2.29",
		"operation_id": "1.11.55",
		"sequence": 13,
		"next": "2.9.105"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[1,\"1.3.1\"]",
		"virtual_op": 132,
		"op": "[10,{\"fee\":{\"amount\":1000010351,\"asset_id\":\"1.3.0\"},\"issuer\":\"1.2.29\",\"symbol\":\"JADE\",\"precision\":6,\"common_options\":{\"max_supply\":\"1000000000000000\",\"market_fee_percent\":0,\"max_market_fee\":0,\"issuer_permissions\":79,\"flags\":0,\"core_exchange_rate\":{\"base\":{\"amount\":200000000,\"asset_id\":\"1.3.0\"},\"quote\":{\"amount\":1000000,\"asset_id\":\"1.3.1\"}},\"whitelist_authorities\":[],\"blacklist_authorities\":[],\"whitelist_markets\":[],\"blacklist_markets\":[],\"description\":\"{\\\"main\\\":\\\"It's gateway name.\\\",\\\"market\\\":\\\"\\\"}\",\"extensions\":[]},\"is_prediction_market\":false,\"extensions\":[]}]"
	},
	"operation_type": 10,
	"block_data": {
		"block_num": 1481,
		"block_time": "2018-02-25T21:48:54",
		"trx_id": "9625afed51b1d265bbbb461e0d1a0ef6288c83dd"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 1000010351,
		"asset_id": "1.3.0"
	},
	"issuer": "1.2.29",
	"symbol": "JADE",
	"precision": 6,
	"common_options": {
		"max_supply": "1000000000000000",
		"market_fee_percent": 0,
		"max_market_fee": 0,
		"issuer_permissions": 79,
		"flags": 0,
		"core_exchange_rate": {
			"base": {
				"amount": 200000000,
				"asset_id": "1.3.0"
			},
			"quote": {
				"amount": 1000000,
				"asset_id": "1.3.1"
			}
		},
		"whitelist_authorities": [],
		"blacklist_authorities": [],
		"whitelist_markets": [],
		"blacklist_markets": [],
		"description": "{\"main\":\"It's gateway name.\",\"market\":\"\"}",
		"extensions": []
	},
	"is_prediction_market": false,
	"extensions": []
}
```


# asset_update_operation (op_id : 11)
```
{
	"_id": ObjectId("5b7ba90c55ef33729d07b9d8"),
	"account_history": {
		"id": "2.9.46086",
		"account": "1.2.29",
		"operation_id": "1.11.26911",
		"sequence": 166,
		"next": "2.9.45729"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 26996,
		"op": "[11,{\"fee\":{\"amount\":111157,\"asset_id\":\"1.3.0\"},\"issuer\":\"1.2.29\",\"asset_to_update\":\"1.3.4\",\"new_options\":{\"max_supply\":\"1000000000000000\",\"market_fee_percent\":0,\"max_market_fee\":0,\"issuer_permissions\":79,\"flags\":0,\"core_exchange_rate\":{\"base\":{\"amount\":1300000,\"asset_id\":\"1.3.0\"},\"quote\":{\"amount\":1000000,\"asset_id\":\"1.3.4\"}},\"whitelist_authorities\":[],\"blacklist_authorities\":[],\"whitelist_markets\":[],\"blacklist_markets\":[],\"description\":\"{\\\"main\\\":\\\"It's an EOS IOU of Jade gateway.\\\",\\\"market\\\":\\\"\\\"}\",\"extensions\":[]},\"extensions\":[]}]"
	},
	"operation_type": 11,
	"block_data": {
		"block_num": 861585,
		"block_time": "2018-03-28T05:23:42",
		"trx_id": "d591c2fbf0143352e51eab1c147f60f65b1fed8e"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 111157,
		"asset_id": "1.3.0"
	},
	"issuer": "1.2.29",
	"asset_to_update": "1.3.4",
	"new_options": {
		"max_supply": "1000000000000000",
		"market_fee_percent": 0,
		"max_market_fee": 0,
		"issuer_permissions": 79,
		"flags": 0,
		"core_exchange_rate": {
			"base": {
				"amount": 1300000,
				"asset_id": "1.3.0"
			},
			"quote": {
				"amount": 1000000,
				"asset_id": "1.3.4"
			}
		},
		"whitelist_authorities": [],
		"blacklist_authorities": [],
		"whitelist_markets": [],
		"blacklist_markets": [],
		"description": "{\"main\":\"It's an EOS IOU of Jade gateway.\",\"market\":\"\"}",
		"extensions": []
	},
	"extensions": []
}
```

# asset_update_bitasset_operation (op_id : 12)
```

```
* op format
```

```


# asset_update_feed_producers_operation (op_id : 13)
```

```
* op format
```

```


# asset_issue_operation (op_id : 14)
```
{
	"_id": ObjectId("5b7ba72455ef33729d074e8a"),
	"account_history": {
		"id": "2.9.18616",
		"account": "1.2.29",
		"operation_id": "1.11.9501",
		"sequence": 103,
		"next": "2.9.15045"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 9580,
		"op": "[14,{\"fee\":{\"amount\":1058,\"asset_id\":\"1.3.0\"},\"issuer\":\"1.2.29\",\"asset_to_issue\":{\"amount\":400000000,\"asset_id\":\"1.3.2\"},\"issue_to_account\":\"1.2.4733\",\"memo\":{\"from\":\"CYB6bCHU6sWD4estBBmpNeLMsuL3aZynrBLANGGg2MjELxzNJt45r\",\"to\":\"CYB7LQo2kFyqmvjgb6xdNL2iCDdPd4dhgjypkRWEcMgdiQBM3gvK7\",\"nonce\":\"389163421220045\",\"message\":\"366d2761dd42471a533dc426ead2fdcbf3b10cf9d6b0cdbbec66754919522fbe\"},\"extensions\":[]}]"
	},
	"operation_type": 14,
	"block_data": {
		"block_num": 182095,
		"block_time": "2018-03-04T13:20:18",
		"trx_id": "02db3892b307f93c984d755f6d07bc33742f4d65"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 1058,
		"asset_id": "1.3.0"
	},
	"issuer": "1.2.29",
	"asset_to_issue": {
		"amount": 400000000,
		"asset_id": "1.3.2"
	},
	"issue_to_account": "1.2.4733",
	"memo": {
		"from": "CYB6bCHU6sWD4estBBmpNeLMsuL3aZynrBLANGGg2MjELxzNJt45r",
		"to": "CYB7LQo2kFyqmvjgb6xdNL2iCDdPd4dhgjypkRWEcMgdiQBM3gvK7",
		"nonce": "389163421220045",
		"message": "366d2761dd42471a533dc426ead2fdcbf3b10cf9d6b0cdbbec66754919522fbe"
	},
	"extensions": []
}
```


# asset_reserve_operation (op_id : 15)
```

```
* op format
```

```


# asset_fund_fee_pool_operation (op_id : 16)
```
{
	"_id": ObjectId("5b7ba72e55ef33729d07503e"),
	"account_history": {
		"id": "2.9.19052",
		"account": "1.2.29",
		"operation_id": "1.11.9722",
		"sequence": 106,
		"next": "2.9.18935"
	},
	"operation_history": {
		"trx_in_block": 0,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 9801,
		"op": "[16,{\"fee\":{\"amount\":27778,\"asset_id\":\"1.3.0\"},\"from_account\":\"1.2.29\",\"asset_id\":\"1.3.2\",\"amount\":100000000,\"extensions\":[]}]"
	},
	"operation_type": 16,
	"block_data": {
		"block_num": 202814,
		"block_time": "2018-03-05T06:39:06",
		"trx_id": "e6c03c398c87a7bd4b57cf9984d9bf403707e73c"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 27778,
		"asset_id": "1.3.0"
	},
	"from_account": "1.2.29",
	"asset_id": "1.3.2",
	"amount": 100000000,
	"extensions": []
}
```


# asset_settle_operation (op_id : 17)
```
{
	"_id": ObjectId("5b7bc07e55ef33729dadf36c"),
	"account_history": {
		"id": "2.9.10939802",
		"account": "1.2.31451",
		"operation_id": "1.11.10849698",
		"sequence": 12,
		"next": "2.9.10939410"
	},
	"operation_history": {
		"trx_in_block": 4,
		"op_in_trx": 0,
		"operation_result": "[2,{\"amount\":1000000,\"asset_id\":\"1.3.0\"}]",
		"virtual_op": 36350,
		"op": "[17,{\"fee\":{\"amount\":2777,\"asset_id\":\"1.3.0\"},\"account\":\"1.2.31451\",\"amount\":{\"amount\":1000000,\"asset_id\":\"1.3.54\"},\"extensions\":[]}]"
	},
	"operation_type": 17,
	"block_data": {
		"block_num": 2968142,
		"block_time": "2018-06-09T12:16:54",
		"trx_id": "a2ade9fd1182a0b7c2586be4150e45d3bac03dfd"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 2777,
		"asset_id": "1.3.0"
	},
	"account": "1.2.31451",
	"amount": {
		"amount": 1000000,
		"asset_id": "1.3.54"
	},
	"extensions": []
}
```


# asset_global_settle_operation (op_id : 18)
```
{
	"_id": ObjectId("5b7bc07d55ef33729dadf1e0"),
	"account_history": {
		"id": "2.9.10939406",
		"account": "1.2.31980",
		"operation_id": "1.11.10849302",
		"sequence": 102,
		"next": "2.9.10933976"
	},
	"operation_history": {
		"trx_in_block": 4,
		"op_in_trx": 0,
		"operation_result": "[0,{}]",
		"virtual_op": 35954,
		"op": "[18,{\"fee\":{\"amount\":277784,\"asset_id\":\"1.3.0\"},\"issuer\":\"1.2.31980\",\"asset_to_settle\":\"1.3.47\",\"settle_price\":{\"base\":{\"amount\":1,\"asset_id\":\"1.3.47\"},\"quote\":{\"amount\":0,\"asset_id\":\"1.3.0\"}},\"extensions\":[]}]"
	},
	"operation_type": 18,
	"block_data": {
		"block_num": 2968124,
		"block_time": "2018-06-09T12:16:00",
		"trx_id": "3c397afde2a5d1b992da54b9e79354b46a75bd70"
	},
	"additional_data": {
		"fee_data": {
			"asset": "1.3.0",
			"amount": 0
		},
		"transfer_data": {
			"asset": "1.3.0",
			"amount": 0,
			"from": "1.2.0",
			"to": "1.2.0"
		}
	}
}
```
* op format
```
{
	"fee": {
		"amount": 277784,
		"asset_id": "1.3.0"
	},
	"issuer": "1.2.31980",
	"asset_to_settle": "1.3.47",
	"settle_price": {
		"base": {
			"amount": 1,
			"asset_id": "1.3.47"
		},
		"quote": {
			"amount": 0,
			"asset_id": "1.3.0"
		}
	},
	"extensions": []
}
```


# asset_publish_feed_operation (op_id : 19)
```

```
* op format
```

```


# witness_create_operation (op_id : 20)
```

```
* op format
```

```


# witness_update_operation (op_id : 21)
```

```
* op format
```

```


# proposal_create_operation (op_id : 22)
```

```
* op format
```

```


# proposal_update_operation (op_id : 23)
```

```
* op format
```

```


# proposal_delete_operation (op_id : 24)
```

```
* op format
```

```


# withdraw_permission_create_operation (op_id : 25)
```

```
* op format
```

```



# withdraw_permission_create_operation (op_id : 25)
```

```
* op format
```

```



# withdraw_permission_update_operation (op_id : 26)
```

```
* op format
```

```



# withdraw_permission_claim_operation (op_id : 27)
```

```
* op format
```

```



# withdraw_permission_delete_operation (op_id : 28)
```

```
* op format
```

```



# committee_member_create_operation (op_id : 29)
```

```
* op format
```

```



# committee_member_update_operation (op_id : 30)
```

```
* op format
```

```



# committee_member_update_global_parameters_operation (op_id : 31)
```

```
* op format
```

```



# vesting_balance_create_operation (op_id : 32)
```

```
* op format
```

```



# vesting_balance_withdraw_operation (op_id : 33)
```

```
* op format
```

```



# worker_create_operation (op_id : 34)
```

```
* op format
```

```



# custom_operation (op_id : 35)
```

```
* op format
```

```



# assert_operation (op_id : 36)
```

```
* op format
```

```



# balance_claim_operation (op_id : 37)
```

```
* op format
```

```



# override_transfer_operation (op_id : 38)
```

```
* op format
```

```



# transfer_to_blind_operation (op_id : 39)
```

```
* op format
```

```



# blind_transfer_operation (op_id : 40)
```

```
* op format
```

```

# transfer_from_blind_operation (op_id : 41)
```

```
* op format
```

```

# asset_settle_cancel_operation (op_id : 42)
```

```
* op format
```

```

# asset_claim_fees_operation (op_id : 43)
```

```
* op format
```

```

# fba_distribute_operation (op_id : 44)
```

```
* op format
```

```

# initiate_crowdfund_operation (op_id : 45)
```

```
* op format
```

```

# participate_crowdfund_operation (op_id : 46)
```

```
* op format
```

```

# withdraw_crowdfund_operation (op_id : 47)
```

```
* op format
```

```

# cancel_vesting_operation (op_id : 48)
```

```
* op format
```

```

# bid_collateral_operation (op_id : 49)
```

```
* op format
```

```

# execute_bid_operation (op_id : 50)
```

```
* op format
```

```


