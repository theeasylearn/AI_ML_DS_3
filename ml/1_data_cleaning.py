# ========================================================
# TITANIC DATA CLEANING AND PREPROCESSING PIPELINE
# Single File - Uses only pandas, matplotlib, seaborn
# Developed by: The Easylearn academy
# ========================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("=== TITANIC DATA CLEANING PIPELINE STARTED ===\n")
# ========================================================
# STEP 1: LOAD THE DATA
# ========================================================
print("STEP 1: Loading Titanic Dataset...")
# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
df = pd.read_csv(url)

print(f"Original Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows preview:")
print(df.head())
print("\n" + "="*70)

# ========================================================
# STEP 2: REMOVE DUPLICATES
# ========================================================
print("STEP 2: Removing Duplicates...")
print(f"Duplicates found: {df.duplicated().sum()}")
df = df.drop_duplicates() #remove duplicates in dataframe 
print(f"Shape after removing duplicates: {df.shape}")
print("="*70)

# ========================================================
# STEP 3: IDENTIFY COLUMN TYPES
# ========================================================
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

# ========================================================
# STEP 4: MISSING VALUES ANALYSIS
# ========================================================
print("STEP 4: Missing Values Analysis...")
missing = round((df.isnull().sum() / len(df)) * 100, 2)
print(missing.sort_values(ascending=False))
print("="*70)

# ========================================================
# STEP 5: DROP IRRELEVANT COLUMNS
# ========================================================
print("STEP 5: Dropping Irrelevant Columns...")
irrelevant = ['PassengerId', 'Name', 'Ticket', 'Cabin']
df = df.drop(columns=irrelevant)
print(f"Remaining columns: {list(df.columns)}")
print(f"New Shape: {df.shape}")
print("="*70)

# ========================================================
# STEP 6: HANDLE MISSING VALUES
# ========================================================
print("STEP 6: Handling Missing Values...")
# Drop rows with missing Embarked (only 2 rows)
df = df.dropna(subset=['Embarked'])
# Fill Age with median (more robust for skewed data)
df['Age'] = df['Age'].fillna(df['Age'].median())

print("Missing values after handling:")
print(df.isnull().sum())
print(f"Shape after handling missing: {df.shape}")
print("="*70)

# ========================================================
# STEP 7: DETECT OUTLIERS (Box Plot)
# ========================================================
print("STEP 7: Detecting Outliers in Age...")
plt.figure(figsize=(10, 4))
plt.boxplot(df['Age'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Box Plot - Age (Before Outlier Removal)')
plt.xlabel('Age')
plt.grid(True, alpha=0.3)
plt.show()
