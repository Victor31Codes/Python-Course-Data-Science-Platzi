import numpy as np

prices = np.array([100, 200, 300])
discounts = np.array([0.8])
final_prices = prices * discounts  # Broadcasting the discounts array across prices
print("Final Prices after Discount:", final_prices)

prices = np.random.randint(100, 500, size = (3,3))
discount = np.array([10,20,30])
final_prices = prices - discount  # Broadcasting the discount array across each row of prices
print("Original Prices:\n", prices)
print("Final Prices after Discount:\n", final_prices)

array = np.array([1,2,3,4,5])
print(np.all(array > 0))  # Check if all elements are greater than 0
print(np.any(array > 3))  # Check if any element is greater than 3
print(np.any(array == 7))  # Check if any element is equal to 7

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatenated_ab = np.concatenate((array_a,array_b))  # Concatenate array_a and array_b
print("Concatenated Array A and B:", concatenated_ab)

stacked_v = np.vstack((array_a,array_b))  # Stack array_a and array_b vertically
print("Vertically Stacked Arrays:\n", stacked_v)
stacked_h = np.hstack((array_a,array_b))  # Stack array_a and array_b horizontally
print("Horizontally Stacked Arrays:\n", stacked_h)

array_c = np.arange(1,10)
split_array = np.split(array_c,3)  # Split array_c into 3 equal parts  
print("Original Array C:", array_c)
print("Split Array into 3 parts:", split_array)
