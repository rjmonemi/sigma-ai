from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load dummy data
data = pd.read_csv("faults.csv")

@app.route("/")
def home():
    records = data.to_dict(orient="records")
    return render_template("index.html", data=records)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
