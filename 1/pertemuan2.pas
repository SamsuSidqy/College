program pertemuan2;
uses crt;

var
a,b,c,d,e,f,g,h:Real;
u:Real;
z:Boolean;

begin
  clrscr;
  a:=10 div 5*4+4-3;
  u:=5*10/2-13+7;
  b:=(10 mod 3)+(5*3+3);
  d:=9 mod 2; //4.5*2mod2
  z:=3+5*3<10;
  
  
  
  WriteLn('Soal No 1= ',a);
  WriteLn('Soal No 2= ',u);
  WriteLn('Soal No 3= ',b);
  WriteLn('Soal No 4= ',d);
  WriteLn('Soal No 5= ',z);

  readln;
end.
