from redis import StrictRedis

if __name__ == '__main__':
    #创建StrictRedis对象
    strict_redis = StrictRedis()

    #id为1的用户添加了商品到购物车
    strict_redis.hset('cart_1',1,2)
    strict_redis.hset('cart_1',2,3)

    #取出用户购买的id为1的商品数量，
