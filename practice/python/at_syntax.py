import functools

user = {"access_level": "guest"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return "error"
#     return secure_function

# @make_secure
# def get_admin_password():
#     return "1234"

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return "error"
        return secure_function
    return decorator

@make_secure("guest")
def get_admin_password(arg1, arg2):
    return f'{arg1} {arg2}1234'

@make_secure("admin")
def make_dashboard_password():
    return "user: user password"

print(get_admin_password("hello", 1))
print(make_dashboard_password())
# print(get_admin_password.__name__)