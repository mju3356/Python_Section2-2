import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


class Self_Test:
    def function1():
        print('function1 called')
    def function2(self):
        print(id(self))
        print('function2 called')


f=Self_Test()

print(Self_Test.function1())
