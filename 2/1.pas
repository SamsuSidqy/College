program matriksjumlah02;
uses crt;
type
matrix=array[1..2,1..3] of byte;
var
s,k : matrix;
i,j : integer;
procedure input(var x:matrix);
begin
writeln;
  for i:=1 to 2 do
    begin
  for j:=1 to 3 do
    begin
    write('Masukkan matrix[',i,',',j,'] : ');
    readln(x[i,j]);
    end;
   end;
  end;
procedure show(var x:matrix);
begin
writeln;
    for i:=1 to 2 do
      begin
    for j:=1 to 3 do
      begin
      write(x[i,j]:4);
      end;
      writeln;
     end;
    writeln;
end;
{Main Program}
begin
writeln('Matriks I');
Input(s);
writeln('Matriks II');
input(k);
writeln('Matriks I : ');
show(s);
writeln('Matriks II : ');
show(k);

writeln('Hasil Penjumlahan Matriks I dan Matriks II : ');
    for i:=1 to 2 do
     begin
    for j:=1 to 3 do
     begin
     write((s[i,j]+k[i,j]):4);
     end;
     writeln;
    end;
readln;
end.