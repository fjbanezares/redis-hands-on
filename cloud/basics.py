import redis

r = redis.Redis(
    host='redis-16287.c302.asia-northeast1-1.gce.cloud.redislabs.com',
    port=16287,
    password='WpnrnezZHgXgnsM9K1xEbzwLwrVTRym6')

r.set('javi', 'profesor')
desde_redis = r.get('javi')
print(desde_redis)

print(r.exists('key1'))
print(r.get('key1'))