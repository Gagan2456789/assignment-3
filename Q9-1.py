class Emp:
    def_init_(self,eid,ename,esal):
    self.eid=eid
    self.ename=ename
    self.esal=esal
    def_init_(self):







class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()

