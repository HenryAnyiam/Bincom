import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("laptops.csv")

x_data = list(data["Price"].values)
y_data = list(data["Rating"].values)

slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

plt.plot(x_data, y_data, color='red', label='Data')
plt.xlabel('Laptop Prices')
plt.ylabel('Ratings')
plt.title('Linear Regression Analysis of Laptop Prices')
plt.xticks(rotation=90)
plt.legend()
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)
print("p-value:", p_value)
print("Standard error:", std_err)
