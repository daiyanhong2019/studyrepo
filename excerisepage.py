import requests
from lxml import etree

class excerisepage:
    def __init__(self):
        self.starturl = 'http://www.glidedsky.com/level/web/crawler-basic-2'
        # self.post_url = 'http://www.glidedsky.com/login'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
            # "Cookie": "_ga=GA1.2.518339943.1599996718; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1599996718,1600094873; __gads=ID=c76b21dc9f719139:T=1600094918:S=ALNI_Mam7gnb0_x3JNC_M8qrcoi4yZBVMw; _gid=GA1.2.182225057.1600265209; footprints=eyJpdiI6IlBwRjZsTVwvU1JlWW1wNFwvbjMzYnhLQT09IiwidmFsdWUiOiJVakdUTkw0WFVtdVVGeU5WUVplMHJudUdRY2M0YjdudUFvRk1BVjJxaGRqRTE1WE5hYnYzMTRnNk42bFNzTVI1IiwibWFjIjoiMGVkM2E1NGQwNjZlZmRhNDJjZTg1OTM4MjE3YmJlYWExMTExMjYwMGM4NmZmZWVmMTZlNjYwNzlmNjJkZTUwMSJ9; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IjVLXC9SQUFJdnV5UFhISTNEWHFFYlp3PT0iLCJ2YWx1ZSI6ImJ2bTJlUmNoV2I0ZXZrc1FkUnhzSUhkSkJ3NzhtOWkwMjZMclVnaGtvRThsZ1wvalwvUmFNeThkY0N1XC9oZFJEdzgiLCJtYWMiOiI2OTE2MDc5YzcwZmJhOTUxM2MxMjExNWNmN2I3ZTgyMzA5ZTYxYmM1NmY0NDM5OGIyYTk3ZDc1YzVmMjVlNDFmIn0%3D; glidedsky_session=eyJpdiI6InIrMlpBcUROSzdPWTZFVmZSNDVadFE9PSIsInZhbHVlIjoiNVBDemcxb1wvbFRXN1huVHFpUGQ2bGJwNTlEbzJuK0RLNTl5UTlaZGRRanIySnhDSGRMY2tOZWFhUm5VNGh0Y28iLCJtYWMiOiJlNmEzMzIwMjcxNjVhNDE4ZmZkNzY5NmZlNTczMDMyNGFkMzY0OTM5NmY1MzQ4MTY1ZjZjMTk0OGM4MGI4NTY3In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1600352877"
            "Cookie": "_ga=GA1.2.518339943.1599996718; __gads=ID=c76b21dc9f719139:T=1600094918:S=ALNI_Mam7gnb0_x3JNC_M8qrcoi4yZBVMw; _gid=GA1.2.182225057.1600265209; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1599996718,1600094873,1600354660; footprints=eyJpdiI6Inl6cE12Wm5QR2Fab0hPWU16Y1k5Ync9PSIsInZhbHVlIjoiXC94QkFUekpieW1PMitlU1JvbG1GVitXUVRnZk9nZkluRitRekZuSmo5SkpjY0x3ZE54TXM4cThcL3dFMElvQmVoIiwibWFjIjoiMGNiYzYxZDllZTFjYWFmZGI0MzNjOTM2YTZlNGNhZDY1MDRiMWZhZWYzNzE2ZTdjZjY3ZTczM2U4Yjg3ZTAwNCJ9; XSRF-TOKEN=eyJpdiI6IllZbVBqaG5Jb2RJQXJJeVBNRFI0Znc9PSIsInZhbHVlIjoiNFIwTVBmZ0dNUFZOMktRYmc2V3NQQUxqZEtVQlwvbHM1SkxTQjY1UlQ5RVk5TzVNUmhlOXN2Y0dic1wvRUZPWkVEIiwibWFjIjoiYmU1ZTk0YjQ2YjhjMDgwYWRkMGQ2MDU3YmY2NDQxNzhhMTllZDIzNTNjZmRmZTljZGJjN2VhYjIwZDU5NTYyYyJ9; glidedsky_session=eyJpdiI6IkNRc2FiUEF3VWFqMmNVR0ZBeHkyemc9PSIsInZhbHVlIjoiRWxKbU5vcWJFTms4cWp6WGxTYkxsSmZqVTRJV21MVGxWcTF1VDMwM09kODhPT0lpNkRycStsdzNaV3VDdnZybyIsIm1hYyI6IjhjMTk0MzNmMGMyNzMxODkxNGI1YTMzODZhMmI3MTQ2ODcwMjFlNjFlMmFhNzExM2Y3ZjU2ZWM3NWM2NDk3NmYifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1600432408"
        }
        # self.pageurl = 'http://www.glidedsky.com/level/web/crawler-basic-2?page={}'
    def getonepage(self,page):
        url = 'http://www.glidedsky.com/level/web/crawler-basic-2?page={}'.format(page)
        html = requests.get(url=url,headers=self.headers).text
        # print(html)
        response = etree.HTML(html)
        numberlist = response.xpath('//div[@class="row"]/div')
        sum = 0
        for number in numberlist:
            num = number.xpath('./text()')[0]
            sum += int(num)
        print(sum)
        return sum

if __name__ == '__main__':
    expage =excerisepage()
    sumpage = 0
    for i in range(1001):
        onepage = expage.getonepage(i)
        sumpage += onepage
    # print(sumpage)  2690667