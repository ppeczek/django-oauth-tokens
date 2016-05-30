# distributedlock settings
import distributedlock
from django.core.cache import caches


distributedlock.DEFAULT_TIMEOUT = 60 * 5
distributedlock.DEFAULT_MEMCACHED_CLIENT = caches['default']

# import after distributedlock settings
from distributedlock import distributedlock, LockNotAcquiredError
