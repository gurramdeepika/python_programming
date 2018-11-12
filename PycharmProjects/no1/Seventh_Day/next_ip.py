# next ip address
class IpAddress:

    def __init__(self,ip):
        self.ip =ip

    def validateIp(self):
        iparry = self.ip.split('.')
        if len(iparry) < 4:
            print(" please enter the valid ip address")
            ip = input("enter the ip address")
            self.validateIp()
        return iparry

    def nextip( self ):
        ip1=''
        iparry = self.validateIp()
        i =len(iparry)-1
        count = 0
        while(i >= 0):
            if iparry[i] == '255':
               i -=1
               count+=1
               if count == 3:
                   iparry[1]=iparry[2]=iparry[3]='0'
                   break
            else:
                ippa = int(iparry[i])
                ippa += 1
                iparry[ i ] = str(ippa)
                i-=1

        ip1 = '.'.join(iparry)
        return ip1

if __name__ == '__main__':
    ip = input("please enter the ip address")
    cip = IpAddress(ip)
    print(cip.nextip())





