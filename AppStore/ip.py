import  requests
order = "c3134e8283deabba5a25bc49ad3061ff";
    # 获取IP的API接口
apiUrl = "http://dynamic.goubanjia.com/dynamic/get/c3134e8283deabba5a25bc49ad3061ff.html?sep=3" + order + ".html";

res = requests.get(apiUrl).content.decode()
print(res)