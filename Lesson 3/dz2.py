def check_ip(ip):
    return all(map(lambda n: False if not n.isdigit() 
                   else (True if int(n) in range(0,256) else False),
                     ip.split('.')))

# def check_n(num):
#     try:
#         return True if int(num) in range(0,256) else False
#     except BaseException:
#         return False

print(check_ip('10.0.1.1'))
print(check_ip('10.0.1.a'))
print(check_ip('10.0.1.276'))
a = True if 1<0 else (2 if 1<0 else 3)
print(a)
print("a".isdigit())
