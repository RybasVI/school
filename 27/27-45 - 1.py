Fin = open("27-45b.txt")

N = int(Fin.readline())

s1 = s2 = s3 = 0
fl = False
minAC1 = 1e10
minAC2 = 1e10
minBC1 = 1e10
minBC2 = 1e10
nminAC1 = -1
nminBC1 = -1
for i in range(N):
  a, b, c = map( int, Fin.readline().split() )
  a, b, c = sorted( [a, b, c] )[::-1]
  s1 += a
  s2 += b
  s3 += c
  if (a - b) % 2 == 1:
    fl = True
  if (a - c) % 2 == 1:
    if a - c < minAC1:
      minAC2=minAC1
      minAC1 = a-c
      nminAC1=i
    elif a - c < minAC2:
      minAC2 = a-c
  if (b - c) % 2 == 1:
    if b - c < minBC1:
      minBC2=minBC1
      minBC1 = b-c
      nminBC1=i
    elif b - c < minBC2:
      minBC2 = b-c
  #print(minAC1, minAC2, minBC1, minBC2)

Fin.close()

print( 's1 =', s1, 's2 =', s2 )
print( 's3 =', s3 )
print( 'b <-> a:', fl )
print( 'c <-> a:', minAC1, ' ' , minAC2 )
print( 'c <-> b:', minBC1, ' ' , minBC2 )

print("Ответ:")
if s1 % 2 == 1  and  s2 % 2 == 1:
  print( s3 )
elif s1 % 2 != 1 and s2 % 2 != 1:
  if fl:
    print( s3 )
  else:
    d = min(minAC1+minBC2, minAC2+minBC1, minAC1 + minAC2, minBC1+minBC2)
    if nminAC1 != nminBC1:
      d = min( d, minAC1 + minBC1 )
    print( s3 + d )
elif s1 % 2 != 1:
  print( s3 + minAC1 )
elif s2 % 2 != 1:
  print( s3 + minBC1 )


