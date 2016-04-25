'''
Created on 25 Apr 2016

@author: Rolf
'''

class HelloWorldClass(object):
    
    @staticmethod
    def helloWorld():
        message = "Hello World!"
        #print message
        return message

if __name__ == '__main__':
    HelloWorldClass.helloWorld()
    
