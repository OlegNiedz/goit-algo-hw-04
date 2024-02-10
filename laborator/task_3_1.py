
#--------task3---------------
import colorama
import sys
import pathlib

def Explore(user_path,tab=0):
    colorama.init(autoreset=True)
    path = pathlib.Path(user_path)
    if path.exists:
        lst=path.iterdir()
        for el in lst:
            if el.is_dir():
                print(colorama.Fore.GREEN+(tab*' ')+"\\"+el.name)
                Explore(user_path=el,tab=tab+1)
            else:
                print(colorama.Fore.LIGHTBLUE_EX+(tab*' ')+"|"+el.name)
 
def main():
    colorama.init(autoreset=True)
    argv=sys.argv
    user_path = (argv[1] if len(argv)>=2 else '') # argv[0] - ім'я самого файлу програми; ''-робочий каталог (каталог з якого запускається програма)
    
    Explore(user_path,tab=1)

if __name__=="__main__": 
    main()