# coding:utf-8
"""
代理模式
模式特点：为其他对象提供一种代理以控制对这个对象的访问。
点评：挺不错，提供代理来访问接口
"""


class Interface :
    def Request(self):
        return "hello"


class RealSubject(Interface):
    def Request(self):
        print "Real request."



class Proxy(Interface):
    def Request(self):
        self.real = RealSubject()
        self.real.Request()


if __name__ == "__main__":
    p = Proxy()