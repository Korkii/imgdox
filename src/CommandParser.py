from click import secho


def print_strings(listToParse: list,name: str):
    if listToParse:
        secho(f"{name} Found:", fg = "green")
        for sublist in listToParse:
            for occurrence in sublist:
                secho(occurrence, fg = "magenta")
    else:
        secho("\nSearched literals were not found.", fg="red")
    
def print_list(listToParse: list,name: str):
    if listToParse:
        secho(f"{name} Found:", fg = "green")
        for occurrence in listToParse:
             secho(occurrence, fg = "magenta")
    else:
        secho(f"\n{name} were not found.", fg="red")
    