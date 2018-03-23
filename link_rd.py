from redis import StrictRedis


def main():
    if __name__ == '__main__':
        try:
            #创建StrictRedis对象，与Redis数据库连接
            sr = StrictRedis(host='localhost',port=6379,db=1)
            #使用sr对象对数据库进行操作
            # result = sr.set('bb',23)
            #修改bb的值
            # result = sr.set('bb','itcast')
            #删除键值
            # result = sr.delete('bb')
            #获取所有键名
            result = sr.keys()
            #打印返回结果
            print(result)
        except Exception as e:
            print(e)


main()

