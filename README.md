# mongo-tornado
# mongo-tornado-api.md
This is a webservice as a dataviewer for cybex, where you can view all the ops(include virtual ones) under specific account, please refrence mongo-tornado-api.md to know how to use the restful api.

# operation-types.md
The account_history table under mongo/cybex database store all the operations of different types:

```
  0             transfer_operation,
  1             limit_order_create_operation,
  2             limit_order_cancel_operation,
  3             call_order_update_operation,
  4             fill_order_operation,           // VIRTUAL
  5             account_create_operation,
  6             account_update_operation,
  7             account_whitelist_operation,
  8             account_upgrade_operation,
  9             account_transfer_operation,
 10             asset_create_operation,
 11             asset_update_operation,
 12             asset_update_bitasset_operation,
 13             asset_update_feed_producers_operation,
 14             asset_issue_operation,
 15             asset_reserve_operation,
 16             asset_fund_fee_pool_operation,
 17             asset_settle_operation,
 18             asset_global_settle_operation,
 19             asset_publish_feed_operation,
 20             witness_create_operation,
 21             witness_update_operation,
 22             proposal_create_operation,
 23             proposal_update_operation,
 24             proposal_delete_operation,
 25             withdraw_permission_create_operation,
 26             withdraw_permission_update_operation,
 27             withdraw_permission_claim_operation,
 28             withdraw_permission_delete_operation,
 29             committee_member_create_operation,
 30             committee_member_update_operation,
 31             committee_member_update_global_parameters_operation,
 32             vesting_balance_create_operation,
 33             vesting_balance_withdraw_operation,
 34             worker_create_operation,
 35             custom_operation,
 36             assert_operation,
 37             balance_claim_operation,
 38             override_transfer_operation,
 39             transfer_to_blind_operation,
 40             blind_transfer_operation,
 41             transfer_from_blind_operation,
 42             asset_settle_cancel_operation,  // VIRTUAL
 43             asset_claim_fees_operation,
 44             fba_distribute_operation,       // VIRTUAL
 45             initiate_crowdfund_operation,
 46             participate_crowdfund_operation,
 47             withdraw_crowdfund_operation,
 48             cancel_vesting_operation,
 49             bid_collateral_operation,
 50             execute_bid_operation           // VIRTUAL

```
please refer to operation-types.md to know the json format of some frequent used ops.
