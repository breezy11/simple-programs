import json
import csv
import pandas as pd
from datetime import datetime
from os import listdir
from os.path import isfile, join

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 1. Imports

# import borrows data
with open('data/borrows.json') as json_file:
    borrows = json.load(json_file)
data_list = []
for x in borrows:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['amount'], x['borrowRate'], x['borrowRateMode'], x['accruedBorrowInterest'], x['timestamp']])
borr = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'amount', 'borrow-rate', 'borrow-rate-mode', 'accrued-borrow-interest', 'timestamp'])
borr['date'] = borr['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
borr.drop('timestamp', axis=1, inplace=True)
borr['method'] = 'borrow'

# import deposits data
with open('data/deposits.json') as json_file:
    deposits = json.load(json_file)
data_list = []
for x in deposits:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['amount'], x['timestamp']])
dep = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'amount', 'timestamp'])
dep['date'] = dep['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
dep.drop('timestamp', axis=1, inplace=True)
dep['method'] = 'deposit'

# import luqidation_calls data
with open('data/liquidation_calls.json') as json_file:
    liquidation = json.load(json_file)
data_list = []
for x in liquidation:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['collateralAmount'], x['principalAmount'], x['liquidator'], x['timestamp']])
liq = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'collateral-amount', 'principal-amount', 'liquidator', 'timestamp'])
liq['date'] = liq['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
liq.drop('timestamp', axis=1, inplace=True)
liq['method'] = 'liquidation-call'

# import origination_fee_liquidation data
with open('data/origination_fee_liquidation.json') as json_file:
    orig_fee_liq = json.load(json_file)
data_list = []
for x in orig_fee_liq:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['feeLiquidated'], x['liquidatedCollateralForFee'], x['timestamp']])
orig = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'fee-liquidated', 'liquidated-collateral-for-free', 'timestamp'])
orig['date'] = orig['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
orig.drop('timestamp', axis=1, inplace=True)
orig['method'] = 'origination-fee-liquidation'

# import rebalance_stable_borrow_rate data
with open('data/rebalance_stable_borrow_rate.json') as json_file:
    reb_stab_borr = json.load(json_file)
data_list = []
for x in reb_stab_borr:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['borrowRateFrom'], x['borrowRateTo'], x['accruedBorrowInterest'], x['timestamp']])
reb = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'borrow-rate-from', 'borrow-rate-to', 'accrued-borrow-interest','timestamp'])
reb['date'] = reb['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
reb.drop('timestamp', axis=1, inplace=True)
reb['method'] = 'rebalance-stable-borrow-rate'

# import redeem_underlyings data
with open('data/redeem_underlyings.json') as json_file:
    red_under = json.load(json_file)
data_list = []
for x in red_under:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['amount'], x['timestamp']])
red = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'amount', 'timestamp'])
red['date'] = red['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
red.drop('timestamp', axis=1, inplace=True)
red['method'] = 'redeem-underlying'

# import repays data
with open('data/repays.json') as json_file:
    repays = json.load(json_file)
data_list = []
for x in repays:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['amountAfterFee'], x['fee'], x['timestamp']])
rep = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'amount-after-fee','fee', 'timestamp'])
rep['date'] = rep['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
rep.drop('timestamp', axis=1, inplace=True)
rep['method'] = 'repay'

# import swaps data
with open('data/swaps.json') as json_file:
    swaps = json.load(json_file)
data_list = []
for x in swaps:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['borrowRateFrom'], x['borrowRateModeFrom'],x['borrowRateTo'], x['borrowRateModeTo'], x['accruedBorrowInterest'], x['timestamp']])
swap = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'borrow-rate-from', 'borrow-rate-mode-from', 'borrow-rate-to', 'borrow-rate-mode-to', 'accrued-borrow-interest', 'timestamp'])
swap['date'] = swap['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
swap.drop('timestamp', axis=1, inplace=True)
swap['method'] = 'swap'

# import usage_as_collaterals data
with open('data/usage_as_collaterals.json') as json_file:
    usag_coll = json.load(json_file)
data_list = []
for x in usag_coll:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['user']['id'], x['fromState'], x['toState'], x['timestamp']])
usage = pd.DataFrame(list_, columns = ['id', 'pool-id', 'user-id', 'from-state', 'to-state', 'timestamp'])
usage['date'] = usage['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
usage.drop('timestamp', axis=1, inplace=True)
usage['method'] = 'usage-as-collateral'

# import flash_loans data
with open('data/flash_loans.json') as json_file:
    flash_loan = json.load(json_file)
data_list = []
for x in flash_loan:
    data_list += list(list(x.values())[0].values())[0]
list_ = []
for x in data_list:
    list_.append([x['id'], x['pool']['id'], x['target'], x['amount'], x['totalFee'], x['protocolFee'], x['timestamp']])
flash = pd.DataFrame(list_, columns = ['id', 'pool-id', 'target', 'amount', 'total-fee', 'protocol-fee', 'timestamp'])
flash['date'] = flash['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
flash.drop('timestamp', axis=1, inplace=True)
flash['method'] = 'flash-loan'

borr.sort_values('date', inplace=True, ascending=False)
dep.sort_values('date', inplace=True, ascending=False)
liq.sort_values('date', inplace=True, ascending=False)
orig.sort_values('date', inplace=True, ascending=False)
reb.sort_values('date', inplace=True, ascending=False)
red.sort_values('date', inplace=True, ascending=False)
rep.sort_values('date', inplace=True, ascending=False)
swap.sort_values('date', inplace=True, ascending=False)
usage.sort_values('date', inplace=True, ascending=False)
flash.sort_values('date', inplace=True, ascending=False)

borr = borr[borr['date'] > '2021-06-14']
dep = dep[dep['date'] > '2021-06-14']
liq = liq[liq['date'] > '2021-06-14']
orig = orig[orig['date'] > '2021-06-14']
reb = reb[reb['date'] > '2021-06-14']
red = red[red['date'] > '2021-06-14']
rep = rep[rep['date'] > '2021-06-14']
usage = usage[usage['date'] > '2021-06-14']
flash = flash[flash['date'] > '2021-06-14']

# prints the date range that each method exist in
print(borr['date'].min(), borr['date'].max())
print(dep['date'].min(), dep['date'].max())
print(liq['date'].min(), liq['date'].max())
print(orig['date'].min(), orig['date'].max())
print(red['date'].min(), red['date'].max())
print(rep['date'].min(), rep['date'].max())
print(usage['date'].min(), usage['date'].max())
print(flash['date'].min(), flash['date'].max())

borr.to_csv("data/borrow.csv")
dep.to_csv("data/deposit.csv")
liq.to_csv("data/liquidation-call.csv")
orig.to_csv("data/origination-fee-liquidation.csv")
red.to_csv("data/redeem-underlyings.csv")
rep.to_csv("data/repay.csv")
usage.to_csv("data/usage-as-collateral.csv")
flash.to_csv("data/flash.csv")

# df = borr.append(dep)
# df = df.append(flash)
# df = df.append(liq)
# df = df.append(orig)
# df = df.append(red)
# df = df.append(rep)
# df = df.append(usage)

# print(df.shape)

# df.to_csv('data/dataframe.csv')
