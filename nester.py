#! /usr/local/bin/python3

def print_lol(the_list):
	for each_item in the_list:
		if isinstanse(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)

#
