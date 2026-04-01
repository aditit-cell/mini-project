import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import joblib

# STEP 1: Load dataset
df = pd.read_csv("../results/coverage_log.csv")

print("Dataset loaded:")
print(df.head())

# STEP 2: Encode categorical features
le_a = LabelEncoder()
le_b = LabelEncoder()

df['a_type_enc'] = le_a.fit_transform(df['a_type'])
df['b_type_enc'] = le_b.fit_transform(df['b_type'])

# STEP 3: Define features and target
X = df[['opcode', 'a_type_enc', 'b_type_enc']]
y = df['gain_label']   # IMPORTANT

# STEP 4: Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("Model trained!")

# STEP 5: Predict probability of coverage gain
df['predicted_gain'] = model.predict_proba(X)[:, 1]

# STEP 6: Sort testcases
df_sorted = df.sort_values(by='predicted_gain', ascending=False)

print("Top prioritized testcases:")
print(df_sorted.head())

# STEP 7: Save prioritized list
df_sorted.to_csv("prioritized_tests.csv", index=False)
print("Saved prioritized_tests.csv")

# STEP 8: Save model for pyuvm use
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")

# STEP 9: Plot graph
plt.plot(df_sorted['predicted_gain'].values)
plt.title("Testcase Priority Curve")
plt.xlabel("Testcases")
plt.ylabel("Predicted Coverage Gain")
plt.savefig("priority_plot.png")
print("Plot saved as priority_plot.png")