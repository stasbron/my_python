a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
action = eval('*'.join(a_tuple))
print ("The result of multiply is=: ", action)



a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
a_list = list(a_tuple)
a_list.reverse()
a_rev = int(''.join(a_list))
print ("The result of reversion of typed digit is: ",  a_rev)


a = input("enter 4-character digit: ")
a_tuple = tuple(str(a))
a_list = list(a_tuple)
a_sort = int(''.join(sorted(str(a))))
print ("the sorted digit that you have just typed is: ", a_sort)