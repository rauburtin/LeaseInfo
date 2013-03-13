#!/usr/bin/python3

def parse(fileName):

    f = open( fileName, "r" )
    output = ""
    
    for line in f:
        
        # ip
        if (line.find("lease") > -1):
            if (output != ""):
                print(output)
                output = ""
            thisIp = line[line.find(" ") +1 : line.find("{") -1]
            output = thisIp
            
        # mac
        if(line.find("hardware ethernet") > -1):
            thisMAC = line[line.find("ethernet") +9 : line.find(";")]
            output += " " + thisMAC
            
        # hostname
        if(line.find("client-hostname") > -1):
            thisName = line[line.find("hostname") +10 : line.find(";") -1]
            output += " " + thisName 
            
    if(output != ""):
        print(output)

    # Close the file
    f.close()
    
#parse("/home/james/Source/LeaseInfo/dhcpd.leases")
parse("/var/lib/dhcpd/dhcpd.leases")