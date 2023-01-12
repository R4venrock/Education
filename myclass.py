class MyClass():
   def f(self):
       return 155
mc2=MyClass()
print("It's for test too", mc2.f())

if __name__ == "__main__":
   mc=MyClass()
   print("It's only for test", mc.f())

from myclass import MyClass
if __name__ == "__main__":
   m=MyClass()
   print("It's really working:",m.f())