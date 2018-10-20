# def greet(name="Ryu", time="morning"):
#     print(f"Good {time} {name}")
#
#
# # name = input("Your name: ")
# # time = input("What time is it? ")
# # greet(name, time)
#
# greet("Shaun", "Afternoon")
# greet(name="Shaun")


def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)


radius = int(input("Enter a radius: "))
length = int(input("Enter a length: "))

vol(area(radius), length)
