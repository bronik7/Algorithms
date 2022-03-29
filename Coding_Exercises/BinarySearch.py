from jovian.pythondsa import evaluate_test_cases
from datetime import datetime
import time


def find_card(cards, query):
    now = datetime.now()
    print("Now ", now)
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_number = cards[mid]
        print(f"low:{low} high: {high} mid: {mid} middle number: {mid_number}")
        if mid_number == query:
            if cards[mid] == query and cards[mid - 1] == query:
                high = mid - 1
            else:

                print((datetime.now() - now).total_seconds())
                return mid
        elif mid_number < query:
            high = mid - 1
        elif mid_number > query:
            low = mid + 1
    print(datetime.now() - now)
    return -1


print(find_card(list(range(100000000, 0, -1)), 2))

# tests = [{'input': {'cards': [13, 7, 4], 'query': 7}, 'output': 1}]
# tests.append({'input': {'cards': [], 'query': 7}, 'output': -1})
# tests.append({'input': {'cards': [13, 11, 8, 7,  4,], 'query': 7}, 'output': 3})
# tests.append({'input': {'cards': [13,8, 4,2, 1], 'query': 7}, 'output': -1})
# tests.append({'input': {'cards': [13,8, 4,2, 1], 'query': 13}, 'output': 0})
# tests.append({'input': {'cards': [7,7,7,7,5,4,3,2,1], 'query': 7}, 'output': 0})
# tests.append({'input': {'cards': [8,8,8,8,8,7,7,7,7,5,4,3,2,1], 'query': 7}, 'output': 5})
# tests.append({'input': {'cards': list(range(100000000,0,-1)), 'query': 2}, 'output': 99999998})
# evaluate_test_cases(find_card, tests)
