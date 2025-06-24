from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

# Load data
data = pd.read_csv("faults.csv")

# Add dummy risk prediction (random number between 0 and 1)
data["predicted_risk"] = [round(random.uniform(0, 1), 2) for _ in range(len(data))]

@app.route("/")
def home():
    records = data.to_dict(orient="records")
    return render_template("index.html", data=records)

if __name__ == "__main__":
    app.run(debug=True)
