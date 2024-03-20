from unittest.mock import MagicMock
from calculator import *
import unittest


class TestWithMock(unittest.TestCase):
    def test_external_service(self):
        service = ChatGPTAPI()
        service.service_method = MagicMock(return_value=True)
        self.assertTrue(service.service_method())


# 이메일 서비스
class TestEmailService(unittest.TestCase):
    def test_send_email(self):
        email_service = EmailService()
        email_service.send_email = MagicMock(return_value=True)
        self.assertTrue(email_service.send_email("user@nasa.com", "Hello"))


# API 요청 테스트
    
class TestAPIClient(unittest.TestCase):
    def test_tech_data(self):
        client=APIClient()
        client.fetch_data=MagicMock(return_value={"key:value"})
        self.assertEqual(client.fetch_data("http://"),{"key:value"})

#database 연결

class TestDatabase(unittest.TestCase):
    def test_database_connetion(self):
        db_client=DatabaseClient()
        db_client.connect=MagicMock(return_value=True)
        self.assertTrue(db_client.connect())


class TestFileOperations(unittest.TestCase):
    #test.txt.파일을 열서 읽고, 그 내용을 확인하다.
    #파일을 열고
    def setUp(self) -> None:
        self.file=open('test.txt','w')
    #닫고
    def tearDown(self) -> None:
        self.file.close()
    #test
    def test_write_to_file(self):
        self.file.write("Hello, World!")
        self.file.close()
        with open("test.txt","r") as f:
            self.assertEqual(f.read(),"Hello, World!")

#임시 데이터베이스 데스트
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db=TemporaryDatabase()
        self.db.connect()
    def tearDown(self) -> None:
        self.db.disconnect()
    def test_database_insert(self):
        self.db.insert("data")
        self.assertTrue(self.db.contains("data"))

class TestNetworkConnection(unittest.TestCase):
    def setUp(self):
        self.connection = NetworkConnection()
        self.connection.open()

    def tearDown(self):
        self.connection.close()
        
    def test_send_data(self):
        self.assertTrue(self.connection.send("data"))


#조건부 테스트 실행
#파이썬 버전에 따른 테스트
import sys
@unittest.skipIf(sys.version_info > (3,9),"Test required Python 3.9")
class TestPython310Feature(unittest.TestCase):
    def test_new_feature(self):
        pass
@unittest.skipUnless(sys.platform.startswith("linux"),"Linux")
class TestLinuxSpecific(unittest.TestCase):
    def test_linux_behavior(self):
        pass

import os
@unittest.skipIf(os.environ.get("NO_NETWORK_TESTS"),"")
class TestNetworkFeartures(unittest.TestCase):
    def test_network_call(self):
        pass

if __name__=="__main__":
    unittest.main()
    