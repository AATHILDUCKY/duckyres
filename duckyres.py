import requests
inputs= input()
input_arr=inputs.split()
textfile = input_arr[0]
output_file = input_arr[1]

file = open(textfile)

content = file.read()

subdomains= content.splitlines()
discovered_subdomains=[]
for subdomain in subdomains:
    url =f"http://{subdomain}"

    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] discovered subdomain:",url)
        discovered_subdomains.append(url)


with open(output_file, 'w') as f:
    for i in discovered_subdomains:
        res = requests.head(i)
        last =i + "  respone: "+ str(res.status_code)+"\n"
        f.write(last)