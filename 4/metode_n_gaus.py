
matrik = [

	[4,1,1],
	[0,6,2],
	[1,2,8]

] # Ini Soal

tebakan = [0.85,2.14,2.98] #Tebakan Awal
batas = [0.3,0.3,0.3] # Batas / Toleransi
batas2 = [0.85,2.14,2.98]
variabel = [9,18,29] # Variabel

# Langkah 1 Membuat Persamaan Linear & Literasi
x1_ = matrik[0]
angkaTerbesarx1 = abs(max(x1_,key=abs)) # Mencari Angka Terbesar

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
			tebakan.pop(i)
			break	
	for i in range(len(x1_)):
		if x1_[i] < 0:
			x1_[i] = abs(x1_[i])
		else:
			x1_[i] = -abs(x1_[i])
		a = (x1_[i] * tebakan[i])
		mylist.append(a)		
		
	mylist.insert(0,variabel[0])
	x1 = sum(mylist) / angkaTerbesarx1
	duangka = round(x1,2)
	tebakan.insert(0,abs(duangka))

#x2
if angkaTerbesarx2 in map(abs,x2_):
	#x2_.remove(angkaTerbesarx2)
	mylist = []
	for i in range(len(x2_)):
		if abs(x2_[i] )== angkaTerbesarx2:
			x2_.pop(i)
			tebakan.pop(i)
			break	
	for i in range(len(x2_)):
		if x2_[i] < 0:
			x2_[i] = abs(x2_[i])
		else:
			x2_[i] = -abs(x2_[i])
		a = (x2_[i] * tebakan[i])
		mylist.append(a)		
		
	mylist.insert(0,variabel[1])
	x2 = sum(mylist) / angkaTerbesarx2
	duangka = round(x2,2)
	tebakan.insert(1,abs(duangka))

#x3
if angkaTerbesarx3 in map(abs,x3_):
	#x2_.remove(angkaTerbesarx2)
	mylist = []
	for i in range(len(x3_)):
		if abs(x3_[i]) == angkaTerbesarx3:
			x3_.pop(i)
			tebakan.pop(i)
			break	
	for i in range(len(x3_)):
		if x3_[i] < 0:
			x3_[i] = abs(x3_[i])
		else:
			x3_[i] = -abs(x3_[i])
		for j in range(len(tebakan)):
			if i == j:
				z = x3_[i]*tebakan[i]
				mylist.append(z)
	mylist.insert(0,variabel[2])
	x3 = sum(mylist) / angkaTerbesarx3
	duangka = round(x3,2)
	tebakan.append(duangka)
	



print(tebakan)
print(cekGalat(tebakan,batas2))





# if angkaTerbesarx1 in x1_:
# 	x1_.remove(angkaTerbesarx1)
# 	#print(x1_)
# 	o = variabel[0] - sum(x1_ * tebakan[0])
# 	hasil = o / angkaTerbesarx1
# 	x1 = hasil
# 	#print(angkaTerbesarx1)

# if angkaTerbesarx2 in x2_:
# 	x2_.remove(angkaTerbesarx2)  
# 	if x2_[0] == 0:    
# 		o = variabel[1] - sum(x2_ * tebakan[1])
# 		print(f"KOSONG")
# 	else:
# 		x2_[0] *= x1		
# 		o = variabel[1] - sum(x2_)	
# 	#o = variabel[1] - sum(x2_ * tebakan[1])
# 	print(x2_)
# 	print(sum(x2_))
# 	hasil = o / angkaTerbesarx2
# 	x2= hasil

# if angkaTerbesarx3 in x3_:
# 	x3_.remove(angkaTerbesarx3)
# 	#print(x3_)
# 	x3_[0] = x1
# 	x3_[1] *= x2
# 	#print(x3_)
# 	o = variabel[2] - sum(x3_)
# 	# print(sum(x3_*tebakan[2]))
# 	hasil = o / angkaTerbesarx3
# 	x3 = hasil
# 	#print(angkaTerbesarx3) 

# def cekToleransi(x1,x2,x3):
# 	for i in batas:
# 		if x1 > i:
# 			return True
# 		else:
# 			return False

# print(cekToleransi(x1,x2,x3))


# print(f"X1 => {x1}")
# print(f"X2 => {x2}")
# print(f"X3 => {x3}")	


































