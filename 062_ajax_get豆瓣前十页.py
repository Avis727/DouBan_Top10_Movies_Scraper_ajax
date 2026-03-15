# _*_ coding : UTF-8 _*_
# @Time : 2025/12/16 04:34
# @Author : Avis
# @File : 062_ajax_get豆瓣前十页
# @Project : PythonProject
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

#start = 0 20 40 60 (page - 1) * 20
#page = 1 2 3 4

#下载豆瓣电影前十页数据
# request object
# obtain response
# download data
import urllib.request
import urllib.parse

def get_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
    data = {
        "start":(page - 1) * 20,
        "limit":20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def download(page, content):
    with open(f"douban_{page}.json", "w", encoding="utf-8") as fp:
        fp.write(content)

def main():
    start_page = int(input("start page:"))
    end_page = int(input("end page:"))
    for page in range(start_page, end_page + 1):
        request = get_request(page)
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        download(page, content)

main()




