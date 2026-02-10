total_list=[21,22,23,24]
num=int(input("enter your rollno."))
if num in total_list :
    print("already registered")
else :
    total_list.append(num)
    print("registered")
    print(f"updated is : {total_list}")
    print(f"registeration completed for the roll numbeer {num}")
    
