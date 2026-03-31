import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# STEP 1: Load dataset
df = pd.read_csv("coverage_data.csv")

print("Dataset loaded:")
print(df.head())

# STEP 2: Define features and target
X = df[['opcode', 'operand_a', 'operand_b']]
y = df['coverage_gain']

# STEP 3: Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

print("Model trained!")

# STEP 4: Predict coverage gain
df['predicted_gain'] = model.predict(X)

# STEP 5: Sort testcases
df_sorted = df.sort_values(by='predicted_gain', ascending=False)

print("Top prioritized testcases:")
print(df_sorted.head())

# STEP 6: Save output
df_sorted.to_csv("prioritized_tests.csv", index=False)

print("Saved prioritized_tests.csv")

# STEP 7: Plot graph
plt.plot(df_sorted['predicted_gain'].values)
plt.title("Testcase Priority Curve")
plt.xlabel("Testcases")
plt.ylabel("Predicted Coverage Gain")
plt.show()
