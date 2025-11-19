# Why Python is called OOPS

my_id_int = 1001
my_name_str = "Nitesh"
my_dict = {my_name_str:"Nitesh",my_id_int:"1001"}
my_list = [1,2,3,"test",1]

print("my_id_int ", type(my_id_int))        # -> my_id_int  <class 'int'>
print("my_name_str ", type(my_name_str))    # -> my_name_str  <class 'str'>
print("my_dict ",type(my_dict))             # -> my_dict  <class 'dict'>
print("my_list ", type(my_list))            # -> my_list  <class 'list'>

print(my_id_int.bit_count)                  # -> <built-in method bit_count of int object at 0x00000256777C9E10>
print(my_name_str.upper())                  # -> NITESH
print(my_dict.items())                      # -> dict_items([('Nitesh', 'Nitesh'), (1001, '1001')])
print(my_list.count(1))                     # -> 2