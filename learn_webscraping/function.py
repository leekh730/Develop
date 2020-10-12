# def fuction_name(parameters, ...):
#     function_suite
#     return [expression]

# result = function_name(parameters, ...)

def sum():
    result = 21 + 14
    print("Inside the function : ", result)
    return result
total = sum()
print("Outside the function : ", total)
total = sum() + 15
print("Outside the function : ", total)


def print_info(name, age = 35):
    print("Name: ", name)
    print("Age: ", age)
    return
print_info(age=50, name="miki")
print_info(name="miki")
print_info("John", 40)
print_info(80,"Silvia") # 이것 처럼 parameter의 순서가 바뀌면 안됨!!
