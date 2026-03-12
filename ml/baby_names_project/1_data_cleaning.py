# ========================================================
# TITANIC DATA CLEANING AND PREPROCESSING PIPELINE
# Single File - Uses only pandas, matplotlib, seaborn
# Developed by: The Easylearn academy
# ========================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("=== BABY DATA CLEANING PIPELINE STARTED ===\n")
# ========================================================
# STEP 1: LOAD THE DATA
# ========================================================
print("STEP 1: Loading Titanic Dataset...")
url = "allnames.csv"
df = pd.read_csv(url)

print(f"Original Shape: {df.shape}")
print(f"No of Columns: {list(df.columns)}")
print("\nFirst 5 rows preview:")
print(df.head())
print("\n" + "="*70)

# # ========================================================
# # STEP 2: REMOVE DUPLICATES
# ========================================================
print("STEP 2: Removing Duplicates...")
print(f"Duplicates found: {df.duplicated(['name']).sum()}")
df = df.drop_duplicates(['name']) #remove duplicates in dataframe 
print(f"Shape after removing duplicates: {df.shape}")
print("="*70)

# # ========================================================
# # STEP 3: IDENTIFY COLUMN TYPES
# # ========================================================
print("STEP 3: Identifying Categorical & Numerical Columns...")
cat_cols = []
num_cols = []

for col in df.columns:           # go through every column name
    if df[col].dtype == 'object':
        cat_cols.append(col)     # text → categorical
    else:
        num_cols.append(col)     # number → numerical

print("Categorical columns :", cat_cols)
print("Numerical columns   :", num_cols)
print("Unique values in categorical columns:")
print(df[cat_cols].nunique())
print("="*70)

# # ========================================================
# # STEP 4: MISSING VALUES ANALYSIS
# # ========================================================
print("STEP 4: Missing Values Analysis...")
missing = round((df.isnull().sum() / len(df)) * 100, 2)
print(missing.sort_values(ascending=False))
print("="*70)

# # ========================================================
# # STEP 10: SEPARATE FEATURES (X) & TARGET (y)
# # ========================================================
print("STEP 10: Separating Features & Target...")
X = df[['name','gender','meaning','race']].copy()
y = df['name'].copy()
print(f"Features (X) shape: {X.shape}")
print(f"Target (y) shape  : {y.shape}")
print("="*70)

# # ========================================================
# print("STEP 11: Categorical Encoding...")
# # Sex: male=0, female=1
X['gender'] = X['gender'].map({'f': 0, 'm': 1,'both':2})

print("After Encoding - First 5 rows of X:")
print(X.head())
print(f"Final X columns: {list(X.columns)}")
print("="*70)

