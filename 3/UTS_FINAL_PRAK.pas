Program HelloWorld(output);
type
    kop =
        record
            nama_masakan:string[20];
            banyak:integer;
            harga:integer;
            total:longint;
        end;
var
    nota : array[0..5] of kop;
    total,pay,return,c:longint;
    a,i:integer;
begin
    
    write('Total Pesanan = ');readln(a);
    for i:= 1 to a do
        begin
            write('Nama Masakan = ');readln(nota[i].nama_masakan);
            write('Banyak = ');readln(nota[i].banyak);
            write('Harga = ');readln(nota[i].harga);
            nota[i].total := nota[i].banyak*nota[i].harga;
            
        end;
    
    writeln;
    writeln('______________________________________________________________');
    writeln('                        Ayam Geprek77');
    writeln('                Jl. Merdeka Raya, NO.01 Surabaya');
    writeln('______________________________________________________________');
    writeln('Nama Pembeli : Muhamad Abi Samsu Sidqi');
    writeln('NO     Nama Masakan            Banyak      Harga       Jumlah');
    writeln('--------------------------------------------------------------');
    
    for i := 1 to a do
        begin
            write(i);
            write('      ',nota[i].nama_masakan);
            write('             ');
            write(nota[i].banyak);
            write('           ');
            write(nota[i].harga);
            write('      ');
            write(nota[i].total);
            writeln;
        end;
     total := nota[1].total + nota[2].total + nota[3].total;
     pay := 250000;
     return := (pay - total);
    writeln('==============================================================');
    writeln('       Total                                          ',total);
    writeln('       Pembayaran                                     ',pay);
    writeln('       Kembalian                                      ',return);
    writeln('==============================================================');
    writeln('                        Terima Kasih');
end.