import redis

# 默认如下
# sr = redis.StrictRedis(host="localhost", port=6379, db=0)

# 可以简写
# sr = redis.StrictRedis()

sr = redis.StrictRedis(host="192.168.85.128")

res = sr.keys("*")
res = sr.get("price")
sr.close()
print(type(res.decode()))
print(res)