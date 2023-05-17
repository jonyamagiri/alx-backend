# 0x01. Caching

> This repository contains the tasks for `Caching` project and a description of what each program or function does:


## Learning Objectives

	* What a caching system is
	* What FIFO means
	* What LIFO means
	* What LRU means
	* What MRU means
	* What LFU means
	* What the purpose of a caching system
	* What limits a caching system have


* A caching system in Python is a mechanism that stores the results of expensive or time-consuming operations in memory so that subsequent requests for the same data can be retrieved quickly without re-computing or re-fetching it. It aims to improve the performance and efficiency of an application by reducing the time and resources required for repetitive tasks.

* Here are some key purposes and benefits of a caching system:

- **Faster Data Access:** By caching frequently accessed data, a caching system allows subsequent requests for that data to be served directly from the cache, which is typically much faster than fetching the data from its original source, such as a database or remote service. This reduces the response time of the application and improves user experience.
- **Reduced Resource Usage:** Caching reduces the need to repeatedly perform expensive operations or retrieve data from slower storage systems. 
- **Scalability:** Caching systems help improve the scalability of an application by reducing the load on backend systems.
- **Lower Latency:** Caching systems can significantly reduce latency by serving data from the cache, which is often located closer to the application or users. 
- **Better Performance for Expensive Operations:** Caching systems can be used to cache the results of computationally expensive operations, such as complex calculations or data transformations.
- **Improved Overall System Performance:** By reducing the time and resources required for data retrieval or computation, caching systems contribute to improved overall system performance.


## Tasks

- [x] Task: 0-basic_cache.py
- [x] Task: 1-fifo_cache.py
- [x] Task: 2-lifo_cache.py
- [x] Task: 3-lru_cache.py
- [x] Task: 4-mru_cache.py
- [x] Task: 100-lfu_cache.py

___


