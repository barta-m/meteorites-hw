import requests
import pandas as pd
import os
import sys


# Fetching
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# Analysis
def analyze_data(data):
    df = pd.DataFrame(data)

    # Cleaning
    if "mass" in df.columns:
        df["mass"] = pd.to_numeric(df["mass"], errors="coerce")
    elif "mass (g)" in df.columns:
        df["mass"] = pd.to_numeric(df["mass (g)"], errors="coerce")

    if "year" in df.columns:
        df["year_extracted"] = df["year"].astype(str).str[:4]

    # Logic
    count = len(df)

    max_mass_row = df.loc[df["mass"].idxmax()]
    max_mass_name = max_mass_row["name"]
    max_mass_val = max_mass_row["mass"]

    year_counts = df["year_extracted"].value_counts()
    top_year = year_counts.index[0]
    top_year_count = year_counts.iloc[0]

    return {
        "count": count,
        "max_mass_name": max_mass_name,
        "max_mass_val": max_mass_val,
        "top_year": top_year,
        "top_year_count": top_year_count,
    }


# 3. Main Execution
if __name__ == "__main__":
    url = "https://dmachek.github.io/meteorites-homework/meteorite_landings.json"
    try:
        raw_data = fetch_data(url)
        results = analyze_data(raw_data)

        # Format output
        output = f"""
        --- RESULTS ---
        1. Number of entries: {results['count']}
        2. Most massive meteorite: {results['max_mass_name']} (Mass: {results['max_mass_val']} g)
        3. Most frequent year: {results['top_year']} (Count: {results['top_year_count']} entries)
        """
        print(output)

        # Append results to the summary file in GH Actions
        if "GITHUB_STEP_SUMMARY" in os.environ:
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
                f.write("### ☄️ Meteorite Analysis Results\n")
                f.write(f"- **Total Entries:** {results['count']}\n")
                f.write(
                    f"- **Heaviest Meteorite:** {results['max_mass_name']} ({results['max_mass_val']}g)\n"
                )
                f.write(
                    f"- **Top Year:** {results['top_year']} ({results['top_year_count']} landings)\n"
                )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
