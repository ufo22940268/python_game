#
# Makefile
# ccheng, 2013-10-04 09:40
#

.PHONY: save
save:
	echo "save success"

.PHONY: all
all: list detail
	echo "success"

.PHONY: list
list:
	scrapy crawl list

.PHONY: detail
detail:
	scrapy crawl detail


.DEFAULT_GOAL := all
# vim:ft=make
#

