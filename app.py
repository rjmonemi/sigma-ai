from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

def load_data():
    df = pd.read_csv("faults.csv")
    # Calculate predicted risk safely
    def compute_risk(row):
        if pd.isna(row.get('failure_occurred')) or pd.isna(row.get('last_maintenance_date')):
            return 0.0
        return 0.95 if row['failure_occurred'].strip().lower() == 'yes' else 0.25
    df['predicted_risk'] = df.apply(compute_risk, axis=1)
    return df.to_dict(orient='records')

@app.route('/')
def home():
    data = load_data()
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
