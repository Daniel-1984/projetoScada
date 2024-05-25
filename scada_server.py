import random
import sqlite3
import time

# Cria ou conecta a um banco de dados SQLite
conn = sqlite3.connect('scada.db')
c = conn.cursor()

# Cria uma tabela para armazenar os dados dos sensores
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                temperature REAL,
                pressure REAL,
                battery REAL,
                valve_status INTEGER)''')
conn.commit()

def read_sensors():
    # Simula a leitura dos sensores
    temperature = random.uniform(20.0, 25.0)  # Temperatura entre 20 e 25 graus Celsius
    pressure = random.uniform(100.0, 1100.0)  # Pressão entre 100 e 1100 Pa
    battery = random.uniform(11.0, 14.0)      # Bateria entre 11 e 14 Volts
    valve_status = random.choice([0, 1])      # Válvula fechada (0) ou aberta (1)
    return temperature, pressure, battery, valve_status

def log_data():
    while True:
        temperature, pressure, battery, valve_status = read_sensors()
        # Insere os dados no banco de dados
        c.execute("INSERT INTO sensor_data (temperature, pressure, battery, valve_status) VALUES (?, ?, ?, ?)", 
                  (temperature, pressure, battery, valve_status))
        conn.commit()
        print(f"Logged data - Temperature: {temperature}, Pressure: {pressure}, Battery: {battery}, Valve Status: {valve_status}")
        time.sleep(5)  # Simula a coleta de dados a cada 5 segundos

if __name__ == "__main__":
    log_data()
