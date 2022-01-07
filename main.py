import requests
import time
import threading
# python3 main.py http://192.168.181.141/

s1= time.time()
url = "http://192.168.181.141/"

# This function will write reachable URLs after inject with payloads
def write(word):
    f1 = open("write1.txt", "a")
    # Write it to write1.txt file
    f1.write(word + "\n")

# This function will scan URLs and inject it with payloads
def scan(url,file):
    try:
        payload = open(file, "r+")

        # fixing the newline in payload
        lines = payload.readlines()
        fix = []
        for i in lines:
            i = i.replace("\n", "")
            fix.append(i)
        # for every payload inject URL
        for i in fix:
            surl = url + i
            # send GET request with new URL
            response = requests.get(surl)
            # check respond status code
            if (response.status_code ==  200):
                #if it on the list then print and save to file
                print(f"[+] found :- {surl}")
                write("[+] found :- "+ surl)
            else:
                pass
    except : # catch any connection error or failed request
        pass

# divide payload into files to minimize running time
files = ["fuzzingpayload1.txt", "fuzzingpayload2.txt","fuzzingpayload3.txt","fuzzingpayload4.txt","fuzzingpayload5.txt"]

myTh = []
# divide work to 5 thread to speed up the excution time
for i in range (5) :
    th= threading.Thread(name=f"Thread {i}" , target=scan , args=(url,files[i]))
    th.start()
    myTh.append(th)

# Use join to print Total time after executing all threads
for i in myTh :
    if i.is_alive():
        i.join()
    else : pass


# measure total time
s2 = time.time()
print(" Total Time ", int(s2 - s1), "seconds")