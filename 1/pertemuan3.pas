program input_dasar;
uses crt;
var 
 nama,kelas,matakuliah,NPM : String;
 absen,tugas,uts,uas : Integer;
begin
 clrscr;
  write   ('Masukkan Nama Anda: ');
  Readln (nama);
  write   ('Masukan NPM: ');
  Readln (NPM);
  write   ('Masukkan Kelas Anda: ');
  Readln (kelas);
  write   ('Masukkan Mata Kuliah Anda: ');
  Readln (matakuliah);
  write   ('Masukkan Nilai Absensi Anda: ');
  Readln (absen);
  write   ('Masukkan Nilai Tugas Anda: ');
  Readln (tugas);
  write   ('Masukkan Nilai UTS Anda: ');
  Readln (uts);
  write   ('Masukkan Nilai UAS Anda: ');
  Readln (uas);

  writeln ('_____________________');
  writeln ('Nama Saya :  ', nama);
  writeln ('NPM Saya :  ', npm);
  writeln ('Kelas Saya :  ', kelas);
  writeln ('Mata Kuliah Saya :  ', matakuliah);
  writeln ('Nilai Absen :  ', absen);
  writeln ('Nilai Tugas :  ', tugas);
  writeln ('Nilai UTS :  ', uts);
  writeln ('Nilai UAS :  ', uas);
  writeln ('Nilai Akhir:  ', absen*0.1+tugas*0.2+uts*0.3+uas*0.4);
  readln;
end.