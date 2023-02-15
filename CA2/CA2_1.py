
def template_part_finder(template_part,match_arr):
    for i in range(len(match_arr)):
        if(match_arr[i][0]==template_part):
            return match_arr[i][1]
    else:
        return "-1"
    

def is_patterned(main_str,template,match_arr,string_index,template_index):
    if(string_index==len(main_str) and template_index==len(template)):
        return True
    elif(string_index!=len(main_str) and template_index==len(template)):
        return False
    elif(string_index==len(main_str) and template_index!=len(template)):
        return False
    else :
        this_temp=template[template_index]
        if(template_part_finder(this_temp,match_arr)!="-1"):
            previous_part=template_part_finder(this_temp,match_arr)
            if(len(main_str[string_index:])<len(previous_part)):
                return False
            else:
                current_part=main_str[string_index:string_index+len(previous_part)]
                if(current_part!=previous_part):
                    return False
                else:
                    return is_patterned(main_str,template,match_arr,string_index+len(previous_part),template_index+1)
        else :
            for k in range(1,len(main_str)-string_index+1):
                match_arr.append([template[template_index],main_str[string_index:string_index+k]])
                if(is_patterned(main_str,template,match_arr,string_index+k,template_index+1)):
                    return True
                garbage=match_arr.pop()
            return False
                    



n=int(input())
templates=[]
strs=[]
for j in range(n):
    temp_str=input()
    temp_temp=input()
    strs.append(temp_str)
    templates.append(temp_temp)

match_arr=[]
for k in range(n):
    if(is_patterned(strs[k],templates[k],match_arr,0,0)):
        print("Yes")
    else:
        print("No")
    match_arr.clear()

