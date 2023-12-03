import math
from tabulate import tabulate
import os
import sys

def menu():
    while True:
        print("Welcome to gmsaw tools, ada keperluan apa kali ini: \n 1. Ralat \n 2. Aljabar Fisis \n 3. Keluar \n")
        userinput= input("Pilih berdasarkan nomor: ")
        os.system("cls")
        if userinput == "1":
            ralat()
        elif userinput == "2":
            ketidakpastian()
            break
        elif userinput == "3":
            sys.exit()
        else:
            print("Input Error")
            continue

def ralat():
    # Meminta jumlah data dari pengguna
    jumlah_data = int(input("Masukkan jumlah data yang ingin dimasukkan: "))

    # Inisialisasi daftar untuk menyimpan data
    data = []

    # Meminta pengguna untuk memasukkan data sebanyak yang diinginkan
    for i in range(jumlah_data):
        input_data = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(input_data)

    # Menghitung rata-rata data
    rata_rata = sum(data) / jumlah_data

    # Menghitung data dikurangi dengan rata-rata
    data_minus_rata = [x - rata_rata for x in data]

    # Mengkuadratkan setiap data yang dikurangi dengan rata-rata
    data_kuadrat = [x ** 2 for x in data_minus_rata]

    # Menjumlahkan semua hasil kuadrat
    total_kuadrat = sum(data_kuadrat)

    # Format data ke dalam tabel
    table = []

    for i in range(jumlah_data):
        table.append([f"{data[i]:.5f}", f"{rata_rata:.5f}", f"{data_minus_rata[i]:.5f}", f"{data_kuadrat[i]:.30f}"])

    # Tambahkan kolom "Total Kuadrat" dengan format 4 angka di belakang koma
    total_kuadrat_column = ["Total Kuadrat", "", "", f"{total_kuadrat:.5f}"]
    table.append(total_kuadrat_column)

    # Menampilkan tabel dengan menggunakan Tabulate
    headers = ["Data", "rata-rata", "Data - Rata", "Data^2"]
    print(tabulate(table, headers, tablefmt="fancy_grid"))

    # Menghitung n * (n - 1)
    hasil_n_n_minus_1 = jumlah_data * (jumlah_data - 1)

    # Menampilkan hasil n * (n - 1)
    print(f"• n * (n - 1) = {hasil_n_n_minus_1}")

    # Menghitung total hasil kuadrat dibagi n * (n - 1)
    total_kuadrat_dibagi_n_n_minus_1 = total_kuadrat / hasil_n_n_minus_1

    # Menampilkan total hasil kuadrat dibagi n * (n - 1) dalam notasi ilmiah
    print(f"• Total hasil kuadrat / (n * (n - 1)): {total_kuadrat_dibagi_n_n_minus_1:.5e}")

    # Menghitung akar dari total_kuadrat_dibagi_n_n_minus_1
    akar_total = math.sqrt(total_kuadrat_dibagi_n_n_minus_1)

    # Menampilkan akar dalam notasi ilmiah
    print(f"• Akar dari total hasil kuadrat / (n * (n - 1)): {akar_total:.5e}")

    # Mencetak rata-rata bersama dengan Δx dalam format yang diminta
    print(f"• Rata-rata ± Δx = {rata_rata:.5e} ± {akar_total:.5e}")

    # Rumus Δx/rata-rata
    Δx_rata_rata = akar_total / rata_rata

    # Mencetak Δx/rata-rata
    print(f"• Δx/rata-rata = {Δx_rata_rata:.5e}")

    # Ralat Nisibi
    ralat_nisibi = Δx_rata_rata * 100

    # Mencetak Ralat Nisibi
    print(f"• Ralat Nisibi = {ralat_nisibi:.5f}%")

    # Rumus Ralat Kebenaran
    ralat_kebenaran = 100 - ralat_nisibi

    # Mencetak Ralat Kebenaran
    print(f"• Ralat Kebenaran = {ralat_kebenaran:.5f}% \n \n")
