import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/combined Data.csv")

# Label mapping
label_map = {
    "Normal": 0,
    "Depression": 1,
    "Bipolar": 1,
    "Personality disorder": 1,
    "Anxiety": 2,
    "Stress": 2,
    "Suicidal": 2
}

df["anxiety_level"] = df["status"].map(label_map)

# Keep only needed columns
df = df[["statement", "anxiety_level"]]

# Drop missing values
df = df.dropna()

# Split dataset
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["statement"],
    df["anxiety_level"],
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(train_texts))
print("Testing samples:", len(test_texts))

df.to_csv("dataset/cleaned_anxiety_dataset.csv", index=False)