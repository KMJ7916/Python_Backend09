# file_reader.py

def write_file_out(file_path):
  try:
    with open(file_path, 'a') as f:
      print('모듈에 쓰기 함수')
      f.write('new contents')
  except FileNotFoundError:
    print("파일을 읽을 수 없습니다!")

print("file_reader의 __name__입니다.:".__name__)
if __name__=="__main__":
    read_file_out()
