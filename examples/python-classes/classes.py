#!/usr/bin/python3

class Data:
    def __init__(self):
        print("Data> new class")
        self._data=[]
        self._count=0

    def add(self,item):
        self._data.append(item)
        self._count+=1

    def pop(self):
        result=self._data[-1]
        self._data=self._data[0:-1]
        self._count-=1
        return result

    def __repr__(self):
        return "<Data(%d): %s>" % (self._count,self._data)

    def dump(self):
        assert self._count==len(self._data)
        for i in self._data:
            print("Data.dump>",i)


if __name__=="__main__":
    data1=Data()
    print("classes.py")
    print(data1)
    data1.add("One")
    data1.dump()
    data1.add("Two")
    result=data1.pop()
    assert result=="Two"
    data1.dump()

    d=[]
    for i in ["A","B","C"]:
        o=Data()
        o.add(i)
        d.append(o)
    
    print(d)

