import requests
from lxml import etree
import re
from doubandb import DoubanDb

class DouBan:
    def __init__(self):
        self.starturl = 'https://movie.douban.com/chart'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def getContent(self):
        html = requests.get(self.starturl,headers=self.headers).text
        # print(html)
        response = etree.HTML(html)
        # print(response)

        film_data_list = []
        content_files = response.xpath('//div[@class="pl2"]')
        for content_file in content_files:
            film_data = {}
            # 电影名称
            title = content_file.xpath('./a/text()')[0].strip().split('/')[0].strip()
            print("title:",title)
            film_info = content_file.xpath('./p/text()')[0]
            # print("film_info:",film_info)
            filmtime_country = film_info.split('/', 1)[0]
            # print("filmtime_country:",filmtime_country)
            film_actors = film_info.split('/', 1)[1]
            # print("film_actor:", film_actors)
            filmtime_country_regx = re.compile('(\d{4}[-/]\d{2}[-/]\d{2})\((.*?)\)')
            film_time_country = re.findall(filmtime_country_regx,filmtime_country)[0]
            film_time = film_time_country[0]
            # print("film_time:",film_time)
            film_country = film_time_country[1]
            # print("film_country:", film_country)
            film_star = content_file.xpath('./div[@class="star clearfix"]/span[2]/text()')[0]
            # print("fillm_star:",film_star)
            film_remarks = content_file.xpath('./div[@class="star clearfix"]/span[3]/text()')[0]
            price_regx = re.compile('(\d+)')
            film_remark = price_regx.findall(film_remarks)[0]
            # print("price_num:",film_remark)
            film_data["title"] = title
            film_data["film_actors"] = film_actors
            film_data["film_time"] = film_time
            film_data["film_country"] = film_country
            film_data["film_star"] = film_star
            film_data["film_remark"] = film_remark
            film_data_list.append(film_data)
            # i += 1
        print("film_data_list", film_data_list)
        return film_data_list

if __name__ == '__main__':
    douban = DouBan()
    data = douban.getContent()
    doubandb = DoubanDb()
    # doubandb.delete()
    doubandb.insert(data)
