import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class Warehouse:
    stcok_num=0
    def __init__(self,name):
        self.name=name
        Warehouse.stcok_num+=1

    def __del__(self):
        Warehouse.stcok_num-=1

User1=Warehouse('Kim')
User2=Warehouse('Park')

print(User1.name)
print(User2.name)

print(User1.__dict__)
print(User2.__dict__)

print(Warehouse.__dict__)

print(User1.stcok_num)
print(User2.stcok_num)
