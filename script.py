# El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script: 

# dataset = pandas.DataFrame(cycle, v, mah_g)
# dataset = dataset.drop_duplicates()

# Pegue o escriba aquí el código de script:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Filter Cycle
# cycle_list = [1,5,9,13,18,22,26,30,34,38,42,46,50,54,58]
# dataset = dataset[(dataset['cycle'].isin(cycle_list))]

# Diagram

plt.figure(figsize=[45, 21])

sns.set_theme(style="white", font="Segoe UI")
sns.scatterplot(data=dataset, x='mah_g', y='v', hue='cycle', palette='rocket', s=500, edgecolor=None, legend=False)
plt.xlabel('Capacity (mAh/g)', fontsize=42, fontweight='bold');
plt.ylabel('Voltage (V)', fontsize=42, fontweight='bold');
plt.tick_params(axis='both', which='major', labelsize=24)

plt.show()
