# Write a program: a fake "blockchain transaction" as a dictionary with keys: sender, receiver, amount, timestamp. Validate that all required fields exist

Transaction = {
    'transaction_1':{'sender':'oyasis', 'receiver':'prabhu', 'amount':'10', 'timestamp':'2026-04-23T21:32:43'},
    'transaction_2':{'sender':'ashok', 'receiver':'sahil', 'amount':'100', 'timestamp':'2026-04-23T22:12:56'}, 
    'transaction_3':{'sender':'prime', 'amount':'0.01','timestamp':'2026-04-23T22:43:03'}
}

required_fields = {'sender', 'receiver', 'amount', 'timestamp'}

def validate_transaction(tx):
    return required_fields.issubset(tx.keys())

for tx_id, tx_data in Transaction.items():
    if validate_transaction(tx_data):
        print(f'{tx_id}: Valid')
    else:
        print(f'{tx_id}: Invalid')