#Write a prog to calculate interest for principal amount as Rs10,000,
#at rate of  interest as 5% and number of years the amount is deposited as 7 years.

def calculate_Compund_Interest(p,n,r):
    print('StartBalance\t','\tInterest\t','Ending Balance')
    x = r/100
    tot = 0
    for i in range(1,n+1):
        z_new = p*(1+x)**i-p
        z_old = p*(1+x)**(i-1)-p
        tot = tot+(z_new-z_old)
        if (i==1):
            print('{0:.2f}\t'.format(p),end='')
            print('\t{0:.2f}\t'.format(z_new - z_old),end='')
            print('\t\t{0:.2f}\t'.format(z_new+p))
        else:
            print('{0:.2f}\t'.format(p),end='')
            print('\t{0:.2f}\t'.format(z_new - z_old),end='')
            print('\t\t{0:.2f}\t'.format(z_new+p))   
    print('Total Interest Deposited:Rs{0:.2f}'.format(tot))
p = int(input('Enter the Principal amount:'))
r = int(input('Enter the rate of interest:'))
n = int(input('Enter the Number of Year:'))
calculate_Compund_Interest(p,n,r)