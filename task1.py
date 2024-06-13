Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list=[1,2,3,4,5,6]
>>> my_list.append(7)
>>> my_list.remove(5)
>>> my_list[0]
1
>>> print(my_list)
[1, 2, 3, 4, 6, 7]
>>> 
>>> 
>>> 
>>> my_dict={'name':'atul','age':'21','city':'goa'}
>>> my_dict['gender']='male'
>>> del my_dict['age']
>>> my_dict['city']='Banglore'
>>> print('update dictionary:',my_dict)
... 
update dictionary: {'name': 'atul', 'city': 'Banglore', 'gender': 'male'}
>>> 
>>> 
>>> my_set={1,2,3,4,5,6}
>>> my_set.add(7)
>>> my_set.remove(3)
>>> my_set.discard(2)
>>> my_set.add(10)
>>> print('update set:',my_set)
update set: {1, 4, 5, 6, 7, 10}
