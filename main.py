# This will automatically install all modules required
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
# IN LINUX IT WILL ONLY USE PYTHON3 IF YOU HAVE A DEPRICATED VERSION OF PYTHON YOU NEED TO CHANGE THE COMMAND IN CODE

def installlinux():
    import os
    import subprocess
    modules = ['pandas', 'urllib3', 'requests', 'ipywidgets', 'IPython']
    for module in modules:
        try:
            subprocess.check_output(
                f"sudo python3 -m pip install {module}", stderr=subprocess.STDOUT, shell=True)
            print(f"{color.YELLOW + module + color.END} *OK*")
        except:
            print(
                color.YELLOW + f"Please make sure you have the most recent version of python or these modules are correct {modules}" + color.END)
            print(
                color.YELLOW + "If not you can download it here: https://www.python.org/downloads/ " + color.END)
            print(
                color.RED + "##################################################################" + color.END)
            exit(color.RED + f"{module} *FAILED*" + color.END)
    pd_setup()

def installwindows():
    import os
    import subprocess
    modules = ['urllib3', 'requests', 'pandas', 'ipywidgets', 'IPython']
    for module in modules:
        try:
            subprocess.check_output(
                f"pip install {module}", stderr=subprocess.STDOUT, shell=True)
            print(f"{color.YELLOW + module + color.END}" +
                  color.GREEN + " *OK* " + color.END)
        except:
            print(
                color.YELLOW + f"Please make sure you have the most recent version of python or these modules are correct {modules}" + color.END)
            print(
                color.YELLOW + "If not you can download it here: https://www.python.org/downloads/ " + color.END)
            print(
                color.RED + "##################################################################" + color.END)
            exit(color.RED + f"{module} *FAILED*" + color.END)
    pd_setup()

def version_check():
    import platform
    import os
    import subprocess
    import sys
    system_report = platform.system()

    if system_report == 'Linux':
        pythonver = subprocess.check_output("python3 -V", shell=True)
        pythonver = pythonver.decode("utf-8")
    else:
        pythonver = subprocess.check_output("python -V", shell=True)
        pythonver = pythonver.decode("utf-8")

    if system_report == "Linux" or system_report == "linux":
        subprocess.run("sudo python3 -m pip install regex", capture_output=True)
        #os.system('sudo python3 -m pip install regex')
        import regex
        os.system('sudo python3 -m pip install regex')
        if regex.match(r'Python 3\.([8-9]|([1-9][0-9])?)\.([2-9]|([1-9][0-9])?)', pythonver):
            installlinux()
    else:
        os.system('python -m pip install regex')
        import regex
        if regex.match(r'Python 3\.([8-9]|([1-9][0-9])?)\.([2-9]|([1-9][0-9])?)', pythonver):
            installwindows()
        else:
            print(
                "You have an outdated version of python please consider updating to 3.8 or later")
    return print(f"{color.YELLOW}Version: {color.END}{color.PURPLE}{system_report} {pythonver}" + color.GREEN + "OK" + color.END)

def pd_setup():
    import pandas as pd
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    return print(color.YELLOW + "Pandas Setup: " + color.END + color.GREEN + "*OK*" + color.END)

def main():
    version_check()

    import urllib3
    import urllib.parse
    import requests
    import json
    from IPython.display import display
    import build_url
    http = urllib3.PoolManager()

    url = build_url.first_url.full_url()
    print(url)
    import pandas
    json_data = http.request('GET', f'{url}')
    df = json.loads(json_data.data.decode('utf-8'))

    json_status = df['status']
    # Checking API JSON Status
    if json_status == 'OK':
        df = pandas.json_normalize(df['results'])

        # I SPENT TWO HOURS TRYING TO FIGURE OUT HOW TO TURN A SERIES ITEM TO AN INT BECAUSE FOR SOME RESON IF YOU PRINT THIS
        lat = df['geometry.location.lat']
        # IT WILL COME BACK AS A SERIES AND STILL HOLD A FLOAT VALUE BUT MESS UP THE PRINT STATEMENT
        lng = df['geometry.location.lng']
        
        # THIS CONVERTS THE SERIES ITEMS INTO A FLOAT BECAUSE IT WAS BEING STUPID AND I DONT KNOW A BETTER WAY
        #'''
        lat = lat.tolist()
        lng = lng.tolist()
        for la in lat:
            lat = float(la)
        for ln in lng:
            lng = float(ln)
        ############################################################################################################
        #'''
        display(
            df[['formatted_address', 'geometry.location.lat', 'geometry.location.lng']])
    ###### WHAT IS ABOVE IS MUCH BETTER THAN THE GARBO I HAD TO DEAL WITH BELOW ############
    
    '''
    #Checking API
    if json_status == 'OK':
        formatted_address= json_data['results'][0]['formatted_address']
        #Grabbing lat lng coords from json file
        lat = json_data['results'][0]['geometry']['location']['lat']
        lng = json_data['results'][0]['geometry']['location']['lng']
        print(color.BOLD + formatted_address + color.END)
        print(color.RED + f"{lat}" + color.END, color.YELLOW + f"{lng}" + color.END)
    '''

main()
