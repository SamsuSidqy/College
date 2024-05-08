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
    total,pay,return:longint;
begin
    nota[0].nama_masakan := 'Ayam Geprek';
    nota[0].banyak:=5;
    nota[0].harga:=20000;
    nota[0].total:=100000;
    
    nota[1].nama_masakan := 'Sate Taichan';
    nota[1].banyak:=5;
    nota[1].harga:=15000;
    nota[1].total:=75000;
    
    nota[2].nama_masakan := 'Es Teh Manis';
    nota[2].banyak:=10;
    nota[2].harga:=5000;
    nota[2].total:=50000;
    
    total := nota[0].total + nota[1].total + nota[2].total;
    pay := 250000;
    return := (pay - total);
    writeln('______________________________________________________________');
    writeln('                        Ayam Geprek77');
    writeln('                Jl. Merdeka Raya, NO.01 Surabaya');
    writeln('______________________________________________________________');
    writeln('Nama Pembeli : Muhamad Abi Samsu Sidqi');
    writeln('NO     Nama Masakan            Banyak      Harga       Jumlah');
    writeln('--------------------------------------------------------------');
    
    //Menu Pertama
    write('1');
    write('      ',nota[0].nama_masakan);
    write('             ');
    write(nota[0].banyak);
    write('           ');
    write(nota[0].harga);
    write('      ');
    write(nota[0].total);
    writeln;
    //Menu Kedua
    write('2');
    write('      ',nota[1].nama_masakan);
    write('            ');
    write(nota[1].banyak);
    write('           ');
    write(nota[1].harga);
    write('       ');
    write(nota[1].total);
    writeln;
    //Menu Ketiga
    write('3');
    write('      ',nota[2].nama_masakan);
    write('            ');
    write(nota[2].banyak);
    write('           ');
    write(nota[2].harga);
    write('       ');
    write(nota[2].total);
    writeln;
    writeln('==============================================================');
    writeln('       Total                                          ',total);
    writeln('       Pembayaran                                     ',pay);
    writeln('       Kembalian                                      ',return);
    writeln('==============================================================');
    writeln('                        Terima Kasih');
end.