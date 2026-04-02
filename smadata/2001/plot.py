# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# CSV laden
df = pd.read_csv("daily_energy.csv", sep=";")

# Datum konvertieren
df["date"] = pd.to_datetime(df["date"])

# Letzte Messung auf 2026-03-14 verschieben
target_date = pd.Timestamp.today()
target_date_str = target_date.strftime("%Y-%m-%d")
delta = target_date - df["date"].max()  # Delta berechnen
df["date"] = df["date"] + delta         # Delta zu allen Daten hinzuf�gen

# Sortieren
df = df.sort_values("date")

# Balkendiagramm
plt.figure(figsize=(10,5))
plt.bar(df["date"], df["energy_kWh"])

# Beschriftung
plt.xlabel("Date")
plt.ylabel("Energy (kWh)")
plt.title(f"Daily Energy Production shifted by delta to {target_date_str}")

# Datum lesbar machen
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()