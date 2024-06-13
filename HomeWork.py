def reg_to_bianary(num,num_Siviot):##פעולה שממירה את המספר לבינאירי
    str=''
    num_copy=num
    for j in range(num_Siviot-1,-1,-1):
        if(num>=pow(2,j)):
            str+='1'
            num-=pow(2,j)
        else:
            str+='0'
        print(str,num,j)
    mashlim_le_2(str)
        
def mashlim_le_2(str):##פעולה שמבצעת את שיטת המשלים לשתיים
    str1=""
    str2=""
    for i in range(len(str)):
        if(str[i]=='1'):
            str1+='0'
        else:
            str1+='1'
    print(str1)
    carry_on=1
    str3=""
    for j in range(len(str1)-1,0,-1):
        if(str1[j]=='0' and carry_on==1):       
            str3+="1"
            carry_on=0
        elif(str1[j]=='1' and carry_on==1):
            str3+="0"
        else:
            str3+=str1[j]

    print(reversed(str3))
   
        

            

reg_to_bianary(24,8)

