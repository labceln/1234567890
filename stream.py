# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:54:38 2020

@author: TSG023
"""


import urllib.request

stream_url = 'http://37.251.146.169:8300/stream'
request = urllib.request.Request(stream_url)
try:
    request.add_header('Icy-MetaData', 1)
    response = urllib.request.urlopen(request)
    icy_metaint_header = int(response.headers.get('icy-metaint'))
    if icy_metaint_header is not None:
        metaint = icy_metaint_header
        content = response.read(metaint+1)
        metaLen=content[-1]*16
        if metaLen ==0:
            print ("no title")
        else :    
            content=response.read(metaLen)
            title = content.decode("utf-8").split("'")[1]
            print (title)
        
    count=512
    with open("data", "wb") as fout:
        receivedBytes=0
        while(True):            
            if (receivedBytes == metaint):
                i=response.read(1)
                metaLen = int.from_bytes(i,"little")*16
                if (metaLen > 0):
                    content=response.read(metaLen) 
                    title = content.decode("utf-8").split("'")[1]
                    print(title)
                    
                receivedBytes = 0                    
                    
            bytesLeft = count if ((metaint - receivedBytes) >count) else (metaint - receivedBytes)
            result = response.read(bytesLeft)
            receivedBytes += len(result)
            fout.write(result)
        
except :
    import traceback
    traceback.print_exc()
