import pandas as pd

# Load the dataset
df = pd.read_csv('Breast_Cancer.csv')

# Show basic info
print("Breast_Cancer.csv:", df.shape)
print(df.info())

# Step 1: Drop duplicate rows
df = df.drop_duplicates()

# Step 2: Handle missing values
# Option 1: Drop rows with missing values
df = df.dropna()

# Option 2 (alternative): Fill missing numeric values with the median
# df = df.fillna(df.median(numeric_only=True))

# Step 3: Convert categorical columns to lowercase and strip whitespaces
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower().str.strip()

# Step 4: Encode categorical variables (if needed)
# Example: df = pd.get_dummies(df, columns=['column_name'], drop_first=True)

# Step 5: Normalize or scale numeric features (optional)
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# numeric_cols = df.select_dtypes(include='number').columns
# df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Save cleaned dataset
df.to_csv('Breast_Cancer_Cleaned.csv', index=False)

print("Cleaning complete. Cleaned dataset shape:", df.shape)

#1. Identifying the Label Column
print(df.columns)
print(df.head())


#2. Encoding the Label

# Convert labels to binary format (M = 1, B = 0)
df['Age'] = df['A Stage'].map({'M': 1, 'B': 0})

#3. Separate Features and Labels

X = df.drop('Race', axis=1)
y = df['Age']




# Separate features and labels
X = df.drop('Status', axis=1)  # Replace 'diagnosis' with your actual label column
y = df['Age']


#Split
import pandas as pd

df = pd.read_csv('Breast_Cancer.csv')
chunk_size = 1000  # Adjust based on file size
for i, chunk in enumerate(range(0, df.shape[0], chunk_size)):
    df.iloc[chunk:chunk + chunk_size].to_csv(f'Breast_Cancer_part{i + 1}.csv', index=False)


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

