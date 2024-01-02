import click
from os import system
import subprocess
import re

import Constants
from imgdox.CommandParser import print_list,print_strings
            
            
def find_in_out(out: str,word: str) -> list:
    uls = re.findall(FIND_WORD_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
    
    
def find_url(out: str) -> list:
    return re.findall(FIND_URL_REGEX_VALUE, str(out))
            
   
def find_emails(out: str) -> list:
    results = re.findall(FIND_EMAIL_REGEX_VALUE, out.decode(), re.MULTILINE)
    
    for i in range(len(results)):
        results[i] = "".join(results[i])
        
    return results
def find_base64(out: str) -> list:
    uls = re.findall(FIND_BASE64_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
            
def runCmd(cmdName: str, fileName: str) -> bytes:
    return subprocess.check_output(cmdName+ " " + str(fileName), shell=True)

@click.command()
@click.option("--s", default="",required=False, help="List of words to look for. ( Seperated by a comma )")
@click.option("--f", default="", required=True, help="File name.")
def basic_scan(s, f):
    
    words = s.split(",")
    
    
    # Command Running
    outStrings = subprocess.check_output("strings -n7 " + str(f), shell=True)
    outExiftool = subprocess.check_output("exiftool " + str(f),shell=True)
    
    cat= []
    exiftool = []
    strings = []
    
    
    urls = find_url(outStrings) + find_url(outExiftool)
    emails = find_emails(outStrings) + find_emails(outExiftool)


    for i in range(len(urls)):
        urls[i]=urls[i].replace("'","").replace("\\n","")
    
    if s:
        for i in range(len(words)):
            strings.append(find_in_out(str(outStrings),words[i]))
            exiftool.append(find_in_out(str(outExiftool),words[i]))
        


    # Print found urls.
    print_list(urls,"URLs")
    # If any strings were looked for, print them.
    print_strings(s,"Strings")


    click.secho("\nBase 64 found:",fg="green")


    print_list(emails,"Emails")