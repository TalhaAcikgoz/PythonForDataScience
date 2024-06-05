ft_list = ["Hello", "tata!"]
ft_tuplee = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# your code here
ft_set_tmp = {"Hello", "Kocaeli!"}

ft_list[1] = "World!"

ft_tuple_list = list(ft_tuplee)
ft_tuple_list[1] = "Turkey!"
ft_tuple = tuple(ft_tuple_list)

ft_set.remove("tutu!")
ft_set.update(ft_set_tmp)

ft_dict["Hello"] = "42Kocaeli!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)