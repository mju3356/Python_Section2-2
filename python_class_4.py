import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


class Name_Test:
    total=0

print(dir())
print('Before : ',Name_Test.__dict__)
Name_Test.total=1
print('After : ',Name_Test.__dict__)


n1=Name_Test()
n2=Name_Test()
print(id(n1),' vs ', id(n2))
print(dir())

print(n1.__dict__)
print(n2.__dict__)
n1.total=77
print(n1.__dict__)
print(n2.__dict__)


print(n1.total)
print(n2.total)
