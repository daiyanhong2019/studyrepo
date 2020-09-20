import requests
from lxml import etree

class exerise:
    def __init__(self):
        self.starturl = 'http://www.glidedsky.com/level/web/crawler-basic-1'
        # self.post_url = 'http://www.glidedsky.com/login'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
            "Cookie": "_ga=GA1.2.518339943.1599996718; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1599996718,1600094873; __gads=ID=c76b21dc9f719139:T=1600094918:S=ALNI_Mam7gnb0_x3JNC_M8qrcoi4yZBVMw; _gid=GA1.2.182225057.1600265209; footprints=eyJpdiI6IlBwRjZsTVwvU1JlWW1wNFwvbjMzYnhLQT09IiwidmFsdWUiOiJVakdUTkw0WFVtdVVGeU5WUVplMHJudUdRY2M0YjdudUFvRk1BVjJxaGRqRTE1WE5hYnYzMTRnNk42bFNzTVI1IiwibWFjIjoiMGVkM2E1NGQwNjZlZmRhNDJjZTg1OTM4MjE3YmJlYWExMTExMjYwMGM4NmZmZWVmMTZlNjYwNzlmNjJkZTUwMSJ9; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6IjVLXC9SQUFJdnV5UFhISTNEWHFFYlp3PT0iLCJ2YWx1ZSI6ImJ2bTJlUmNoV2I0ZXZrc1FkUnhzSUhkSkJ3NzhtOWkwMjZMclVnaGtvRThsZ1wvalwvUmFNeThkY0N1XC9oZFJEdzgiLCJtYWMiOiI2OTE2MDc5YzcwZmJhOTUxM2MxMjExNWNmN2I3ZTgyMzA5ZTYxYmM1NmY0NDM5OGIyYTk3ZDc1YzVmMjVlNDFmIn0%3D; glidedsky_session=eyJpdiI6InIrMlpBcUROSzdPWTZFVmZSNDVadFE9PSIsInZhbHVlIjoiNVBDemcxb1wvbFRXN1huVHFpUGQ2bGJwNTlEbzJuK0RLNTl5UTlaZGRRanIySnhDSGRMY2tOZWFhUm5VNGh0Y28iLCJtYWMiOiJlNmEzMzIwMjcxNjVhNDE4ZmZkNzY5NmZlNTczMDMyNGFkMzY0OTM5NmY1MzQ4MTY1ZjZjMTk0OGM4MGI4NTY3In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1600352877"
        }
    def getcontent(self):
        response = requests.get(url=self.starturl,headers=self.headers)
        html = response.text
        # print(html)
        response = etree.HTML(html)
        numbers = response.xpath('//div[@class="row"]/div')
        # print(numbers)
        sum = 0
        for num in numbers:
            num = num.xpath('./text()')[0]
            print(num)
            sum += int(num)
        print(sum)

if __name__ == '__main__':
    exerise =exerise()
    exerise.getcontent()
