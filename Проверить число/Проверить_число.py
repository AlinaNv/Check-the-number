#coding=windows-1251
print("������� �����")
a=float(input())
if (a<0) and (a%2==0):
    print("������������� ������ �����")
elif (a<0) and (a%2!=0):
    print("������������� �������� �����")
elif (a>0) and (a%2!=0):
    print("������������� �������� �����")
elif (a>0) and (a%2==0):
    print("������������� ������ �����")
else:
    print("����")