import pandas, dateutil.parser
from scipy.stats.distributions import binom
from matplotlib import pyplot as plt

data = pandas.DataFrame(pandas.read_csv("crash_data.csv"))

# Fatality rate
fatality_rate =  data["Fatalities"] / data["Aboard"]
print(fatality_rate.sum()/fatality_rate.size)

# plot total fatalities/crashes
plt.xlabel("Fatalities")
plt.ylabel("Crashes")
plt.hist(data["Fatalities"].dropna().values, bins=50)
plt.show()
