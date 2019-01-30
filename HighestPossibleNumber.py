#python 3.7.1

def highest_possible_num1(lst):
    lst  = [int(num) for num in str(lst)]
    new_lst = []
    for num in range(len(lst), 0, -1):
       new_lst.append(max(lst))
       lst.remove(max(lst))
    new_str = "".join(str(num) for num in new_lst)
    return new_str
    
def highest_possible_num2(lst):
    lst  = [int(num) for num in str(lst)]
    lst.sort()
    new_lst = []
    for num in range(len(lst), 0, -1):
       new_lst.append(lst[num-1])
    new_str = "".join(str(num) for num in new_lst)
    return new_str
    
            

print(highest_possible_num1(14592))
print(highest_possible_num2(14592))

list1 = ['1', '2', '3'] 
str1 = ''.join(list1)
print(str1)
