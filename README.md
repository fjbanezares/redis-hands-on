# redis-hands-on


## Try Redis
Feeling lazy?
One of the main authors (https://github.com/antirez/)  manages this site to give it a try...  https://try.redis.io

```shell
SET server:name "fido"
GET server:name
# As simple as this

EXISTS server:name
(integer) 1

# Not TRUE/FALSE, just 1 or 0 integers

SET connections 10
INCR connections 
INCR connections 
DEL connections
GET connections # Give as Nil (like a null)
INCR connections 
GET connections # Give us a one
INCRBY connections 100 => 101
DECR connections => 100
DECRBY connections 10 => 90

# We could use just
x = GET count
x = x + 1
SET count x
# But this is not atomic, results may be unpredictable
# All the Redis operations implemented by single commands are atomic, 
# including the ones operating on more complex data structures. 
# So when you use a Redis command that modifies some value, 
# you don't have to think about concurrent access.

# Remember availability vs consistency, to achieve this result, some way we need to lock on the variable
# In this case looks like a key level lock

SET resource:lock "Redis Demo"
EXPIRE resource:lock 120
# TTL (Time to Live) gives us the remaining time, once is finished a -2 is returned (there is no longer that key)
TTL resource:lock => -2
PTTL key # the same but multiplied by 1000, gives the millisecods


# Wait two minutes and the key will not be there

SET resource:lock "Redis Demo 1"
EXPIRE resource:lock 120
TTL resource:lock => 119 #119 seconds remain
SET resource:lock "Redis Demo 2"
TTL resource:lock => -1 # no timer, when redefine the variable, the timer is lost


#Lists
# A list is a series of ordered values. Some of the important commands for interacting with lists are RPUSH, LPUSH, LLEN, LRANGE, LPOP, and RPOP. You can immediately begin working with a key as a list, as long as it doesn't already exist as a different type.
# This concept is generally true for every Redis data structure: you don't create a key first, and add things to it later, but you can just directly use the command in order to add new elements. As side effect the key will be created if it did not exist. Similarly keys that will result empty after executing some command will automatically be removed from the key space.

RPUSH friends "Alice"
RPUSH friends "Bob"
LPUSH friends "Sam"

LRANGE friends 0 -1 # Give me from the first (0) to the last (-1), we could say LRANGE friends 0 N-1 if we know N

LPOP friends => "Sam" # removes first element
RPOP friends => "Bob" # removes last

LLEN friends # Size of the list

RPUSH friends 1 2 3 # add several elements

# SETS

SADD superpowers "flight"
SADD superpowers "x-ray vision" "reflexes"
# try two times, the set is identical, idempotent
SREM superpowers "reflexes" => 1
SREM superpowers "making pizza" => 0 # member was not there
SMEMBERS superpowers

# To test if flight is a member of superpowers ...
SISMEMBER superpowers "flight"

SADD birdpowers "pecking"
SADD birdpowers "flight"

# The union of two sets
SUNION superpowers birdpowers

SADD superpowers "flight" => 0 # 0 because it was there and nothing happened
SADD superpowers "invisibility" => 1 # 1 element added because it was not there

SADD letters a b c d e f => 6
# ets also have a command very similar to LPOP and RPOP 
# in order to extract elements from the set and return them to the client 
# in a single operation. However since sets are not ordered 
# data structures the returned (and removed) 
# elements are totally casual in this case.
SPOP letters 2 => 1) "c" 2) "a" # pop removes and show
SADD letters a b c d e f => 2 # Added  only 2 as 4 of them still was in the set
# There is also a command to return random elements without 
# removing such elements from the set, it is called SRANDMEMBER. 
# You can try it yourself, the arguments are similar to SPOP, 
# but if you specify a negative count instead of a positive one,
# it may also return repeating elements.


```

## Install Redis on Mac

But what is install redis on Mac??

We install the engine, we will be able to persiste, we have the memory structure
```shell

```