#This will automatically install all modules required


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
## IN LINUX IT WILL ONLY USE PYTHON3 IF YOU HAVE A DEPRICATED VERSION OF PYTHON YOU NEED TO CHANGE THE COMMAND IN CODE
def installlinux():
    import os
    import subprocess
    modules=['requests', 'pandas', 'ipywidgets']
    for module in modules:
        try:
            print(f"Installing: {color.YELLOW + module + color.END}")
            subprocess.check_output(f"sudo python3 -m pip install {module}", stderr=subprocess.STDOUT, shell=True)
        except:
            print(color.YELLOW + f"Please make sure you have the most recent version of python or these modules are correct {modules}" + color.END)
            print(color.YELLOW + "If not you can download it here: https://www.python.org/downloads/ " + color.END)
            print(color.RED+ "##################################################################" + color.END)
            exit(color.RED + f"This module failed: {module}" + color.END) 
    return()


def installwindows():
    import os
    import subprocess
    modules=['requests', 'pandas', 'ipywidgets']
    for module in modules:
        try:
            print(f"Installing: {color.YELLOW + module + color.END}")
            subprocess.check_output(f"pip install {module}", stderr=subprocess.STDOUT, shell=True)
        except:
            print(color.YELLOW + f"Please make sure you have the most recent version of python or these modules are correct {modules}" + color.END)
            print(color.YELLOW + "If not you can download it here: https://www.python.org/downloads/ " + color.END)
            print(color.RED+ "##################################################################" + color.END)
            exit(color.RED + f"This module failed: {module}" + color.END) 
    return()


def main():
    import platform
    import os
    import subprocess
    pythonver = output = subprocess.check_output("python -V", shell=True)
    pythonver = pythonver.decode("utf-8")
    system_report = platform.system()
    if system_report == "Linux" or system_report == "linux":
        os.system('sudo python3 -m pip install regex')
        import regex
        os.system('sudo python3 -m pip install regex')
        if regex.match(r'Python 3\.([8-9]|([1-9][0-9])?)\.([2-9]|([1-9][0-9])?)', pythonver):
            installlinux()
    else:
        os.system('pip install regex')
        import regex
        if regex.match(r'Python 3\.([8-9]|([1-9][0-9])?)\.([2-9]|([1-9][0-9])?)', pythonver):
            installwindows()
        else:
            print("You have an outdated version of python please consider updating to 3.8 or later")
        
    
    
    import urllib.parse
    import requests
    import pandas
    main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
      
    key = input("Please Enter your API Key: ") #YOUR API KEY WILL BE LISTED IN THE Google Cloud: https://console.cloud.google.com/apis/credentials
   
    address = input("Please enter the Address: ")
    url = main_api + urllib.parse.urlencode({'address': address, 'key' : key})
    print(url)
    json_data = requests.get(url).json()

    json_status = json_data['status']
    #Checking API
    if json_status == 'OK':
        formatted_address= json_data['results'][0]['formatted_address']

        #Grabbing lat lng coords from json file
        lat = json_data['results'][0]['geometry']['location']['lat']
        lng = json_data['results'][0]['geometry']['location']['lng']

        print(color.BOLD + formatted_address + color.END)
        print(color.RED + f"{lat}" + color.END, color.YELLOW + f"{lng}" + color.END)

main()
