import pandas as pd

# 1. Caricamento e pulizia
df = pd.read_csv('vgsales.csv')
df.dropna(subset=['Publisher', 'Year'], inplace=True)
df = df[df['Publisher'] != 'Unknown']
if 'Rank' in df.columns:
    df.drop(columns=['Rank'], inplace=True)

# 2. Esclusione di Nintendo
df_filtrato = df[df['Publisher'] != 'Nintendo']

# 3. Calcolo di Totale e Media per ogni Publisher
# .agg(['sum', 'mean']) calcola somma e media nello stesso momento
analisi_publisher = df_filtrato.groupby('Publisher')['Global_Sales'].agg(['sum', 'mean']).reset_index()

# Rinominiamo le colonne per renderle leggibili
analisi_publisher.columns = ['Publisher', 'Fatturato_Totale', 'Fatturato_Medio']

# 4. Ordinamento per FATTURATO TOTALE e selezione dei primi 10
top_10_fatturato = analisi_publisher.sort_values(by='Fatturato_Totale', ascending=False).head(10)

# 5. Aggiunta della colonna Rank per estetica
top_10_fatturato.reset_index(drop=True, inplace=True)
top_10_fatturato.insert(0, 'Rank', range(1, len(top_10_fatturato) + 1))

# Visualizzazione del risultato
print("Top 10 Publisher per Fatturato Totale (Escluso Nintendo):")
print(top_10_fatturato)

# 6. Riga finale per estrarre il CSV
top_10_fatturato.to_csv('top_10_fatturato_totale.csv', index=False)