class Myclass1():

    def __init__(self,cls_input_1):
        print("init of class1")
        self.prop_cls1 = 10
        self.cl1_in1 = cls_input_1
        print(self.cl1_in1)
    def method1_class_1(self):
        print("method_1_class1")

class Myclass2(Myclass1):

    def __init__(self,cl1in1,cl2in1):

        super().__init__(cl1in1)
        print("Init of class2")
        self.cl2in1 = cl2in1
    def method1_class_2(self):
        print("method1_class_2")


#obj1 = Myclass1()
#obj1.method1_class_1()

obj2 = Myclass2("xyz","abc")
obj2.method1_class_2()
obj2.method1_class_1()
print(obj2.cl1_in1)