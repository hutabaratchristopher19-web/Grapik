import sqlite3
import matplotlib.pyplot as plt

def get_data(start_date, end_date):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE date BETWEEN ? AND ? ORDER BY date", (start_date, end_date))
    res = cur.fetchall()
    con.close()
    dates = [res[i][0] for i in range(len(res))]
    prices = [res[i][1] for i in range(len(res))]
    return dates, prices

def viz_data(dates, prices):
    plt.figure(figsize=(8,6))
    plt.plot(dates, prices, marker='o', color='b', linestyle='-')
    plt.title('Grafik Harga')
    plt.xlabel('Tanggal')
    plt.ylabel('Harga')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    start_date = '2001-04-12'
    end_date = '2023-10-12'
    dates, prices = get_data(start_date, end_date)
    viz_data(dates, prices)
