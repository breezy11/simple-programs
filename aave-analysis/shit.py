import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

borr = pd.read_csv("data/borrow.csv")
dep = pd.read_csv("data/deposit.csv")
flash = pd.read_csv("data/flash.csv")
liq = pd.read_csv("data/liquidation-call.csv")
orig = pd.read_csv("data/origination-fee-liquidation.csv")
red = pd.read_csv("data/redeem-underlyings.csv")
rep = pd.read_csv("data/repay.csv")
usage = pd.read_csv("data/usage-as-collateral.csv")

methods = [borr,dep,flash,liq,orig,red,rep,usage]
methods_names = ["borrow", "deposit", "flash-loan", "liquidation-call", "origination-fee-liquidation", "redeem-underlyings", "repays", "usage-as-collateral"]

for i in range(len(methods)):
    print(methods_names[i],": ",methods[i].shape)

print(orig.head())
