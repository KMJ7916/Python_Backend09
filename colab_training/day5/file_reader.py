# file_reader.py

def read_file_out(file_path):
  try:
    with open(file_path, 'r') as f:
      print(f.read())
  except FileNotFoundError:
    print("파일을 읽을 수 없습니다!")

print("file_reader의 __name__입니다.:".__name__)
if __name__=="__main__":
    read_file_out()
