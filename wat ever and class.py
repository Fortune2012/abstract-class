#import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):

    #function to print a value
    def print(self,x):
        print("passed value : ",x)

    #Abstract method
    @abstractmethod
    def task(self):
        print('we are inside Abclass')

#create sub class
class test_class(Absclass):
    def task(self):
        print('we are inside test class task')


#object of the test class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)