# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 23:12
# @Author  : toby
# @File    : 24.字符串常见操作.py
# @Software: PyCharm
# @Desc:

# 1.find
my_str = "hello world"
str_find = my_str.find("wo")
print(f"find:{str_find}")

# 2.index
str_index = my_str.index("wo")
print(f"index:{str_index}")

# 3.count
str_count = my_str.count("wo")
print(f"count:{str_count}")

# 4.replace
str_replace = my_str.replace("e", "E")
print(f"replace:{str_replace}")

# 5.split
str_split = my_str.split(" ")
print(f"split:{str_split}")

# 6.capitalize
str_capitalize = my_str.capitalize()
print(f"capitalize:{str_capitalize}")

# 7.title
str_title = my_str.title()
print(f"title:{str_title}")

# 8.startswith
str_startswith = my_str.startswith("h")
print(f"startswith:{str_startswith}")

# 9.endswith
str_endswith = my_str.endswith("d")
print(f"endswith:{str_endswith}")

# 10.lower
my_str = "Hello World"
str_lower = my_str.lower()
print(f"lower:{str_lower}")

# 11.upper
my_str = "hello world"
str_upper = my_str.upper()
print(f"upper:{str_upper}")

# 12.ljust
my_str = "hello"
str_ljust = my_str.ljust(10)
print(f"ljust:{str_ljust}")

# 13.rjust
str_rjust = my_str.rjust(10)
print(f"rjust:{str_rjust}")

# 14.center
str_center = my_str.center(10)
print(f"center:{str_center}")

# 15.lstrip
my_str = "     hello     "
str_lstrip = my_str.lstrip()
print(f"lstrip:{str_lstrip}")

# 16.rstrip
str_rstrip = my_str.rstrip()
print(f"rstrip:{str_rstrip}")

# 17.strip
str_strip = my_str.strip()
print(f"strip:{str_strip}")

# 18.rfind
my_str = "hello world"
str_rfind = my_str.rfind("o")
print(f"rfind:{str_rfind}")

# 19.rindex
str_rindex = my_str.rindex("o")
print(f"rindex:{str_rindex}")

# 20.partition
str_partition = my_str.partition("o")
print(f"partition:{str_partition}")

# 21.rpartition
str_rpartition = my_str.rpartition("o")
print(f"rpartition:{str_rpartition}")

# 22.splitlines
my_str = "hello\nworld"
str_splitlines = my_str.splitlines()
print(f"splitlines:{str_splitlines}")

# 23.isalpha
my_str = "helloworld"
str_isalpha = my_str.isalpha()
print(f"isalpha:{str_isalpha}")

# 24.isdigit
str_isdigit = my_str.isdigit()
print(f"isdigit:{str_isdigit}")

# 25.isalnum
my_str = "hello1111world"
str_isalnum = my_str.isalnum()
print(f"isalnum:{str_isalnum}")

# 26.isspace
my_str = "     "
str_isspace = my_str.isspace()
print(f"isspace:{str_isspace}")

# 27.join
link_str = "+"
str_list = ["hello", "world"]
str_join = link_str.join(str_list)
print(f"join:{str_join}")
