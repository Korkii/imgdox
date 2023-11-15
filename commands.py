import click
from os import system
import subprocess
import re
            
            
def find_in_out(out: str,word: str) -> list:
    uls = re.findall(re.escape(word)+r'(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(out))
    
    for i in range(len(uls)):
        uls[i]=uls[i].replace("'","").replace("\\n","")
        
    return uls
    
    
def find_url(out: str) -> list:
    return re.findall(r'http[s]?://(?:\w+|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(out))
            
   
def find_emails(out: str) -> list:
    results = re.findall(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$", out.decode(), re.MULTILINE)
    
    for i in range(len(results)):
        results[i] = "".join(results[i])
        
    return results
def find_base64(out: str) -> list:
    uls = re.findall(r'^(?:([a-z0-9A-Z+\/]){4})*(?1)(?:(?1)==|(?1){2}=|(?1){3})$', str(out))
    
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
    click.echo(emails)
    for i in range(len(urls)):
        urls[i]=urls[i].replace("'","").replace("\\n","")
    
    if s:
        for i in range(len(words)):
            strings.append(find_in_out(str(outStrings),words[i]))
            exiftool.append(find_in_out(str(outExiftool),words[i]))
        



    click.secho("\nUrls Found: " ,fg="green")
    
    for i in urls:
        click.secho(i,bg='blue', fg='white')
    
    if s:
        click.secho("Strings Found:", fg = "green")
        for i in strings:
            for j in i:
                click.secho(j, fg = "magenta")
    else:
        click.secho("\nNo strings were searched.", fg="red")

    click.secho("\nBase 64 found:",fg="green")
    
    click.secho("\nEmails found: ",fg="green")
    for i in emails:

        click.secho(i, fg = "magenta")