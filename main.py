immutable_var = (1, 2.5, "a", True)
print("Immutable tuple:", immutable_var)
immutable_var[0] = 100 # Кортежи неизменяемы, поэтому возникнет ошибка
mutable_list = [1, 2.5, "a", True]
mutable_list[0] = 100
mutable_list.append("Modified")
print("Mutable list:", mutable_list)