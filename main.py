def profit(a1,a2):
   print('You have profit of ',a2-a1,'and Profit percentage of',((a2-a1)/a1)*100,'%') 
def loss(a1,a2):
    print('You have loss of ',a1-a2,'and Loss percentage of',((a1-a2)/a1)*100,'%')
def main():
    a1 = float(input('Please enter your cost price- '))
    a2 = float(input('Please enter your selling price- '))
    if (a2>a1):
        profit(a1,a2)
    elif (a2<a1):
        loss(a1,a2)
    else :
        print('You neither have loss or profit')
if __name__=='__main__' :
    main()


