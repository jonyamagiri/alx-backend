# 0x00. Pagination

> This repository contains the tasks for `Pagination` project and a description of what each program or function does:


## Learning Objectives

	* How to paginate a dataset with simple page and page_size parameters
	* How to paginate a dataset with hypermedia metadata
	* How to paginate in a deletion-resilient manner


* Pagination is a common technique used to divide a large dataset into smaller, more manageable chunks. This is often done to improve performance and reduce the amount of data that needs to be loaded and processed at once.

* When using hypermedia metadata for pagination, the server provides additional information along with the data that enables the client to navigate through the available pages. This information includes links to the first, last, next, and previous pages, as well as the total number of pages and the current page number.

* When deleting items from a paginated dataset, it's important to do so in a deletion-resilient manner to ensure that the pagination remains consistent and accurate. This means that if an item is deleted, the pagination should adjust accordingly and the remaining items should be re-paginated in a way that maintains the same ordering and page structure.


## Tasks

- [x] Task: 0-simple_helper_function.py
- [x] Task: 1-simple_pagination.py
- [x] Task: 2-hypermedia_pagination.py
- [x] Task: 3-hypermedia_del_pagination.py

___


* [test_files](https://github.com/jonyamagiri/alx-backend/tree/main/0x00-pagination/test_files)


