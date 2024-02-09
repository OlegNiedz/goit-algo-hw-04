#--------task2---------------

list_cats=[]

def get_cats_info(path):
    try:
        with open(path,"r") as fcats:
            for cat in fcats.readlines():
                cat = cat.strip().split(sep=", ")
                list_cats.append({"id":cat[0], "name":cat[1], "age":cat[2]})
                
            return list_cats
    except Exception as e:
        return e
print(get_cats_info(r'C:\Users\Olegn\PYTHON_PROJECTS\Lesson_0\first_repo\cats.txt'))
