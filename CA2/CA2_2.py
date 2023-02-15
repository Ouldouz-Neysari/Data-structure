
def priority_returner(c):
    if(c=="*" or c=="/"):
        return 2
    elif(c=="+" or c=="-"):
        return 3
    else:
        return 4
    
def process_string(main_str):
    S=[]
    
    for i in range(len(main_str)):
        if(main_str[i]=="/" or main_str[i]=="*" or main_str[i]=="+" or main_str[i]=="-"):
            while(True):
                if(len(S)==0 or S[-1]=="("):
                    S.append(main_str[i])
                    break
                else:
                    if(S[-1]=="/" or S[-1]=="*" or S[-1]=="+" or S[-1]=="-"):
                        if(priority_returner(main_str[i])< priority_returner(S[-1])):
                            S.append(main_str[i])
                            break
                        else:
                            print(S.pop(),end="")

        elif(main_str[i]=="("):
            S.append(main_str[i])
        elif(main_str[i]==")"):
            while(S[-1]!="("):
                print(S.pop(),end="")
            s=S.pop()
        else :
            print(main_str[i],end="")
    while(len(S)!=0):
        s=S.pop()
        if(s!="(" and s!=")"):
            print(s,end="")

main_str=input()
process_string(main_str)