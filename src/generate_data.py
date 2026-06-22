import numpy as np
import pandas as pd
np.random.seed(42)
n_samples = 800
data = pd.DataFrame({
    'Mn_pct': np.random.normal(39, 5, n_samples).clip(20, 50),
    'Fe_pct': np.random.normal(12, 4, n_samples).clip(2, 28),
})
def classify_quality(row):
    if row['Mn_pct'] >= 43:
        return 'Haute'
    elif row['Mn_pct'] >= 38:
        return 'Moyenne'
    else:
        return 'Basse'
data['Qualite'] = data.apply(classify_quality, axis=1)
data.to_csv('data/raw/raw_data.csv', index=False)
print(f"{len(data)} échantillon généré avec succès.")
print(data['Qualite'].value_counts())
