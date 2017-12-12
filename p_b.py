#!/usr/bin/env python3
# coding: utf-8
import multiprocessing
import os

b_flags="local"
c_flags="local"
i_path="local"
b_path="local"

def set_var(M_b_flags,M_c_flags,M_i_path,M_b_path):
	global b_flags,c_flags,i_path,b_path
	b_flags = M_b_flags
	c_flags = M_c_flags
	i_path = M_i_path
	b_path = M_b_path



#DEBUG
#set_var("global","global","global")
#show_var()



def b_create():
	os.system("cd " + b_path + " && git clone git://git.blender.org/blender.git && cd blender && git submodule update --init --recursive && git submodule foreach git checkout master && git submodule foreach git pull --rebase origin master")
	print("----------------BLENDER_PULL_END----------------")

def b_pull():
	#os.system("cd " + get_path() + "/blender-git/blender && git pull --rebase && git submodule foreach git pull --rebase origin master")
	os.system("cd " + b_path + "/blender && make update")
	print("----------------BLENDER_PULL_END----------------")

def b_clean():
	os.system("cd " + b_path + "/build && make clean -j4")

def b0():
	newpath = (b_path+"/blender")
	if not os.path.exists(newpath):
		print("CreateDir")
		b_create()
	else:
		print("Pull Dir")
		b_pull()

def b1():
	if not os.path.exists(b_path+'/build'):
		os.makedirs(b_path+'/build')
	if not os.path.exists(b_path+'/BlenderMyChanges'):
		print("Without folder "+ b_path+'/BlenderMyChanges')
		os.system("cd " + b_path + "/build && rm -rf * && cmake "+b_flags+" -DCMAKE_CXX_FLAGS_RELEASE=\"" + c_flags +"\" -DCMAKE_C_FLAGS_RELEASE=\"" + c_flags +"\" -DCMAKE_INSTALL_PREFIX=\"" + i_path + "blender/\" ../blender/")
	else:
		print("With folder "+ b_path+'/BlenderMyChanges')
		if not os.path.exists(b_path+'/tmp_blender'):
			os.makedirs(b_path+'/tmp_blender')
		os.system("cd " + b_path + "/ && rm -rf tmp_blender/* && cp -R blender/* tmp_blender/ && cp -R BlenderMyChanges/* tmp_blender/")
		os.system("cd " + b_path + "/build && rm -rf * && cmake "+b_flags+" -DCMAKE_CXX_FLAGS_RELEASE=\"" + c_flags +"\" -DCMAKE_C_FLAGS_RELEASE=\"" + c_flags +"\" -DCMAKE_INSTALL_PREFIX=\"" + i_path + "blender/\" ../tmp_blender/")
		print("----------------BLENDER_CONFIGURE_END----------------")



def b2(x = 0):
	if(x == 0):
		make_j = multiprocessing.cpu_count() #Determine automatically
	elif(x == 1):
		make_j = "1"
	elif(x == 2):
		make_j = "2"
	elif(x == 3):
		make_j = "3"
	elif(x == 4):
		make_j = "4"
	else:
		print("Input make -j?")
		make_j = raw_input()

	os.system("cd " + b_path + "/build && make -j" + str(make_j))
	print("----------------BLENDER_BUILD_END----------------")

def b3():
	os.system("cd " + b_path + "/build && make install -j" + str(multiprocessing.cpu_count()))
	print("----------------BLENDER_INSTALL_END----------------")
