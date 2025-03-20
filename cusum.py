import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('tank_level.csv')
print(data.head())

def cusum(target, level):
    cusum_max = [0]
    cusum_min = [0]
    for i in range(1, len(data)):
        cusum_max.append(max(0, level[i] - target))
        cusum_min.append(min(0, level[i] - target))
    return cusum_max , cusum_min


cusum_max, cusum_min = cusum(650, data['Level'])
data['CUSUM_Max'] = cusum_max
data['CUSUM_Min'] = cusum_min

plt.figure(figsize=(10, 5))
plt.plot(data['Time'], data['CUSUM_Max'], label='CUSUM Max')
plt.plot(data['Time'], data['CUSUM_Min'], label='CUSUM Min')
plt.xlabel('Time')
plt.ylabel('CUSUM')
plt.legend()
plt.show()