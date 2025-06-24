from flask import Flask, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

# Load the CSV file
data = pd.read_csv("faults.csv")

# Add dummy risk values if not already in the file
if "predicted_risk" not in data.columns:
    data["predicted_risk"] = [round(random.uniform(0, 1), 2) for _ in range(len(data))]

@app.route("/")
def home():
    records = data.to_dict(orient="records")
    return render_template("index.html", data=records)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
