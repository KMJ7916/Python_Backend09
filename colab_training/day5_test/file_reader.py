def read_file(file_path):
  """파일 경로를 받아 내용을 출력하는 함수"""
  try:
    with open(file_path,'r')as file:
      print(file.read())
  except FileNotFoundError:
    print("파일을 찾을 수 없다.")