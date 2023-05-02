import sys
class ipConversion:
    def __init__(self):
        octet1=0
        octet2=0
        octet3=0
        octet4=0
    def Binary(self,octet1,octet2,octet3,octet4):
        print("Binary:",end='   ')
        print(format(octet1,"08b")+"."+format(octet2,"08b")+"."+format(octet3,"08b")+"."+format(octet4,"08b"))
    def Decimal(self,octet1,octet2,octet3,octet4):
        print("Decimal:",end='  ')
        b='0b'+format(octet1,"08b")+format(octet2,"08b")+format(octet3,"08b")+format(octet4,"08b")
        print(int(b,2))
    def Hexa(self,octet1,octet2,octet3,octet4):
        print("Hexa:",end='     ')
        print(format(octet1,"02X")+"."+format(octet2,"02X")+"."+format(octet3,"02X")+"."+format(octet4,"02X"))
    def Octa(self,octet1,octet2,octet3,octet4):
        print("Octal:",end='    ')
        print(format(octet1,"04o")+"."+format(octet2,"04o")+"."+format(octet3,"04o")+"."+format(octet4,"04o"))
    def split(self,ip):
        octets=ip.split(".")
        self.octet1 = int(octets[0])
        self.octet2 = int(octets[1])
        self.octet3 = int(octets[2])
        self.octet4 = int(octets[3])   
    
    def main(self,ipArray):
        for ip in ipArray:
            print("Converting IP",ip,'\n')
            self.split(ip)
            self.Binary(self.octet1,self.octet2,self.octet3,self.octet4)
            self.Hexa(self.octet1,self.octet2,self.octet3,self.octet4)
            self.Octa(self.octet1,self.octet2,self.octet3,self.octet4)
            self.Decimal(self.octet1,self.octet2,self.octet3,self.octet4)    
            print("------------------------------------------------------------------------")


if __name__ == '__main__':
    obj=ipConversion()
    obj.main(sys.argv[1:])
