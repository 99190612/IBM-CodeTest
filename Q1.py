stock = int(input("The total number of T-shirts in shop:"))
size = input("All the size of T-shirt in shop:")
request = int(input("The number of T-shirt requested:"))
size_request = input("The size of T-shirt requested:")

def cntStock():
    size_list = size.split(" ")
    size_request_list = size_request.split(" ")
    for i in size_request_list:
        if(i in size_list):
            size_request_list.remove(i)
            size_list.remove(i)
        elif(size_list and size_request_list):
            for j in size_request_list:
                if(j > i): 
                    size_request_list.remove(i)
                    size_list.remove(j)
    return size_request_list
    

if(request > stock):
    print("No")
else:
    ans = cntStock()
    if(len(ans) == 0):
        print("Yes")
    else:
        print("No")

# 5
# XL XXXXXXXXXL XXS M XXS
# 4
# L M L XXS