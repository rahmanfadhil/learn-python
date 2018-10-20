my_name = "Ryu"


def print_name():
    global my_name
    my_name = "Yoshi"
    print(f'the name inside the function is {my_name}')


print(f"the name outside the function is {my_name}")
print_name()
print(f"the name outside the function is {my_name}")
