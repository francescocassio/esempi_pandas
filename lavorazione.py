import pandas as pd
import numpy as np


# Carica il file
df = pd.read_csv('vgsales.csv')

print(len(df))

df = df.dropna(subset=['Publisher'])

print(len(df))

df = df[df['Publisher'] != 'Unknown']

print(len(df))

df = df.dropna(subset=['Year'])

print(len(df))

df = df.drop(columns=['Rank'])

df.reset_index(drop=True, inplace=True)

# 3. Creiamo la colonna 'Rank' partendo da 1
# Usiamo insert(posizione, nome, valori) per metterla all'inizio (posizione 0)
df.insert(0, 'Rank', range(1, len(df) + 1))

# 4. Esporta in CSV
# Usiamo index=False perché il nostro Rank è già una colonna dei dati
df.to_csv('vgsales_pulito.csv', index=False)