def show_menu():
  print(f"Soal Menghitung Metode Numerik Dengan Metode Gaus Siedel")

  print("\nMain Menu")
  print("------------------------------------------------")
  print(" ")
  print("| [1]. [0,0,0] => Masukan Angka Baris Pertama  |")
  print("| [2]. [0,0,0] => Masukan Angka Baris Kedua    |")
  print("| [3]. [0,0,0] => Masukan Angka Baris Ketiga   |")
  print("------------------------------------------------")
  print("| [4]. Masukan Tebakan Awal                    |")
  print("| [5]. Masukan Batas Toleransi                 |")
  print("------------------------------------------------")
  print("| [6]. Hitung Literasi                         |")
  print("| [7]. Hitung Galat                            |")
  print("------------------------------------------------")
  print("| [8]. Exit                                    |")
  print(" ")
  print("------------------------------------------------")


    

def main_menu():
  show_menu()
  matrik = []
  variabel = []
  batas = None
  tebakan = None
  literasi = None

  while True:    
    choice = input("Pilihan (1-7): ")
    

    if choice == '1':
      mylist = [] # Array Sementara           
      for i in range(3):
        br1 = int(input(f"Masukan Soal X{i+1}= ")) # Input Untuk Memasukan Baris Pertama X1
        mylist.append(br1) # Memasukan Ke Dalam Array Sementara
      matrik.insert(0,mylist) # Memasukan Kedalam Array Induk
      const = int(input("Masukan Variabel = ")) # Input Variabel Dari Baris Pertama
      variabel.append(const) # Memasukan Kedalam Induk Variabel   
      pass
    elif choice == '2':
      mylist2 = [] # Array Sementara
      for i in range(3):
        br2 = int(input(f"Masukan Soal X{i+1}= ")) # Input Untuk Memasukan Baris Kedua X2
        mylist2.append(br2) # Memasukan Ke Dalam Array Sementara
      matrik.insert(1,mylist2) # Memasukan Kedalam Array Induk
      const2 = int(input("Masukan Variabel = "))# Input Variabel Dari Baris Kedua
      variabel.append(const2) # Memasukan Kedalam Induk Variabel   
      pass
    elif choice == '3':
      mylis3 = [] # Array Sementara
      for i in range(3):
        br3 = int(input(f"Masukan Soal X{i+1}= ")) # Input Untuk Memasukan Baris Ketiga X3
        mylis3.append(br3) # Memasukan Ke Dalam Array Sementara
      matrik.insert(2,mylis3) # Memasukan Kedalam Array Induk
      const3 = int(input("Masukan Variabel = ")) # Input Variabel Dari Baris Kedua
      variabel.append(const3)  # Memasukan Kedalam Induk Variabel   
      pass
    elif choice == '5':
      mylist4 = [] # Array Sementara
      for i in range(3):
        bts = float(input(f"Masukan Batas Toleransi X{i+1} = ")) # Menginput Batas Toleransi
        mylist4.insert(i,bts) # Memasukan Kedalam Array Sementara
      batas = mylist4 # Mmeasukannya Ke Sebuah Variabel
      pass
    elif choice == '4':
      if tebakan is not None:
        tebakan.clear()
      listtebakan = []
      listliterasi = []
      for i in range(3):
        tbkn = float(input(f"Masukan Tebakan Awal x{i+1} = ")) # Menginput Tebakan Awal
        listtebakan.insert(i,tbkn) # Mmeasukan Kedalam Array listtebakan
        listliterasi.insert(i,tbkn) # Memasukan Kedalam Array Listebakan     
      tebakan = listtebakan # Memasukan Array List Tebakan Kedalam Variabel
      literasi = listliterasi # Memasukan Array list Tebakan Kedalam Variabel     
      pass
    
    elif choice == '8':
      print("Exit Program") # Exit Program / Berhenti Pada Program
      break

    elif choice == '6': # Menghitung Literasi     
      if len(matrik) < 3 :
        print("Data Soal Belum Terpenuhi")        
        break
      # Langkah 1 Membuat Persamaan Linear & Literasi
      x1_ = matrik[0]
      angkaTerbesarx1 = abs(max(x1_,key=abs)) # Mcencari Angka Terbesar Tanpa Melihat Angka Tersebut  - / +

      x2_ = matrik[1]
      angkaTerbesarx2 = abs(max(x2_,key=abs)) # Mencari Angka Terbesar Tanpa Melihat Angka Tersebut  - / +

      x3_ = matrik[2]
      angkaTerbesarx3 = abs(max(x3_,key=abs)) # Mencari Angka Terbesar Tanpa Melihat Angka Tersebut  - / +

      x1 = None
      x2 = None
      x3 = None


      # x1 
      if angkaTerbesarx1 in map(abs,x1_): # Cek Jika Ada 
        mylist = [] # Array Sementara
        for i in range(len(x1_)):
          if abs(x1_[i] ) == angkaTerbesarx1: # Jika Angka Di X1 Sama atau Ada Pada Soal Baris Pertama
            x1_.pop(i) # Hilangkan / Tidak Diambil Sata menghitung 
            literasi.pop(i) # Hilangkan / Tidak Diambil Sata menghitung
            break 
        for i in range(len(x1_)): 
          if x1_[i] < 0: # Ini Untuk Mengecek Jika Terdapat Angka Negatif Pada Angka Terbesarnya
            x1_[i] = abs(x1_[i]) # Menghilangkan Tanda Negatifnya
          else:
            x1_[i] = -abs(x1_[i]) # Jika Ada Positif Ubah Menjadi Negatif        
          a = (x1_[i] * literasi[i]) # Lakukan Perkalian Pada Literasi
          mylist.append(a) # Masukan Kedalam Array Sementara Pada Index Terakhir   
          
        mylist.insert(0,variabel[0]) # Masukan Kedalam Array Sementara Pada Index 0 / Kolom Pertama
        x1 = sum(mylist) / angkaTerbesarx1 # Menghitung Lalu Membagi
        duangka = round(x1,2) # Mengambil 2 Angka Di Belkang Koma
        literasi.insert(0,abs(duangka))

      #x2
      if angkaTerbesarx2 in map(abs,x2_): # Sama Seperti Diatas (x2)
        #x2_.remove(angkaTerbesarx2)
        mylist = []
        for i in range(len(x2_)):
          if abs(x2_[i] ) == angkaTerbesarx2:
            x2_.pop(i)
            literasi.pop(i)
            break 
        for i in range(len(x2_)):
          if x2_[i] < 0:
            x2_[i] = abs(x2_[i])
          else:
            x2_[i] = -abs(x2_[i])
          a = (x2_[i] * literasi[i])
          mylist.append(a)    
          
        mylist.insert(0,variabel[1])
        x2 = sum(mylist) / angkaTerbesarx2
        duangka = round(x2,2)
        literasi.insert(1,abs(duangka))

      #x3
      if angkaTerbesarx3 in map(abs,x3_): # Sama Seperti Diatas (x3)
        #x2_.remove(angkaTerbesarx2)
        mylist = []
        for i in range(len(x3_)):
          if abs(x3_[i]) == angkaTerbesarx3:
            x3_.pop(i)
            literasi.pop(i)
            break 
        for i in range(len(x3_)):
          if x3_[i] < 0:
            x3_[i] = abs(x3_[i])
          else:
            x3_[i] = -abs(x3_[i])
          for j in range(len(literasi)):
            if i == j:
              z = x3_[i]*literasi[i]
              mylist.append(z)
        mylist.insert(0,variabel[2])
        x3 = sum(mylist) / angkaTerbesarx3
        duangka = round(x3,2)
        literasi.append(duangka)             
        print(f"Literasi Ditemukan => {literasi}") # Menampilkan Literasi

    elif choice == '7':
      galat = [] # Array Sementara
      for i in range(len(literasi)):
        for j in range(len(tebakan)):
          if i == j:
            calculate = literasi[i] - tebakan[j] # Melakukan Pengurangan
            galat.insert(i,abs(round(calculate,2))) # Membvulatkan Dan Mengambil Dua Angka Di Belakang Koma
                                   
      for i in range(len(batas)):
        if galat[i] < batas[i]: # Jika Semua Galat Lebih Kecil Dari Tolerasnsi 
          print(f"EX{i+1} |{literasi[i]} - {tebakan[i]}| = {galat[i]} < {batas[i]}")
          print(f"Solusi Ditemukan => X{i+1} : {literasi[i]} 'Stop' ")
        else: # Jika Salah Satu Atau Semuanya
          print(f"EX{i+1} |{literasi[i]} - {tebakan[i]}| = {galat[i]} > {batas[i]}")
          print(f"Harus Berlanjut")
      break



 

# Menjalankan Function 
if __name__ == "__main__":
  main_menu()
