#! /usr/bin/python3
# -*- coding: utf-8 -*-
import athletemodel
import yate
import glob

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("老司机 Silence 的资源收藏"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("请选择你想要深入了解的角色:"))

for each_athlete in athletes:
	print(yate.radio_button("which_athlete",athletes[each_athlete].name))
print(yate.end_form("选择"))

print(yate.include_footer({"返回首页":"/index.html"}))
