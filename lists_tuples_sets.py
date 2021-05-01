#List
The list is a collection that is ordered and changeable. Allows duplicate members.
In Python list is written with the Square bracket.
In List support both string and number.
Add and remove the elements is possible.

#List Methods
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	      Adds an element at the end of the list
                List = ['Mathematics', 'chemistry', 1997, 2000]
                List.append(20544)
                print(List)
                Output: ['Mathematics', 'chemistry', 1997, 2000, 20544]

clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	      Add the elements of a list (or any iterable), to the end of the current list
                List1 = [1, 2, 3] 
                List2 = [2, 3, 4, 5]
                List1.extend(List2)        
                print(List1)
                Output: [1, 2, 3, 2, 3, 4, 5]
                        [2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]
  
 
index()	        Returns the index of the first element with the specified value
insert()	      Adds an element at the specified position
                List = ['Mathematics', 'chemistry', 1997, 2000]
                List.insert(2,10087)     
                print(List)        
                Output: ['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]

pop()	          Removes the element at the specified position ,by default takes out last element
                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                print(List.pop())
                Output: 2.5
        
del() :         Element to be deleted is mentioned using list name and index.     
                List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
                del List[0]
                print(List)
                Output: [4.445, 3, 5.33, 1.054, 2.5]

remove()	      Removes the item with the specified value
reverse()      	Reverses the order of the list
sort()	        Sorts the list
