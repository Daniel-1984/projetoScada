from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    conn = sqlite3.connect('scada.db')
    c = conn.cursor()
    c.execute("SELECT timestamp, temperature, pressure, battery, valve_status FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
    data = c.fetchall()
    conn.close()

    formatted_data = []
    for row in data:
        formatted_data.append({
            "timestamp": row[0],
            "temperature": row[1],
            "pressure": row[2],
            "battery": row[3],
            "valve_status": row[4],
            "record_time": row[0],
            "message_time": row[0]
        })
    return jsonify(formatted_data)

if __name__ == "__main__":
    app.run(debug=True)
