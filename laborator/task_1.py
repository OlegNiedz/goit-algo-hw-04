#--------task1---------------

import re

def total_salary(path):
    try:
        with open(path,"r") as f_txt:
            lines = f_txt.readlines()
            total=0
            for sal in lines:
                total+=int(re.findall(r"[\d\+]+", sal)[0])
            return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {total//lines.__len__()}"
    except Exception as e:
        return (f"ERROR: {e}")
    
print(total_salary(r"source\salary_file.txt"))
