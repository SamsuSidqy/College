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

# Membuat Galat & Cek Galat
def cekGalat(literasi,tebakan,tol):
  for i in range(len(literasi)):
    for j in range(len(tol)):
      calculate = literasi[i] - tebakan[j]
      if i == j and  calculate < tol[i]:
        return False
  return True
    

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
      mylist = []            
      for i in range(3):
        br1 = int(input(f"Masukan Soal X{i+1}= "))
        mylist.append(br1)
      matrik.insert(0,mylist)
      const = int(input("Masukan Variabel = "))
      variabel.append(const)    
      pass
    elif choice == '2':
      mylist2 = []
      for i in range(3):
        br2 = int(input(f"Masukan Soal X{i+1}= "))
        mylist2.append(br2)
      matrik.insert(1,mylist2)
      const2 = int(input("Masukan Variabel = "))
      variabel.append(const2)   
      pass
    elif choice == '3':
      mylis3 = []
      for i in range(3):
        br3 = int(input(f"Masukan Soal X{i+1}= "))
        mylis3.append(br3)
      matrik.insert(2,mylis3)
      const3 = int(input("Masukan Variabel = "))
      variabel.append(const3)   
      pass
    elif choice == '5':
      mylist4 = []
      for i in range(3):
        bts = float(input(f"Masukan Batas Toleransi X{i+1} = "))
        mylist4.insert(i,bts)
      batas = mylist4
      pass
    elif choice == '4':
      if tebakan is not None:
        tebakan.clear()
      listtebakan = []
      listliterasi = []
      for i in range(3):
        tbkn = float(input(f"Masukan Tebakan Awal x{i+1} = "))
        listtebakan.insert(i,tbkn)
        listliterasi.insert(i,tbkn)      
      tebakan = listtebakan
      literasi = listliterasi      
      pass
    elif choice == '8':
      print("Exit Program")
      break

    elif choice == '6':      
      if len(matrik) < 3 :
        print("Data Soal Belum Terpenuhi")        
        break
      # Langkah 1 Membuat Persamaan Linear & Literasi
      x1_ = matrik[0]
      angkaTerbesarx1 = abs(max(x1_,key=abs)) # Mcencari Angka Terbesar

      x2_ = matrik[1]
      angkaTerbesarx2 = abs(max(x2_,key=abs)) # Mencari Angka Terbesar

      x3_ = matrik[2]
      angkaTerbesarx3 = abs(max(x3_,key=abs)) # Mencari Angka Terbesar

      x1 = None
      x2 = None
      x3 = None


      # x1 
      if angkaTerbesarx1 in map(abs,x1_): # Cek Jika Ada 
        mylist = []
        for i in range(len(x1_)):
          if abs(x1_[i] )== angkaTerbesarx1:
            x1_.pop(i)
            literasi.pop(i)
            break 
        for i in range(len(x1_)):
          if x1_[i] < 0:
            x1_[i] = abs(x1_[i])
          else:
            x1_[i] = -abs(x1_[i])
          a = (x1_[i] * literasi[i])
          mylist.append(a)    
          
        mylist.insert(0,variabel[0])
        x1 = sum(mylist) / angkaTerbesarx1
        duangka = round(x1,2)
        literasi.insert(0,abs(duangka))

      #x2
      if angkaTerbesarx2 in map(abs,x2_):
        #x2_.remove(angkaTerbesarx2)
        mylist = []
        for i in range(len(x2_)):
          if abs(x2_[i] )== angkaTerbesarx2:
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
      if angkaTerbesarx3 in map(abs,x3_):
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
        print(f"Literasi Ditemukan => {literasi}")
    elif choice == '7':
      galat = [] 
      for i in range(len(literasi)):
        for j in range(len(tebakan)):
          if i == j:
            calculate = literasi[i] - tebakan[j]
            galat.insert(i,abs(round(calculate,2)))
                                   
      for i in range(len(batas)):
        if galat[i] < batas[i]:
          print(f"EX{i+1} |{literasi[i]} - {tebakan[i]}| = {galat[i]} < {batas[i]}")
        else:
          print(f"EX{i+1} |{literasi[i]} - {tebakan[i]}| = {galat[i]} > {batas[i]}")



 


if __name__ == "__main__":
  main_menu()
