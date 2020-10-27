from django.shortcuts import render
from django.http import HttpResponse
import os
import socket
import string
# Create your views here.

def call(request):
	return render(request,'jalebifafda.html')
# Create your views here.

def contact(request):
	return render(request, 'test.html', {})

def get_nmap(options, ip):
    print("NMAP (Network Mapper) is activated!! \n ")
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    data = str(process.read())
    return data

def get_whois(domain_name):
    command = "whois " + domain_name
    process = os.popen(command)
    data = str(process.read())
    # for lines in data:
    # 	print("\n",data[lines])
    return data

def get_domain_name(url):
    results = url
    str(results)
    # check whether http or https
    flag = results[:5]
    if flag == 'https':
        domain_name = get_https_domain(url)
    else:
        domain_name = get_http_domain(url)
    # return value to the main
    return domain_name

def get_https_domain(url):
    marker = url[12:]
    return marker
def get_http_domain(url):
    marker = url[11:]
    return marker


# # Create a directory
# def create_directory(directory):
#     # If directory not available, then create a new dir
#     if not os.path.exists(directory):
#         print("Creating a directory...\n")
#         os.makedirs(directory)
#     print("Directory is created \n")


# # Write data to text file
# def write_file(path, data):
#     print("Writing the data into files...\n")
#     f = open(path, 'w')
#     f.write(data)
#     f.close()


# # Create Reports
# def create_company_report(name, url, domain_name, ip_address, nmapp, whoiss):
#     project_dir = ROOT_DIRECTORY + '/' + name
#     # Call the create_dir
#     create_directory(project_dir)
#     # Call the write_file function
#     write_file(project_dir + "/url.txt", url)
#     write_file(project_dir + "/domain_name.txt", domain_name)
#     write_file(project_dir + "/ip_address.txt", ip_address)
#     write_file(project_dir + "/nmapp.txt", nmapp)
#     write_file(project_dir + "/whoiss.txt", whoiss)

# Gather all company data
def gather_company_info(name,url):
    domain_name = get_domain_name(url)
    #print("Name of folder is : ", name)
    #print("Domain name is : ", domain_name)
    ip_address = socket.gethostbyname(domain_name)
    #print("IP address: ", ip_address)

    whoiss = get_whois(domain_name)
    #print("Whois Information: \n", whoiss)
    nmapp = get_nmap(' ', ip_address)
    #print("Nmap Information: ", nmapp)

    # Call Create company reports
    #create_company_report(name, url, domain_name, ip_address, nmapp, whoiss)

# main function
#print("Begins here \n")

def scan(request):
	url=request.POST['url']
	# Main folder name.
	#ROOT_DIRECTORY = 'companies'
	#create_directory(ROOT_DIRECTORY)
	#url = input("Enter the url : ")
	domain_name = get_domain_name(url)
	ip_address = socket.gethostbyname(domain_name)
	whoiss = get_whois(domain_name)
	nmapp = get_nmap(' ', ip_address)
	name = domain_name[0:-4]
	#gather_company_info(name,url)

	return render(request,"result.html",
	{'result1':url , 'result2':domain_name , 'result3':name ,
	'result4':ip_address , 'result5':nmapp , 'result6':whoiss })