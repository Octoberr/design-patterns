# coding:utf-8
"""
大话设计模式
工厂模式
模式特点：工厂根据条件产生不同功能的类。
点评：应该就是类的继承，定义了一个公共父类，然后就使用继承来编写子类
"""

class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.op1+self.op2


class OperationSub(Operation):
    def GetResult(self):
        return self.op1-self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1*self.op2


class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1/self.op2
            return result
        except:
            print "error:divided by zero."
            return 0

class OperationUndef(Operation):
    def GetResult(self):
        print "Undefine operation."
        return 0

class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationSub()
    operation["*"] = OperationMul()
    operation["/"] = OperationDiv()
    def createOperation(self,ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == "__main__":
    op = raw_input("operator: ")
    opa = input("a: ")
    opb = input("b: ")
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.GetResult()