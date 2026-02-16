#obiettivo: media delle vendite delle top 10 publisher escluso nintendo
import pandas as pd

df = pd.read_csv('vgsales_pulito.csv')

df_filtrato = df[df['Publisher'] != 'Nintendo']

# Raggruppiamo per Publisher e calcoliamo la media delle vendite globali
media_publisher = df_filtrato.groupby('Publisher')['Global_Sales'].mean().reset_index()

# print(media_publisher)
# 4. Selezione dei primi 10
# Ordiniamo i valori in modo decrescente e prendiamo i primi 10
top_10_media = media_publisher.sort_values(by='Global_Sales', ascending=False).head(10)

print(top_10_media)

#abbiamo ottenuto le top 10 aziende per media di vendite

top_10_media.to_csv('top_10_media_publisher.csv', index=False)