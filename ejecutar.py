#then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end + back_end
insert_index = full.index('Redux') + 1
full[insert_index:insert_index] = ['Python', 'SQL']
print(full)