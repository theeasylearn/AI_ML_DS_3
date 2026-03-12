import pandas as pd
import re
import os

folder = "."  # same folder as your files

def extract_race(meaning):
    if pd.isna(meaning) or not meaning:
        return "indian"
    match = re.search(r'\(([^)]+)\)', str(meaning))
    return match.group(1).strip().lower() if match else "indian"

all_rows = []

# 1. baby_names_final(1).csv (has mixed races)
df1 = pd.read_csv(os.path.join(folder, "baby_names_final(1).csv"))
for _, row in df1.iterrows():
    name = str(row['Name']).strip()
    if re.search(r'\d', name) or not name: continue
    gender_raw = str(row['Gender']).strip()
    gender = {'Male':'m', 'Female':'f', 'Boy':'m', 'Girl':'f', 'Both':'both'}.get(gender_raw, gender_raw.lower())
    if gender not in ['m','f','both']: continue
    meaning = str(row['Meaning']).strip()
    race = extract_race(meaning)
    all_rows.append({'name':name, 'gender':gender, 'meaning':meaning, 'race':race})

# 2. All pure Indian files
indian_files = [
    "indian_baby_names_100k.csv",
    "indian_baby_names_50k.csv",
    "indian_baby_names_10000.csv"
]
for f in indian_files:
    df = pd.read_csv(os.path.join(folder, f))
    for _, row in df.iterrows():
        name = str(row.get('name') or row.get('Name')).strip()
        if re.search(r'\d', name) or not name: continue
        gender_raw = str(row.get('gender') or row.get('Gender')).strip()
        gender = {'Boy':'m', 'Girl':'f', 'Both':'both'}.get(gender_raw, gender_raw.lower())
        if gender not in ['m','f','both']: continue
        meaning = str(row.get('meaning') or row.get('Meaning')).strip()
        all_rows.append({'name':name, 'gender':gender, 'meaning':meaning, 'race':'indian'})

# 3. All batch Excel files
batch_files = ["batch_1_clean_names_meaning.xlsx", "batch_2_clean_names_meaning.xlsx",
               "batch_3_clean_names_meaning.xlsx", "batch_4_clean_names_meaning.xlsx"]
for f in batch_files:
    df = pd.read_excel(os.path.join(folder, f))
    for _, row in df.iterrows():
        name = str(row['name']).strip()
        if re.search(r'\d', name) or not name: continue
        gender_raw = str(row['gender']).strip()
        gender = {'m':'m', 'f':'f', 'Male':'m', 'Female':'f', 'Both':'both'}.get(gender_raw.lower(), gender_raw.lower())
        if gender not in ['m','f','both']: continue
        meaning = str(row.get('meaning', '')).strip()
        all_rows.append({'name':name, 'gender':gender, 'meaning':meaning, 'race':'indian'})

# Final cleanup
df = pd.DataFrame(all_rows)
df.drop_duplicates(subset=['name', 'gender', 'meaning'], inplace=True)
df = df.sort_values('name').reset_index(drop=True)

df.to_csv('allnames.csv', index=False)
print(f"✅ Success! allnames.csv created with {len(df):,} rows")
print("\nPreview (real races now included):")
print(df.head(10)[['name', 'gender', 'meaning', 'race']])