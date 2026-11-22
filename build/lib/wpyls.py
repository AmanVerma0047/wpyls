from pathlib import Path
import argparse
from rich import print
from rich.console import Console
from rich.table import Table


def main_cli():
    console = Console()
    table = Table(title="wpyls List")
    table.add_column("Name",style="bold")
    table.add_column("Size",style="bold")


    p = Path('.')
    ls = [".txt"]

    parser = argparse.ArgumentParser()
    parser.add_argument("--ex",help ="Display all the files containing the given extension!" )
    parser.add_argument("--search",help ="Display all the files with the given name!" )
    agp = parser.parse_args()

    extension = agp.ex
    search_query = agp.search

    print(search_query)
    if agp.ex != None:
        for x in p.glob(f"*{extension}"):
            files = Path(x)
            table.add_row(f"[magenta]{x}[/magenta]", f"[blue]{files.stat().st_size}[/blue]","bytes")
            # print(f"[magenta]{x} \t [blue]{files.stat().st_size}bytes")     
    elif agp.search !=None:
        found = False
        for x in p.iterdir():
            files = Path(x)
            if  search_query in str(x):
                table.add_row(f"[magenta]{x}", f"[blue]{files.stat().st_size}","bytes")
                found = True
        if not found:
            print("[red]File Not Found in the current directory![/red]")
    else:
        # for x in p.glob("**/"):
        #     files = Path(x)
        #     print(f"{x} \t {files.stat().st_size}bytes")
        for x in p.iterdir():
            files = Path(x)
            table.add_row(f"[magenta]{x}[/magenta]", f"[blue]{files.stat().st_size}[/blue]","bytes")
    

    console.print(table)