def ketidakpastian():
    def jumlah():
        def penjumlahan():
            x_plus_y= x + y
            dx2= dx**2
            dy2= dy**2
            dx2_plus_dy2= dx2 + dy2
            sqrt_result= math.sqrt(dx2_plus_dy2)
            
            print(f"= ({x:.5f} + {y:.5f}) ± √({dx:.5f}^2 + {dy:.5f}^2)")
            print(f"= {x_plus_y:.5f} ± √({dx2:.5f} + {dy2:.5f})")
            print(f"= {x_plus_y:.5f} ± √{dx2_plus_dy2:.5f}")
            print(f"= {x_plus_y:.5f} ± {sqrt_result:.5e} \n")
        
        x= float(input("x: "))
        dx= float(input("Δx: "))
        y= float(input("y: "))
        dy= float(input("Δy: "))
        print(f"{x} ± {dx}")
        print(f"{y} ± {dy}")
        lanjut= str(input("lanjut x + y? (y/1, n/2) : "))
        if lanjut.lower() == "y" or lanjut == "1":
            os.system("cls")
            penjumlahan()
        elif lanjut.lower() == "n" or lanjut == "2":
            os.system("cls")
            jumlah()
        else:
            print("Input error \n")
    def kurang():
        def pengurangan():
            x_min_y= x - y
            dx2= dx**2
            dy2= dy**2
            dx2_plus_dy2= dx2 + dy2
            sqrt_result= math.sqrt(dx2_plus_dy2)
            
            print(f"= ({x:.5f} - {y:.5f}) ± √({dx:.5f}^2 + {dy:.5f}^2)")
            print(f"= {x_min_y:.5f} ± √({dx2:.5f} + {dy2:.5f})")
            print(f"= {x_min_y:.5f} ± √{dx2_plus_dy2:.5f}")
            print(f"= {x_min_y:.5f} ± {sqrt_result:.5e} \n")
        
        x= float(input("x: "))
        dx= float(input("Δx: "))
        y= float(input("y: "))
        dy= float(input("Δy: "))
        print(f"{x} ± {dx}")
        print(f"{y} ± {dy}")
        lanjut= input("lanjut x - y? (y/1, n/2) : ")
        if lanjut.lower() == "y" or lanjut == "1":
            os.system("cls")
            pengurangan()
        elif lanjut.lower() == "n" or lanjut == "2":
            os.system("cls")
            kurang()
        else:
            print("Input error \n")
    def kali():
        def perkalian():
            x_times_y= x * y
            x2= x**2
            y2= x**2
            dx2= dx**2
            dy2= dy**2
            dx2_y2= dx2 * x2
            dy2_x2= dy2 * y2
            total_inside= dx2_y2 + dy2_x2
            sqrt_result= math.sqrt(total_inside)
            
            print(f"= (x * y) ± √(Δx^2*y^2 + Δy^2*x^2)")
            print(f"= ({x:.5f} * {y:.5f}) ± √({dx:.5f}^2 * {y:.5f}^2 + {dy:.5f}^2 * {x:.5f}^2)")
            print(f"= {x_times_y:.5f} ± √({dx2:.5f} * {y2:.5f} + {dy2:.5f} * {x2:.5f})")
            print(f"= {x_times_y:.5f} ± √({dx2_y2:.5f} + {dy2_x2:.5f})")
            print(f"= {x_times_y:.5f} ± √{total_inside:.5e}")
            print(f"= {x_times_y:.5f} ± {sqrt_result:.5e} \n")
        
        x= float(input("x: "))
        dx= float(input("Δx: "))
        y= float(input("y: "))
        dy= float(input("Δy: "))
        print(f"{x} ± {dx}")
        print(f"{y} ± {dy}")
        lanjut= input("lanjut x * y? (y/1, n/2) : ")
        if lanjut.lower() == "y" or lanjut == "1":
            os.system("cls")
            perkalian()
        elif lanjut.lower() == "n" or lanjut == "2":
            os.system("cls")
            kali()
        else:
            print("Input error \n")
    def bagi():
        def pembagian():
            x_divide_y= x / y
            dx_d_y= dx / y
            x_dy= x * dy
            y2= x**2
            x_dy_y2= x_dy / y2
            dx_d_y2= dx_d_y ** 2
            x_dy_y22= x_dy_y2 ** 2
            total_inside= dx_d_y2 + x_dy_y22
            sqrt_result= math.sqrt(total_inside)
            
            print(f"= (x : y) ± √((Δx/y)^2 + (x*Δy/y^2)^2)")
            print(f"= ({x:.5f} : {y:.5f}) ± √( ({dx:.5f}/{y:.5f})^2 + ({x:.5f}{dy:.5f}/{y:.5f}^2)^2 ")
            print(f"= {x_divide_y:.5f} ± √({dx_d_y})^2 + ({x_dy:.5f}/{y:.5f}^2)^2")
            print(f"= {x_divide_y:.5f} ± √({dx_d_y})^2 + ({x_dy_y2})^2")
            print(f"= {x_divide_y:.5f} ± √({dx_d_y2} + {x_dy_y22})")
            print(f"= {x_divide_y:.5f} ± √{total_inside:.5e}")
            print(f"= {x_divide_y:.5f} ± {sqrt_result:.5e} \n")
        
        x= float(input("x: "))
        dx= float(input("Δx: "))
        y= float(input("y: "))
        dy= float(input("Δy: "))
        print(f"{x} ± {dx}")
        print(f"{y} ± {dy}")
        lanjut= input("lanjut x * y? (y/1, n/2) : ")
        if lanjut.lower() == "y" or lanjut == "1":
            os.system("cls")
            pembagian()
        elif lanjut.lower() == "n" or lanjut == "2":
            os.system("cls")
            bagi()
        else:
            print("Input error \n")
    def pangkat():
        def pemangkatan():
            x_p_n= x ** n
            n1= n-1
            x_p_n1= x ** n1
            total_inside= (n * x_p_n1) * (dx)
            
            print(f"= (x)^n ± n(x)^(n-1)(Δx)")
            print(f"= {x:.5f}^({n}) ± {n:.5f}({x:.5f})^({n:.5f}-1)({dx:.5f})")
            print(f"= {x_p_n:.5f} ± {n:.5f} * ({x:.5f})^({n1:.5f}) * {dx:.5f}")
            print(f"= {x_p_n:.5f} ± {n:.5f} * {x_p_n1:.5f} * {dx:.5f}")
            print(f"= {x_p_n:.5f} ± {total_inside:.5e} \n")
        
        x= float(input("x: "))
        dx= float(input("Δx: "))
        n= float(input("Masukan pangkat :"))
        print(f"({x} ± {dx})^{n}")
        lanjut= input("lanjut x ^ n (y/1, n/2) : ")
        if lanjut.lower() == "y" or lanjut == "1":
            os.system("cls")
            pemangkatan()
        elif lanjut.lower() == "n" or lanjut == "2":
            os.system("cls")
            pangkat()
        else:
            print("Input error \n")

    while True:
        print("Pilihan Jenis Operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")
        print("6. Kembali ke Menu \n")
        userinput= str(input("Pilih menurut nomor: "))
        os.system("cls")
        if userinput == "1":
            jumlah()
        elif userinput == "2":
            kurang()
        elif userinput == "3":
            kali()
        elif userinput == "4":
            bagi()
        elif userinput == "5":
            pangkat()
        elif userinput == "6":
            menu()
        else:
            print("Input Tidak Valid")
            continue

menu()
