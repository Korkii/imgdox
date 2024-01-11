from subprocess import check_output as check_command_output
import re
def runCmd(cmdName: str, fileName: str) -> bytes:
    return check_command_output(cmdName+ " " + str(fileName), shell=True)

outStrings = check_command_output("cat " + "img.jpg", shell=True)
print(outStrings)


uls = re.findall(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$',str(outStrings))


print(uls)