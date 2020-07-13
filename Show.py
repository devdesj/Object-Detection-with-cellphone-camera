a = [n for n in range(20) if n % 2 == 0]

nums_list = [1, 2, 3]
names_list = ['Joa', 'Margot', 'Emi']
surnames_list =['Porro', 'Robbie', 'Porro']
"""
my_tulip = list(map(lambda n: n * 22, nums))
my_list = [(number, name) for number, name in nums]
print(my_tulip)
print(my_list)
"""
print("  HEllo   ".strip().title())
full_names = list(zip(names_list, surnames_list))
my_dict = {name: surname for names, surnames in list(zip(names_list, surnames_list))}
print(my_dict)