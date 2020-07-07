import json

from django.test import TestCase

# Create your tests here.
import requests
# class api():
#
#     def test(self,url):
#         res = requests.request(url=url,method='post')
#         return res
#
# if __name__ == '__main__':
#     url = "http://127.0.0.1:8000/index/"
#
#     run = api.test('post',url)
#     print(run)
#     print(run.content)
#     print(run.text)



class api():

    def test(self,url,data):
        res = requests.request(url=url,method='post',data=data)
        return res

if __name__ == '__main__':
    url = "http://127.0.0.1:8000/register/"
    data={
       'username':123,
        'password':123,
        'f_pwd':123
    }

    run = api.test('POST',url,data=data)
    print(run)

    print(run.text)
