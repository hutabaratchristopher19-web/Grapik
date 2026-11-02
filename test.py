import matplotlib.pyplot as plt
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), random_numbers, marker='o', color='r', linestyle='--')
plt.title('Grafik Angka Acak')
plt.xlabel('Indeks')
plt.ylabel('Nilai')
plt.grid(True)
plt.show()
