program TugasStrukturData;

type
  Node = record
    Data: integer;
    Next: ^Node;
  end;
  LinkedList = ^Node;

var
  Head: LinkedList;

procedure InitializeLinkedList(var List: LinkedList);
begin
  List := nil;
end;

procedure InsertData(var List: LinkedList; Value: integer);
var
  NewNode, CurrentNode, PreviousNode: LinkedList;
begin
  New(NewNode);
  NewNode^.Data := Value;
  NewNode^.Next := nil;

  if List = nil then
    List := NewNode
  else
  begin
    CurrentNode := List;
    PreviousNode := nil;

    while (CurrentNode <> nil) and (Value > CurrentNode^.Data) do
    begin
      PreviousNode := CurrentNode;
      CurrentNode := CurrentNode^.Next;
    end;

    if PreviousNode = nil then
    begin
      NewNode^.Next := List;
      List := NewNode;
    end
    else
    begin
      PreviousNode^.Next := NewNode;
      NewNode^.Next := CurrentNode;
    end;
  end;
end;

procedure DeleteData(var List: LinkedList; Value: integer);
var
  CurrentNode, PreviousNode, TempNode: LinkedList;
begin
  CurrentNode := List;
  PreviousNode := nil;

  while (CurrentNode <> nil) and (CurrentNode^.Data <> Value) do
  begin
    PreviousNode := CurrentNode;
    CurrentNode := CurrentNode^.Next;
  end;

  if CurrentNode <> nil then
  begin
    if PreviousNode = nil then
      List := CurrentNode^.Next
    else
      PreviousNode^.Next := CurrentNode^.Next;

    Dispose(CurrentNode);
  end;
end;

procedure DisplayData(List: LinkedList);
var
  CurrentNode: LinkedList;
begin
  CurrentNode := List;

  writeln('Menampilkan Data:');
  while CurrentNode <> nil do
  begin
    writeln(CurrentNode^.Data);
    CurrentNode := CurrentNode^.Next;
  end;
end;

var
  Choice, Data: integer;

begin
  InitializeLinkedList(Head);
  write('Nama = Muhamad Abi Samsu Sidqi 2');
  write('Kelas = R3Q ');
  write('NPM = 202243501611');
  repeat
    writeln;
    writeln('1. Tambah Data');
    writeln('2. Hapus Data');
    writeln('3. Tampilkan Data');
    writeln('0. Keluar');
    write('Pilih operasi: ');
    readln(Choice);

    case Choice of
      1:
      begin
        write('Masukkan data yang ingin ditambahkan: ');
        readln(Data);
        InsertData(Head, Data);
      end;
      2:
      begin
        write('Masukkan data yang ingin dihapus: ');
        readln(Data);
        DeleteData(Head, Data);
      end;
      3:
        DisplayData(Head);
    end;
  until Choice = 0;

end.
