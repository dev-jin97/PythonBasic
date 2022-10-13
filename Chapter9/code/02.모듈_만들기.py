import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAutor()

# 클래스 사용
pay_info = pay_module.Pay("A1012023", 13000, "2022-10-13")

print(pay_info.get_pay_info())

print(pay_module.__name__)