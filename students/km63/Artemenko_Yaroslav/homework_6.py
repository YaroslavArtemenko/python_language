#task1---------------------------------------------------


"""
������ ������� ��������
�������
�������� ��� �������� ������ � ������� ��������� (�� ���� A[0], A[2], A[4], ...).
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range(0,len(elem),2):

        data.append(elem[i])

    return data

def print_data(output_data):

    for i in output_data:

        print (i, end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task2------------------------------------------------------


"""
������ ������� ���������
�������
�������� ��� ������ �������� ������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in elem:

        if int(i)%2==0:

            data.append(i)

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task3------------------------------------------------------


"""
������ ������� �����������
�������
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range(0,len(elem)):

        if i<len(elem)-1:

            if int(elem[i])<int(elem[i+1]):

                data.append(elem[i+1])

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task4------------------------------------------------------


"""
������ ������� ������ �����
�������
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. ���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range (0,len(elem)):

        if len(data)==0:

            if i<len(elem)-1:

                if int(elem[i])*int(elem[i+1])>0:

                    data=[elem[i]]

                    data.append(elem[i+1])

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task5------------------------------------------------------


"""
������ ������� ����� �������
�������
��� ������ �����. ����������, ������� � ���� ������ ���������, ������� ������ ���� ����� �������, � �������� ���������� ����� ���������. 
������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.
"""
#
def input_data():
    data=input().split()
    return data
def operation_data(elem):
    count=0
    for i in range(1,len(elem)-1):
        if int(elem[i-1])<int(elem[i])>int(elem[i+1]):
            count+=1
    return count
def print_data(output_data):
    print(output_data)
print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task6------------------------------------------------------


"""
������ ����������� �������
�������
��� ������ �����. �������� �������� ����������� �������� � ������, � ����� ������ ����� �������� � ������. 
���� ���������� ��������� ���������, �������� ������ ������� �� ���.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    max_elem=elem[0]

    data=[max_elem]

    data.append(0)

    for i in range(1,len(elem)):

        if int(max_elem)<int(elem[i]):

            max_elem=elem[i]

            data=[max_elem]

            data.append(i)

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))

#-----------------------------------------------------------


#task7------------------------------------------------------


"""
������ ��������
�������
���� ������� � ������ �����. �� ����� ����������� ��� ������������ ���������� ��� ����� � �����. �������� ��� ��� �������.
��������� �������� �� ���� �������������� ������������������ ����������� �����, ���������� ���� ������� �������� � �����. ����� ����� �������� ����� X � ���� ����. ��� ����� �� ������� ������ ����������� � �� ��������� 200.

�������� �����, ��� ������� ���� ������ ������ � �����. ���� � ����� ���� ���� � ���������� ������, ����� ��, ��� � ����, �� �� ������ ������ ����� ���.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    height=int(input())

    position=0

    while position<len(elem) and int(elem[position])>=height:

        position+=1

    return position

def print_data(output_data):

    print (output_data+1)

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task8------------------------------------------------------


"""
������ ����������� ��������� ���������
�������
��� ������, ������������� �� ���������� ��������� � ���.
����������, ������� � ��� ��������� ���������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    count=0

    for i in range (0,len(elem)-1):

        if int(elem[i])!=int(elem[i+1]):

            count+=1

    return(count)

def print_data(output_data):

    print (output_data+1)

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task9------------------------------------------------------


"""
������ ������������ ��������
�������
����������� �������� �������� ������ (A[0] c A[1], A[2] c A[3] � �. �.).
���� ��������� �������� �����, �� ��������� ������� �������� �� ����� �����.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    for i in range(0,len(elem)//2):

        elem[i*2],elem[i*2+1]=elem[i*2+1],elem[i*2]

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task10------------------------------------------------------


"""
������ ������������ min � max�
�������
� ������ ��� �������� ��������. ��������� ������� ����������� � ������������ ������� ����� ������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    max_elem=elem[0]

    min_elem=elem[0]

    index_max=0

    index_min=0

    for i in range(0,len(elem)):

        if int(min_elem)>int(elem[i]):

            min_elem=elem[i]

            index_min=i

        if int(max_elem)<int(elem[i]):

            max_elem=elem[i]

            index_max=i

    elem[index_min],elem[index_max]=elem[index_max],elem[index_min]

    return elem

def print_data(output_data):

    for i in output_data:

        print (i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task11------------------------------------------------------


"""
������ �������� �������
�������
��� ������ �� ����� � ������ �������� � ������ k. ������� �� ������ ������� � �������� k, ������� ����� ��� ��������, ������� ������ �������� � �������� k.
��������� �������� �� ���� ������, ����� ����� k. ��������� �������� ��� ��������, � ����� ����� ������� ��������� ������� ������ ��� ������ ������ pop() ��� ����������.

��������� ������ ������������ ����� ��������������� � ������, � �� ������ ��� ��� ������ ���������. ����� ������ ������������ �������������� ������. ����� �� ������� ������������ ����� pop(k) � ����������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    k=int(input())

    for i in range(k,len(elem)-1):

        elem[i]=elem[i+1]

    elem.pop()

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task12------------------------------------------------------


"""
������ ��������� �������
�������
��� ������ ����� �����, ����� k � �������� C. ���������� �������� � ������ �� ������� � �������� k �������, ������ C, ������� ��� ��������, ������� ������ �� ����� k, ������.
��������� ��� ���� ���������� ��������� � ������ �������������, ����� ���������� ������ � ��� ����� ����� ����� �������� ����� �������, ��������� ����� append.

������� ���������� ������������ ��� � ��������� ������, �� ����� ����� ��� ������ � �� �������� ��������������� ������.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=input().split()

    elem.append(data[1])

    for i in range(len(elem)-1,int(data[0]),-1):

        elem[i]=elem[i-1]

    elem[int(data[0])]=int(data[1])

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))

#-----------------------------------------------------------


#task13------------------------------------------------------


"""
������ ����������� ����������� ���
�������
��� ������ �����. ����������, ������� � ��� ��� ���������, ������ ���� �����.
���������, ��� ����� ��� ��������, ������ ���� ����� �������� ���� ����, ������� ���������� ���������.
"""
#
def input_data(): 
    data = input().split() 
    return data 
def operation_data(elem): 
    count=0 
    for i in elem: 
        for j in elem: 
            if i==j: 
                count+=1 
        count-=1 
    return(count // 2) 
def print_data(output_data): 
    print(output_data) 
print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task14------------------------------------------------------


"""
������ ����������� ���������
�������
��� ������. �������� �� ��� ��������, ������� ����������� � ������ ������ ���� ���. �������� ����� �������� � ��� �������, � ������� ��� ����������� � ������.
"""
#

#-----------------------------------------------------------


#task15------------------------------------------------------


"""
������ ����������
�������
N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. ����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � �������� �� li �� ri ������������. ����������, ����� ����� �������� ������ �� �����.
��������� �������� �� ���� ���������� ������ N � ���������� ������� K. ����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N.

��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ ���� �I�, ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����.
"""
#

#-----------------------------------------------------------


#task16------------------------------------------------------


"""
������ ������
�������
��������, ��� �� ����� 8?8 ����� ���������� 8 ������ ���, ����� ��� �� ���� ���� �����. ��� ���� ����������� 8 ������ �� �����, ����������, ���� �� ����� ��� ���� ������ ���� �����.
��������� �������� �� ���� ������ ��� �����, ������ ����� �� 1 �� 8 � ���������� 8 ������. ���� ����� �� ���� ���� �����, �������� ����� NO, ����� �������� YES.
"""
#

#-----------------------------------------------------------



