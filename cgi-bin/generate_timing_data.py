#! /usr/bin/python3
# -*- coding: gbk -*-
import cgi
import athletemodel
import yate

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header(athlete_name+"���鱨�ռ�"))
print(yate.header("��ɫӢ����:"+athletes[athlete_name].ename+",����:"+athletes[athlete_name].dob+"."))
print(yate.para("�ǳ���Ʒ:"))
print(yate.para(athletes[athlete_name].movie))
print(yate.include_footer({"������ҳ":"/index.html","ѡ��������ɫ":"generate_list.py"}))
