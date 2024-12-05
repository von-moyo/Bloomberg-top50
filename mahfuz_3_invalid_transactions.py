# Invalid transaction
from collections import defaultdict

def invalidTransactions(transactions):
    # Parse transactions into structured data and organize by name
    transaction_data = []
    for i, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(',')
        transaction_data.append((name, int(time), int(amount), city, i))
    
    # Group transactions by name for easier access
    transactions_by_name = defaultdict(list)
    for transaction in transaction_data:
        name = transaction[0]
        transactions_by_name[name].append(transaction)
    
    # Set to store indices of invalid transactions
    invalid = set()
    
    # Process each group of transactions by name
    for name, transactions in transactions_by_name.items():
        # Sort transactions by time for each name
        transactions.sort(key=lambda x: x[1])
        
        # Sliding window approach within the 60-minute range
        for i, (name, time, amount, city, idx) in enumerate(transactions):
            # Condition 1: Mark transaction as invalid if amount > 1000
            if amount > 1000:
                invalid.add(idx)
            
            # Condition 2: Check only subsequent transactions within the 60-minute range
            for j in range(i + 1, len(transactions)):
                other_time, other_city, other_idx = transactions[j][1], transactions[j][3], transactions[j][4]
                
                # Stop the loop if other_time is outside the 60-minute window
                if other_time - time > 60:
                    break
                
                # If the cities are different, mark both transactions as invalid
                if city != other_city:
                    invalid.add(idx)
                    invalid.add(other_idx)
    
    # Return invalid transactions in original order
    return [transactions[i] for i in sorted(invalid)]



# create the list of transactions
# use the list to populate the hashmap
# initialise a set to contain the invalid transaction id


# Time Complexity: 𝑂(𝑛log⁡𝑛)
# Space Complexity: 𝑂(𝑛)