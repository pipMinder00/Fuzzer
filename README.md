# Fuzzer
Fuzzing directories is a tool for exposing hidden paths by sending a request to a target URL using a payload wordlist line by line. The request will be made to see if this page exists depending on the status code of the response

# Steps to Scan Vulnerabilities: 
- Identify the Metasploitable IP address 
- Use the Metasploitable IP address as the target URL to fuzz it •
- Creating five threads to reduce running time 
- Scan the URL 
- Inject the URLs with payload wordlist line by line 
- Send GET request with the injected URLs 
- Check responds status code if it is = 200 
- Print the URLs that matched status code 200 
- Save the reachable URL after injected with payloads into a text file

## using Multithreads (5 thread) 
![image](https://user-images.githubusercontent.com/56893695/148609149-6f6ef922-4f5e-414f-b530-d5a09e929559.png)

## using Single thread
![image](https://user-images.githubusercontent.com/56893695/148609155-f949a3df-9ebc-437d-9245-b22f482ce3bc.png)
