def mixed_params(age, address, name="아이유", *args, **kwargs):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)

mixed_params(20, "seoul", "정우성", "01012341234", "male" ,mobile="01012341234")