#List
The list is a collection that is ordered and changeable. Allows duplicate members.
In Python list is written with the Square bracket.
In List support both string and number.
Add and remove the elements is possible.

#List Methods
Python has a set of built-in methods that you can use on lists.

Method	        Description

append()	Adds an element at the end of the list

                List = ['Mathematics', 'chemistry', 1997, 2000]
                List.append(20544)
                print(List)
                Output: ['Mathematics', 'chemistry', 1997, 2000, 20544]
          

clear()	        Removes all the elements from the list.

                list = ['1','2','3']  
                for l in list:  # Iterating list  
                print(l)  
                list.clear()  
                print("After clearing:")  
                for l in list:  # Iterating list  
                print(l)  
                Output:1
                      2
                      3
                After clearing:
                  
                  
max():          Calculates maximum of all the elements of List.

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                print(max(List))
                Output:5.33
          
          
len(list_name): Calculates total length of List.

                List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
                print(len(List))
                Output:10          
          
          
min() :         Calculates minimum of all the elements of List.

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                print(min(List))
                Output:1.054          

          
copy()	        Returns a copy of the list

                lis1 = [ 1, 2, 3, 4 ]
                lis2 = lis1.copy()
                print ("The new list created is : " + str(lis2))
                lis2.append(5)
                print ("The new list after adding new element : " + str(lis2))
                print ("The old list after adding new element to new list  : " + str(lis1))
                Output: The new list created is : [1, 2, 3, 4]
                        The new list after adding new element : [1, 2, 3, 4, 5]
                        The old list after adding new element to new list  : [1, 2, 3, 4]
                          
                          
count()	        Returns the number of elements with the specified value

                List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
                print(List.count(1))
                Output:4
        

extend()	Add the elements of a list (or any iterable), to the end of the current list

                List1 = [1, 2, 3] 
                List2 = [2, 3, 4, 5]
                List1.extend(List2)        
                print(List1)
                Output: [1, 2, 3, 2, 3, 4, 5]
                        [2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]
              
  
 
index()	        Returns the index of the first element with the specified value.

                List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
                print(List.index(2))
                Output:1
        
insert()        Adds an element at the specified position

                List = ['Mathematics', 'chemistry', 1997, 2000]
                List.insert(2,10087)     
                print(List)        
                Output: ['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]
          

pop()	        Removes the element at the specified position ,by default takes out last element

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                print(List.pop())
                Output: 2.5
        
        
del() :         Element to be deleted is mentioned using list name and index.     

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                del List[0]
                print(List)
                Output: [4.445, 3, 5.33, 1.054, 2.5]
            

remove()	Removes the item with the specified value.

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                List.remove(3)
                print(List)
                Output: [2.3, 4.445, 5.33, 1.054, 2.5]
          
          
reverse()      	Reverses the order of the list. Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter 
                and reverse_flag is set to False, if nothing is passed through sorted().

                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                #Reverse flag is set True
                List.sort(reverse=True) 
                #List.sort().reverse(), reverses the sorted list  
                print(List)        
                Output: [5.33, 4.445, 3, 2.5, 2.3, 1.054]
                
              
sort()	        Sorts the list in particular manner. 

                # vowels list
                vowels = ['e', 'a', 'u', 'o', 'i']
                # sort the vowels
                vowels.sort()
                # print vowels
                print('Sorted list:', vowels)
                Output: Sorted list: ['a', 'e', 'i', 'o', 'u']
                  

sum() :         Calculates sum of all the elements of List.

                List = [1, 2, 3, 4, 5]
                print(sum(List))
                Output:15
