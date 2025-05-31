import pandas as pd
import json
import numpy as np
import math
# Transactions

raw_transactions = pd.read_csv('transactions.csv')
transactions = []
for i in range(len(raw_transactions)):
    arr_data = raw_transactions.iloc[i].values
    transactions.append(arr_data[0])

trans_mean = sum(transactions) / len(transactions)
std_mean = pd.Series(transactions).std()

data = pd.read_csv('data.csv')
"""
{
    time: 0,
    people_mean: ...,
    people_std: ...,
    spend_mean: ...,
    spend_std: ...,
    transaction_mean: ...,
    transaction_std: ...,
}
"""
curr = {}
new_json = []
spend = []
people = []
for i in range(len(data)):
    arr_data = data.iloc[i].values
    if i > 0 and (i % 10 == 0 or i == len(data) - 1):
        spend_mean = sum(spend) / len(spend) if spend else 0
        spend_std = pd.Series(spend).std() if spend else 0
        people_mean = sum(people) / len(people) if people else 0
        people_std = pd.Series(people).std() if people else 0
        curr = {
            'time': (i // 10) - 1,
            'people_mean': people_mean,
            'people_std': people_std,
            'spend_mean': spend_mean,
            'spend_std': spend_std,
            'transaction_mean': trans_mean,
            'transaction_std': std_mean
        }
        new_json.append(curr)
        people = []
        spend = []

    people.append(arr_data[1])
    for i in range(2, len(arr_data)):
        # print(type(arr_data[i]))
        if not math.isnan(float(arr_data[i])):
            spend.append(arr_data[i])

with open('observation_data.json', 'w') as f:
    json.dump(new_json, f, indent=4)
