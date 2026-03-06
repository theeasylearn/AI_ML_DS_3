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

# ========================================================
# STEP 8: REMOVE OUTLIERS (Z-score method)
# ========================================================
print("STEP 8: Removing Outliers using Z-score...")
mean_age = df['Age'].mean()
std_age = df['Age'].std()
lower_bound = mean_age - 2 * std_age
upper_bound = mean_age + 2 * std_age

print(f"Lower Bound: {lower_bound:.2f} | Upper Bound: {upper_bound:.2f}")

df_clean = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

print(f"Rows before outlier removal: {df.shape[0]}")
print(f"Rows after outlier removal : {df_clean.shape[0]}")
print("="*70)

# ========================================================
# STEP 9: FINAL VERIFICATION
# ========================================================
print("STEP 9: Final Verification...")
print("Any missing values left?")
print(df_clean.isnull().sum())
print(f"\nClean dataset ready! Final Shape: {df_clean.shape}")
print("="*70)

# ========================================================
# STEP 10: SEPARATE FEATURES (X) & TARGET (y)
# ========================================================
print("STEP 10: Separating Features & Target...")
X = df_clean[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']].copy()
y = df_clean['Survived'].copy()

print(f"Features (X) shape: {X.shape}")
print(f"Target (y) shape  : {y.shape}")
print("="*70)

# ========================================================
print("STEP 11: Categorical Encoding...")
# Sex: male=0, female=1
X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})

# Embarked: One-Hot Encoding using pandas
X = pd.get_dummies(X, columns=['Embarked'], drop_first=True)

print("After Encoding - First 5 rows of X:")
print(X.head())
print(f"Final X columns: {list(X.columns)}")
print("="*70)

# ========================================================
# STEP 12: FEATURE SCALING (Manual Functions - No sklearn)
# ========================================================
print("STEP 12: Feature Scaling...")

def min_max_scale(df, columns):
    """Manual Min-Max Scaling to range 0-1"""
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = df[col]/max_val
    return df

def standard_scale(df, columns):
    """Manual Standardization (mean=0, std=1)"""
    for col in columns:
        mean = df[col].mean()
        std = df[col].std()
        df[col] = (df[col] - mean) / std
    return df

num_cols_to_scale = ['Age', 'Fare', 'SibSp', 'Parch']

# Create two scaled versions
X_minmax = min_max_scale(X.copy(), num_cols_to_scale)
X_standard = standard_scale(X.copy(), num_cols_to_scale)

print("Scaling completed successfully!")
print("Example - First 5 rows after Standardization (recommended for most models):")
print(X_standard.head().round(4))
print("="*70)
# ========================================================
# FINAL SUMMARY + VISUALIZATION
# ========================================================
print("\nCOMPLETE PIPELINE FINISHED SUCCESSFULLY!")
print("You now have two ready-to-use feature sets:")
print("   • X_standard → Recommended for most ML models")
print("   • X_minmax   → Good for neural networks / distance-based algorithms")
print("   • y          → Target variable")
print(f"Final shape     : {X_standard.shape}")

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X_standard.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap After Full Preprocessing')
plt.tight_layout()
plt.show()


