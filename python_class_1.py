import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class User_Info:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def print_info(self):
        print("---------------")
        print('Name:' + self.name)
        print("Phone:"+self.phone)
        print('---------------')\

    def __del__(self):
        print('Delete')
        

User1=User_Info('Kim','010-1234-2896')
User2=User_Info('Park','010-4321-2896')

#print(id(User1))
#print(id(User2))


#User1.set_info('Kim','010-1234-2896')
#User2.set_info('Park','010-4321-2896')
User1.print_info()
User2.print_info()
