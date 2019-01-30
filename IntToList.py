#python 3.7.1

def int_to_list(lst):

    new_lst = map(int,str(lst))
    print (list(new_lst))
    
    new_lst2 = [int(num) for num in str(lst)]
    print (new_lst2)
    
    new_lst3 =[]
    slst = str(lst)
    for num in slst:
       new_lst3.append(int(num))
    print (new_lst3)
    
    """
    q = lst
    new_lst4 = []
    while lst != 0:
          q, r = divmod(q, 10)
          new_lst4.append(r)
    print(new_lst4)
    """
      

int_to_list14592)
