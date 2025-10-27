def find_duplicates(arr):  
    # 3 5 2 5 6 8 9 1 3 3 
    elements = {}  
    # 3,5,2,5,6,8,9,1,3,3,
    duplicates = []  
      
    # 35 25 68 9 13 3 
    for index, value in enumerate(arr):  
        if value in elements:  
            # 3,5,2,5,6,8,9,1,3,3,
            duplicates.append((value, elements[value], index))  
        else:  
            # 3 5 2 5 6 8 9 1 3 3 
            elements[value] = index  
