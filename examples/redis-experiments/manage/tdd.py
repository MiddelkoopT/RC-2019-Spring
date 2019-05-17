#!/usr/bin/python3

class Tdd:

    def true(self,s1):
        if s1!=True:
            print('!!!',s1)
            assert s1==True

    def false(self,s1):
        if s1!=False:
            print('!!!',s1)
            assert s1==False

    def equals(self,s1,s2):
        if s1!=s2:
            print('!!!',s1,s2)
            assert s1==s2


def tdd_test_tdd(tdd):
    #tdd_true(False)
    tdd.true(True)
    #tdd_false(True)
    tdd.false(False)
    #tdd_equals(0,1)

    tdd.equals(1,1)
    tdd.equals("one","one")
    tdd.equals({"one":1,"two":2},{"two":2,"one":1})

if __name__=='__main__':
    tdd=Tdd()
    tdd_test_tdd(tdd)

