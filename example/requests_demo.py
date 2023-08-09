"""
requests 模块
安装： pip install requests
导包：import requests
url: 统一资源定位符是互联网上标准资源地址。互联网上的每一个文件都有一个唯一的 URL
eg:
protocol://host[:port]/path/[?query]#fragment
http://www.itcast.cn/index.html?name=andy&age=18#link
"""
import requests
from requests import Response

'''
http 请求方法
GET	    请求获取URL位置的资源
HEAD	请求获取URL位置资源的响应消息报告，即获得资源的头部信息
POST	请求向URL位置的资源后附加新的消息
PUT	    请求向URL位置存储一个资源，覆盖原URL位置的资源
PATCH	请求局部更新URL位置的资源,即改变该处资源的部分内容
DELETE	请求删除URL位置存储的资源
'''

'''
requests 库中的方法
requsts.requst()	构造一个请求，最基本的方法，是下面方法的支撑
requsts.get()	    获取网页，对应HTTP中的GET方法
requsts.post()	    向网页提交信息，对应HTTP中的POST方法
requsts.head()	    获取html网页的头信息，对应HTTP中的HEAD方法
requsts.put()	    向html提交put方法，对应HTTP中的PUT方法
requsts.patch()	    向html网页提交局部请求修改的的请求，对应HTTP中的PATCH方法
requsts.delete()	向html提交删除请求，对应HTTP中的DELETE方法
'''

'''
==========================================================
                           get
==========================================================
常用参数
params	字典	    url为基准的url地址，不包含查询参数；该方法会自动对params字典编码,然后和url拼接
url	    字符串	requests 发起请求的地址
headers	字典	    请求头，发送请求的过程中请求的附加内容携带着一些必要的参数
cookies	字典	    携带登录状态
proxies	字典	    用来设置代理 ip 服务器
timeout	整型	    用于设定超时时间， 单位为秒
'''
def get_request(url, params=None, **kwargs):
    """
    def get(url, params=None, **kwargs):
    :return: :class:`Response <Response>` object
    """
    response: Response = requests.get(url=url, params=params, **kwargs)
    print(response.__dict__)


'''
==========================================================
                           post
==========================================================
常用参数
data	字典	    作为向服务器提供或提交资源时提交，主要用于 post 请求
json	字典	    json格式的数据， json合适在相关的html
'''
def post_request(url, data=None, json=None, **kwargs):
    """
    def post(url, data=None, json=None, **kwargs):
    :return: :class:`Response <Response>` object
    """
    resp = requests.post(url=url, data=data, headers=headers)
    print(resp.__dict__)


'''
==========================================================
                           response
==========================================================
resp.status_code	        http请求的返回状态，若为200则表示请求成功。
resp.raise_for_status()	    该语句在方法内部判断resp.status_code是否等于200，如果不等于，则抛出异常
resp.text	                http响应内容的字符串形式，即返回的页面内容
resp.encoding	            从http header 中猜测的相应内容编码方式
resp.apparent_encoding	    从内容中分析出的响应内容编码方式（备选编码方式）
resp.content	            http响应内容的二进制形式
resp.json()	                得到对应的 json 格式的数据，类似于字典
'''


'''
==========================================================
                           head
==========================================================
resp.headers 方法反馈头部内容，很少网络流量获得概要信息
'''

def head_request(url, **kwargs):
    """
    def head(url, **kwargs):
    :return: :class:`Response <Response>` object
    """
    resp = requests.head(url)
    print(resp.__dict__)


if __name__ == "__main__":
    # request 访问不了本地服务
    url = "http://localhost:80/order/getOrder/id=1?"
    get_request(url)
    '''
    '''

    # url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
    # data = {
    #     "from": "zh",
    #     "to": "en",
    #     "query": "你好",
    #     "transtype": "translang",
    #     "simple_means_flag": 3,
    #     "sign": "232427.485594",
    #     "token": "bac81618617c89f404859a8ca69b9003",
    #     "domain": "common",
    #     "ts": 16915652
    # }
    # headers= {
    #     'Cache-Control': 'no-cache, private',
    #     'Content-Encoding': 'gzip',
    #     'Content-Type': 'application/json',
    #     'Date': 'Wed, 09 Aug 2023 07:29:58 GMT',
    #     'P3p': 'CP=" OTI DSP COR IVA OUR IND COM "',
    #     'Server': 'Apache',
    #     'Set-Cookie': 'BAIDUID=3BC186A9735FDFCF3C2F1CA1AB036BF6:FG=1; expires=Thu, 08-Aug-24 07:29:58 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1',
    #     'Tracecode': '17988745862800870410080915',
    #     'Vary': 'Accept-Encoding'
    # }
    # post_request(url, data, headers)

    # head_request("https://fanyi.baidu.com/v2transapi?from=zh&to=en")
    '''
    {
      '_content': b'',
      '_content_consumed': True,
      '_next': None,
      'status_code': 200,
      'headers': {
        'Cache-Control': 'no-cache,
        private',
        'Content-Encoding': 'gzip',
        'Content-Type': 'application/json',
        'Date': 'Wed,
        09Aug202307: 29: 58GMT',
        'P3p': 'CP=" OTI DSP COR IVA OUR IND COM "',
        'Server': 'Apache',
        'Set-Cookie': 'BAIDUID=3BC186A9735FDFCF3C2F1CA1AB036BF6: FG=1;expires=Thu,
        08-Aug-2407: 29: 58GMT;max-age=31536000;path=/;domain=.baidu.com;version=1',
        'Tracecode': '17988745862800870410080915',
        'Vary': 'Accept-Encoding'
      },
      'raw': <urllib3.response.HTTPResponseobjectat0x7fdb98033e80>,
      'url': 'https: //fanyi.baidu.com/v2transapi?from=zh&to=en',
      'encoding': 'utf-8',
      'history': [
        
      ],
      'reason': 'OK',
      'cookies': <RequestsCookieJar[
        Cookie(version=0,
        name='BAIDUID',
        value='3BC186A9735FDFCF3C2F1CA1AB036BF6: FG=1',
        port=None,
        port_specified=False,
        domain='.baidu.com',
        domain_specified=True,
        domain_initial_dot=True,
        path='/',
        path_specified=True,
        secure=False,
        expires=1723102198,
        discard=False,
        comment=None,
        comment_url=None,
        rest={
          
        },
        rfc2109=True)
      ]>,
      'elapsed': datetime.timedelta(microseconds=86070),
      'request': <PreparedRequest[
        HEAD
      ]>,
      'connection': <requests.adapters.HTTPAdapterobjectat0x7fdb98133190>
    }
    '''







