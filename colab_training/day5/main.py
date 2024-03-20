#debug
import file_reader
import file_writer

def job():
    print("파일을 읽고 쓰는 서비스")
    file_reader.read_file_out('test. txt')
    file_writer.write_file_out('test. txt')
print("main.py의 __name__:",__name__)


#def dummy():
    #print("Dummy Function")

#print("main.py의 __name__:",__name__)

if __name__=="__main__":
    job()