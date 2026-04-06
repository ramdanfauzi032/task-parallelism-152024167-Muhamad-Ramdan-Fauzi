import multiprocessing

def hitung_rata(data):
    rata = sum(data) / len(data)
    print("Rata-rata:", rata)

def nilai_tertinggi(data):
    print("Nilai tertinggi:", max(data))

def nilai_terendah(data):
    print("Nilai terendah:", min(data))

if __name__ == "__main__":
    print("Nama: Muhamad Ramdan Fauzi")
    print("NRP: 167 (Task Parallelism)")

    data_nilai = [75, 80, 90, 65, 85, 70]

    p1 = multiprocessing.Process(target=hitung_rata, args=(data_nilai,))
    p2 = multiprocessing.Process(target=nilai_tertinggi, args=(data_nilai,))
    p3 = multiprocessing.Process(target=nilai_terendah, args=(data_nilai,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()