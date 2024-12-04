class MyClass:
    def __init__(self,x):
        self.x=x

    def __gt__(self, obj):
        return self.x > obj.x

    def __lt__(self, obj):
        return self.x < obj.x

    def __eq__(self, obj):
        return self.x == obj.x

s1=MyClass(5)
s2=MyClass(9)
print("Is "+str(s1.x)+" Greater then "+str(s2.x))
print(s1>s2)
print("Is "+str(s1.x)+" Less then "+str(s2.x))
print(s1<s2)
print("Is "+str(s1.x)+" Equals to "+str(s2.x))
print(s1==s2)