Program prosedur04(output);
var
i,N :Integer;
a,t,L :Real;
//Mendefinisikan prosedur
procedure HitungLuasSegitiga(alas, tinggi :real;
    var luas : real); 
begin
    luas:=(alas*tinggi)/2;
end;
begin
    write('Banyaknya segitiga : ');readln(N);
    for i:=1 to N do
begin
    writeln ('HITUNG LUAS SEGITIGA-',i);
        write ('Masukan alas : ');readln(a);
            write ('Masukan tinggi : ');readln(t);
    //Memanggil prosedur
    HitungLuasSegitiga(a,t,L);
        writeln('Luas segitiga = ',L:0:2);
            writeln();
end;
readln;

end.

