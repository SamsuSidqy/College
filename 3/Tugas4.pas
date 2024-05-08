program StackExample;

const
  MaxStackSize = 100;

type
  Stack = record
    Data: array [1..MaxStackSize] of Char;
    Top: Integer;
  end;

procedure InitializeStack(var S: Stack);
begin
  S.Top := 0;
end;

procedure Push(var S: Stack; Value: Char);
begin
  if S.Top < MaxStackSize then
  begin
    Inc(S.Top);
    S.Data[S.Top] := Value;
  end
  else
    WriteLn('Stack is full. Cannot push more elements.');
end;

function Pop(var S: Stack): Char;
begin
  if S.Top > 0 then
  begin
    Pop := S.Data[S.Top];
    Dec(S.Top);
  end
  else
    WriteLn('Stack is empty.');
end;

function IsEmpty(var S: Stack): Boolean;
begin
  IsEmpty := S.Top = 0;
end;

var
  S: Stack;
  i: Integer;
begin
  InitializeStack(S);

  // Push elements onto the stack
  Push(S, 'e');
  Push(S, 'd');
  Push(S, 'b');
  Push(S, 'c');
  Push(S, 'b');
  Push(S, 'a');

  // Pop elements from the stack and print them
  for i := 1 to 6 do
    Write(Pop(S));

  WriteLn;
end.
