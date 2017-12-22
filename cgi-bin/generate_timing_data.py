#! /usr/bin/python3
# -*- coding: gbk -*-
import cgi
import athletemodel
import yate

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header(athlete_name+"的情报收集"))
print(yate.header("角色英文名:"+athletes[athlete_name].ename+",生日:"+athletes[athlete_name].dob+"."))
print(yate.para("登场作品:"))
print(yate.para(athletes[athlete_name].movie))
print(yate.include_footer({"返回首页":"/index.html","选择其他角色":"generate_list.py"}))
