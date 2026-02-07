import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["A","B","C","D"],
    "Sales":[120,90,150,60]
}

df = pd.DataFrame(data)
print(df)

df.plot(x="Product",y="Sales",kind="bar",legend=False)
plt.title("Product sales")
plt.ylabel("Unit sold")
plt.savefig("sales_graph.png")
plt.show()  

# TASK 2 : LINEAR REGRESSION

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# 1.Load Kaggle dataset

df = pd.read_csv("train.csv")

# 2.Select important features
X = df[["GrLivArea", "BedroomAbvGr", "FullBath"]]
y = df["SalePrice"]


# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42
)
# 4.Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5.Predict
y_pred = model.predict(X_test)

# 6.Evaluate model
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:",mae)                          