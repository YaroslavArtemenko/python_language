#task1--------------------------------------------------


"""
�����:���� ��� ����� �����. ������� �������� � ���.

������ ����:���������� ������� ���� �����

������� ����:������� ���� ����� 
"""
#
number_1=int(input())

number_2=int(input())

if number_1>=number_2:
   
  print(number_2)

else:

  print(number_1)
#-------------------------------------------------------


#task2--------------------------------------------------


"""
�����: ������� ��������� ������� sign(x), �� ����������� ��������� �����: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

������ ����: ���������� ������� ����� �����.

������� ����: ������� ��������� sign.
"""
#
x=float(input())

if x<0:
    
  print(-1)

if x==0:
   
  print(0)

if x>0:
 
  print(1)
#----------------------------------------------------------


#task3-----------------------------------------------------


"""
�����: ���� ��� ����� �����. ������� �������� � ���.

������ ����: 3 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ���� �����
"""
#
number_1=int(input())

number_2=int(input())

number_3=int(input())

if (number_1<number_2) and (number_1<number_3):
  
  print(number_1)

elif (number_2<number_1) and (number_2<number_3):
    
  print(number_2)

else:
    
  print(number_3)
#------------------------------------------------------------


#task4-------------------------------------------------------


"""
�����: ���� ���� �����, �� ������� ��. ���������, �� � �������� �� ����������. ���� ���, �� ������� ����������� "LEAP", � ������ ������� � "�OMMON".

г� ����������, ���� ���������� ���� � ���� � ����:

�� ������ ����������, ���� ���� ����� ������� �� 4 ��� ������ � �� ������� ��� ������ �� 100
�� ������ ����������, ���� ���� ����� ������� �� 400 ��� ������
������ ����: ���� �����, �� ������� ����������

������� ����: ������� ��������� �����.
"""
#
year = int(input())

if year%400 == 0 or (year%4 == 0 and year%100 !=0):
  
  print('LEAP')

else:
  
  print('COMMON')
#----------------------------------------------------------------


#task5-----------------------------------------------------------


"""
�����: ���� ��� ����� �����. ��������, ������ � ��� ��������� ���� ������. �������� ������� �������� ���� � �����: 3 (���� �� ����� �������), 2 (���� ��� � ��� ��������� ���� ������, � ���� �����������) ��� 0 (���� �� ����� ����).

������ ����: 3 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ���� �����
"""
#
x=int(input())

y=int(input())

z=int(input())

if x==y==z:
   
  print(3)

elif y==x and x!=z:
  
  print(2)

elif y!=x and x==z:
  
  print(2)

elif x!=y and y==z:
  
  print(2)

elif x!=y!=z:
  
  print(0)
#-----------------------------------------------------------------


#task6------------------------------------------------------------


"""
�����: ������ ���� ����������� �� ���������� ��� �� ��������. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ���� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ���� ���� �������� ����������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if x1==x2 or y1==y2:
  
  print("YES")

else:
  
  print("NO")
#--------------------------------------------------------------------


#task7---------------------------------------------------------------


"""
�����: ���� ���������� ���� ����� ������ �����. ���������, �� ���������� ���� �������. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ���� ���������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if (x1+y1)%2==0 and (x2+y2)%2==0:
  
  print("YES")

elif (x1+y1)%2!=0 and (x2+y2)%2!=0:
  
  print("YES")

else:
  
  print("NO")
#


#task8---------------------------------------------------------------


"""
�����: ������� ������ ����������� �� ����������, �� �������� ��� �� ������� �� ����-��� ������ �������. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ������ ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1=int(input())

y1=int(input())

x2=int(input())

y2=int(input())

if -1<=(x1-x2)<=1 and -1<=(y1-y2)<=1:
  
  print('YES')

else:
  
  print('NO')
#--------------------------------------------------------------------


#task9---------------------------------------------------------------


"""
������� ���� �������� �� ������� �� ����-��� ������� �����. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ���� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if (x1/x2)==(y1/y2):
  
  print("YES")

elif (x1+y1)==(x2+y2):
  
  print("YES")

else:
  
  print("NO")
#----------------------------------------------------------------------


#task10----------------------------------------------------------------


"""
�����: ������ �������� �������� �� ����������, �� �������� ��� �� ������� �� ����-��� ������� �����. ���� ���������� ���� ����� ������ �����. ���������, �� ���� �������� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if x1==x2 or y1==y2:
  
  print("YES")

elif (x1/x2)==(y1/y2):
  
  print("YES")

elif  (x1+y1)==(x2+y2)  or (x1-y1)==(x2-y2):
  
  print("YES")   

else:
  
  print("NO")

#------------------------------------------------------------------------


#task11------------------------------------------------------------------


"""
�����: ������� ��� �������� �� ����� L. ³� ���� ����������� �� �� ������� �� ���������� � ���� ������� �� �������� ��� �� �� ������� �� �������� � ���� �� ����������. ���� ���������� ���� ����� ������ �����. ���������, �� ���� ��� ������� � ����� ������ � ����� �� ���� ���. ���������� ������� ������ ����� ����� �� 1 �� 8, ����� � ���� ������� ����� ����� �� ��������� ������. ����� ��� ����� - ��� ����� ������, ������� ��� ����� � ��� �����. �������� �� ������� "YES", ���� ��� ��������, ��� "NO" � ������ �������.

������ ����: 4 ����� �����.  ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if abs(x1-x2)==2 and abs(y1-y2)==1:
  
  print("YES")

elif abs(x1-x2)==1 and abs(y1-y2)==2:
  
  print("YES")

else:
  
  print("NO")

#-----------------------------------------------------------------------


#task12-----------------------------------------------------------------


"""
�����: ������� �� ����� ������������, ���������� �� n?m �����. ������� ���� ���� ��������� �� �� ������� ����� �� ���������� ��� �� ��������, ��� ����� ������ ����� ���� ������. ���������, �� ����� �������� ������� �� ���� ���� ����� �����, ��� ���� � ������ ������ ����� k �����. �������� �� ������� "YES", ���� ������� ����� �������, ��� "NO" � ������ �������.

������ ����: 3 ����� �����: n,m, k. ����� ����� ���������� ������� � �������� �����.

������� ����: ������� ��������� �����.
"""
#
������ �12
n = int(input())

m = int(input())

k = int(input())

if n*m-k==n or n*m-k==m and n*m>k and k!=1:
  
  print('YES')

elif (n*m-k)%2==0 and n*m>k and k!=1:
   
  print('YES')

else:
  
  print('NO')
#------------------------------------------------------------------------