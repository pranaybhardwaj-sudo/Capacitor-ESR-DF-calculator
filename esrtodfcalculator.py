import math
pi=math.pi
def dftoesr():
    print("enter TANSIGMA")
    df=float(input())
    print("enter frequency in HERTZ")
    freq=float(input())
    print("enter capacitance in FARAD")
    cap=float(input())
    denom=2*pi*freq*cap
    esr=df/denom
    print("ESR IS {}".format(esr))

def esrtodf():
    print("enter ESR")
    esr2=float(input())
    print("enter frequency IN HERTZ")
    freq=float(input())
    print("enter capacitance IN FARAD")
    cap=float(input())
    num2=esr2*2*pi*freq*cap
    print("DF IS {}".format(num2))


while True:
    print("SELECT CHOICE:\n1. TANSIGMA TO ESR\n2.ESR TO DF")
    choice=input()
    if choice=='1':
        dftoesr()
    elif choice=='2':
        esrtodf()
