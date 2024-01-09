import click
from os import system
from subprocess import check_output as check_command_output
from re import findall
import Constants
from imgdox.CommandParser import print_list,print_strings
            
            
def find_in_out(out: str,word: str) -> list:
    uls = findall(FIND_WORD_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
    
    
def find_url(out: str) -> list:
    return findall(FIND_URL_REGEX_VALUE, str(out))
            
   
def find_emails(out: str) -> list:
    results = findall(FIND_EMAIL_REGEX_VALUE, out.decode(), re.MULTILINE)
    
    for i in range(len(results)):
        results[i] = "".join(results[i])
        
    return results


def find_base64(out: str) -> list:
    uls = findall(FIND_BASE64_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
            

def runCmd(cmdName: str, fileName: str) -> bytes:
    return check_command_output(cmdName+ " " + str(fileName), shell=True)


@click.command()
@click.option("--s", default="",required=False, help="List of words to look for. ( Seperated by a comma )")
@click.option("--f", default="", required=True, help="File name.")
# @click.option("--o", default="", required=False, help="Output file.")
def basic_scan(s, f):
    
    words = s.split(",")
    
    
    # Command Running
    outStrings = check_command_output("strings -n7 " + str(f), shell=True)
    outExiftool = check_command_output("exiftool " + str(f),shell=True)
    

    exiftool = []
    strings = []
    
    
    urls = find_url(outStrings) + find_url(outExiftool)
    emails = find_emails(outStrings) + find_emails(outExiftool)
    base64s = find_base64(outStrings) + find_base64(outExiftool)

    for i in range(len(urls)):
        urls[i]=urls[i].replace("'","").replace("\\n","")
    
    if s:
        for i in range(len(words)):
            strings.append(find_in_out(str(outStrings),words[i]))
            exiftool.append(find_in_out(str(outExiftool),words[i]))
        
    
    print_strings(s,"Strings")
    print_list(urls,"URLs")
    print_list(base64s,"Base64 Literals")
    print_list(emails,"Emails")