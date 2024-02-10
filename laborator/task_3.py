
#--------task3---------------
import colorama
import sys
import pathlib

def Explore(user_path,tab=0,mask='*'):
    path = pathlib.Path(user_path)
    if path.exists:
        files=path.glob(mask)# patern '**/*' - знаходить усі файли і папки навіть вкладені
        for f in files:
            if f.is_dir():
                print(colorama.Fore.RED+colorama.Style.BRIGHT+(' '*tab)+'<'+f.name.upper()+'>')
                Explore(user_path=f,tab=tab+3)
            else:
                print(colorama.Fore.BLUE+colorama.Style.BRIGHT+(' '*tab)+'|- '+f.name)
  
def main():
    colorama.init(autoreset=True)
    argv=sys.argv
    user_path = (argv[1] if len(argv)>=2 else '') # argv[0] - ім'я самого файлу програми; ''-робочий каталог (каталог з якого запускається програма)
    #user_path=r'D:\films'
    Explore(user_path)

if __name__=="__main__": 
    main()