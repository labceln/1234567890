import urllib.request

stream_url = 'http://74.91.125.137:8000/stream/2/'
request = urllib.request.Request(stream_url)
try:
    request.add_header('Icy-MetaData', 1)
    response = urllib.request.urlopen(request)
    icy_metaint_header = int(response.headers.get('icy-metaint'))
    if icy_metaint_header is not None:
        metaint = icy_metaint_header
        read_buffer = metaint+1
        content = response.read(read_buffer)
        metaLen=content[metaint]*16
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
