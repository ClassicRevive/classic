#/usr/bin/env python 

from time import sleep

def auto_hail():
    
    n = 2
    i = 1
    while i < 25:

        while n != 1:
            if n == 1:
                break
            elif n % 2 == 0:
                n = n / 2
                print n
                sleep(0.1)
            elif n % 2 == 1:
                n = (3 * n) + 1
                print n
                sleep(0.1)
      
        i += 1
        n = i
        print "Done, starting on", i # "in"
        #print"3.."
        #sleep(0.01)
        #print"2.."
        #sleep(0.01)
        #print"1.."
        #sleep(0.01)


auto_hail()


