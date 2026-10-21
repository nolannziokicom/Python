student_data={"id1":{'name': ['David'],
                  'class': ['V'],
                  'strengths': ["C/A","math","science"]},
                     
               "id2":
                 {'name': ['sara'],
                  'class': ['V'],
                  'strengths': ["kiswahili","math","science"]} ,

                   "id3":
                    {'name': ['David'],
                  'class': ['V'],
                  'strengths': ["C/A","math","science"]},
                  
                  "id4":
                  {"name": ["water"],
                   "class": ['Q'],
                   'strengths': ["nothing"]}

                  }
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)


