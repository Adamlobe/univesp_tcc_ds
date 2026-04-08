#%%
import pandas as pd

df = pd.read_csv('voos.csv', sep=';', header=1)
df['Data Referência UTC'] = pd.to_datetime(df['Data Referência UTC'], errors='coerce')
df['Data Partida Prevista UTC'] = pd.to_datetime(df['Data Partida Prevista UTC'], errors='coerce')
df['Data Chegada Prevista UTC'] = pd.to_datetime(df['Data Chegada Prevista UTC'], errors='coerce')
df = df[
    (df['Data Referência UTC'] < '2026-01-01') &
    (df['Data Referência UTC'] > '2025-01-01')
    ]
df.shape
df['Data Referência UTC'].unique()