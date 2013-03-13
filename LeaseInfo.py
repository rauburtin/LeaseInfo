#!/usr/bin/python3

def parse(fileName):

    f = open (fileName,"r")

    #Read whole file into data
    data = f.read()

    # Print it
    print(data)

    # Close the file
    f.close()
    
parse("/home/james/Source/LeaseInfo/dhcpd.leases")