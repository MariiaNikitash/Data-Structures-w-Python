def student_directory(student_names):
    dic = {}
    for i, name in enumerate(student_names):
        dic[i] = name
    return dic
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
#Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}
#print(student_directory(student_names))

def get_description(info, keys):
    for key in keys:
        if key in info:
	        print(info[key])
        else:
            print("None")
         
    
   
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
#print(get_description(info, keys))



