'''
Created on 2016 apr. 20

@author: mng
'''

if __name__ == '__main__':
    try:
        1/0
    except Exception as e:
        print e == ZeroDivisionError()
        print e is ZeroDivisionError()
        print type(e) == type(ZeroDivisionError())
        #print e(e, ZeroDivisionError)
        print e
        print type(e)
        print str(type(e))
    pass
