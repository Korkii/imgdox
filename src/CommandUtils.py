import click
from os import system,mkdir,path
from subprocess import check_output as check_command_output
import re
import Constants
from CommandParser import print_list,print_strings
from cv2 import split as img_split
from cv2 import imread,imwrite





def generate_bit_planes(fileName):
    """
    Generate bit planes images
    
    Keyword arguments:
    fileName -- the img file name
    """


    if not path.exists("output"):
        mkdir("output")
    else:
        pass
    image = imread(fileName) # Split the image into color planes
    b, g, r = img_split(image)
    #bPlanes,gPlanes,rPlanes = []
    for i in range(7):
        imwrite(f'output/b{i}.jpg',b & (1<<i))
        imwrite(f'output/g{i}.jpg',g & (1<<i))
        imwrite(f'output/r{i}.jpg',r & (1<<i))



           
def find_in_out(out: str,word: str) -> list:
    """
    Find specific words in a str.
    
    Keyword arguments:
    out -- the inputted text
    word -- the word to look for in the text
    """
    uls = re.findall(re.escape(word) + Constants.FIND_WORD_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
    
    
def find_url(out: str) -> list:
    """
    Find URLs within a str.
    
    Keyword arguments:
    out -- the inputted text
    """
    return re.findall(Constants.FIND_URL_REGEX_VALUE, str(out))
            
   
def find_emails(out: str) -> list:
    """
    Find emails within a str.
    
    Keyword arguments:
    out -- the inputted text
    """
    results = re.findall(Constants.FIND_EMAIL_REGEX_VALUE, out.decode(), re.MULTILINE)
    
    for i in range(len(results)):
        results[i] = "".join(results[i])
        
    return results


def find_base64(out: str) -> list:
        """
    
    Find Base64s within a str.
    
    Keyword arguments:
    out -- the inputted text
    """
    uls = re.findall(Constants.FIND_BASE64_REGEX_VALUE, str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
            

def runCmd(cmdName: str, fileName: str) -> bytes:
    return check_command_output(cmdName+ " " + str(fileName), shell=True)



@click.command()
@click.option("--f", default="", required=True,prompt='File name', help="File name.")
@click.option("--s", default="",required=False, help="List of words to look for. ( Seperated by a comma )")

def basic_scan(f,s):
    
    words = s.split(",")
    
    
    # Command Running
    outStrings = check_command_output("strings -n7 " + str(f), shell=True)
    outExiftool = check_command_output("exiftool " + str(f),shell=True)


    exiftool = []
    strings = []
    
    
    urls = find_url(outStrings) + find_url(outExiftool)
    emails = find_emails(outStrings) + find_emails(outExiftool)
    #base64s = find_base64(outStrings) + find_base64(outExiftool)

    for i in range(len(urls)):
        urls[i]=urls[i].replace("'","").replace("\\n","")
    
    if s:
        for i in range(len(words)):
            strings.append(find_in_out(str(outStrings),words[i]))
            exiftool.append(find_in_out(str(outExiftool),words[i]))
        
    
    print_strings(s,"Strings")
    print_list(urls,"URLs")
    print_list(emails,"Emails")


    generate_bit_planes(str(f))