class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

def divide(x, y):
    return x/y

def add(x, y):
    return x+y

def reverse_string(s):
    return s[::-1]

def sort_list(lst):
    return sorted(lst)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

def divide_new(a, b):
    if b==0:
        raise ValueError("Cannot divide by Zero")
    return a/b

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

class ChatGPTAPI:
    def service_method(self):
        pass

class EmailService:
    def send_email(self, address, content):
        pass

class APIClient:
    def fetch_data(self,url):
        pass

class DatabaseClient:

    def connect(self):
        pass

class TemporaryDatabase:
    def __init__(self):
        self.contents=[]
    def connect(self):
        print("연결되었습니다.")
    def disconnect(self):
        print("연결이 끊겼습니다.")
    def insert(self,val):
        self.contents.append(val)
    def contains(self,val):
        return val in self.contents


class NetworkConnection:
    def open(self):
        print("네트워크에 연결하였습니다.")

    def close(self):
        print("네트워크에 연결 실패했습니다.")

    def send(self, val):
        print("메시지를 전송합니다 : {}".format(val))
        return val
    
class A:
    def __init__(self) -> None:
        pass
    def some_func(self, msg : str ='123') -> dict:
        return {'a':1}