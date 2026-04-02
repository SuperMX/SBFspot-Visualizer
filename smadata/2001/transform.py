import pandas as pd
import glob

files = sorted(glob.glob("MyPlant-20*.csv"))

daily_results = []

for file in files:
    if "Spot" in file:
        continue

    print(f"Processing {file}...")

    try:
        df = pd.read_csv(
            file,
            sep=";",
            skiprows=8,
            decimal=",",
            encoding="utf-8"
        )

        df.columns = ["datetime", "kWh_counter", "kW"]

        # Convert datetime
        df["datetime"] = pd.to_datetime(
            df["datetime"],
            format="%d/%m/%Y %H:%M:%S",
            errors="coerce"
        )

        df = df.dropna(subset=["datetime"])

        # Convert kWh counter correctly
        df["kWh_counter"] = pd.to_numeric(df["kWh_counter"], errors="coerce")

        df = df.dropna(subset=["kWh_counter"])

        # Sort just in case
        df = df.sort_values("datetime")

        # Calculate daily energy
        energy = df["kWh_counter"].iloc[-1] - df["kWh_counter"].iloc[0]

        date = df["datetime"].dt.date.iloc[0]

        daily_results.append([date, energy])

    except Exception as e:
        print(f"Skipping {file}: {e}")

# Create dataframe
daily = pd.DataFrame(daily_results, columns=["date", "energy_kWh"])

# Save
daily.to_csv("daily_energy.csv", sep=";", index=False)

print("\n? Done! (using kWh counter - accurate)")