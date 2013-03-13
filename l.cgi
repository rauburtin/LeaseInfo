#!/usr/bin/python3
# default for apache2 is /usr/lib/cgi-bin

def parse(fileName):

    f = open( fileName, "r" )
    output = {}
    thisIp = ""
    thisMAC = ""
    thisName = ""
    
    for line in f:
        
        # ip
        if (line.find("lease") == 0):
            if (thisIp != ""):
                output[thisIp] = "<tr><td>" + thisIp + "</td><td>" + thisMAC + "</td><td>" + thisName + "</td></tr>"
                thisMAC = ""
                thisName = ""
                
            thisIp = line[line.find(" ") +1 : line.find("{") -1]

        # mac
        if(line.find("hardware ethernet") > -1):
            thisMAC = line[line.find("ethernet") +9 : line.find(";")]
        
        # uid - will be replaced with name if it exists
        if(line.find("uid") > -1):
            thisName = line[line.find("uid") +5 : line.find(";") -1]
            
        # hostname
        if(line.find("client-hostname") > -1):
            thisName = line[line.find("hostname") +10 : line.find(";") -1]
            
    #final line
    if (thisIp != ""):
        output[thisIp] = "<tr><td>" + thisIp + "</td><td>" + thisMAC + "</td><td>" + thisName + "</td></tr>"

    #print output
    for k, v in sorted(output.items()):
        print(v + "<br>")

    # Close the file
    f.close()
    
#parse("/home/james/Source/LeaseInfo/dhcpd.leases")
print("Content-type: text/html\n\n")
print("<table valign='top' width='100%'>")
parse("/var/lib/dhcp/dhcpd.leases")
print("</table>")
