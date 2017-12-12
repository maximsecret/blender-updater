#!/usr/bin/env python3
# coding: utf-8
import os,sys

import p_b
import p_b28
def get_path():
    str = os.path.abspath(__file__)
    return(str[:-7])
def check_workdir():
    newpath = (get_path()+"blender-git")
    if not os.path.exists(newpath):
        print("WorkDir - Directory was been created - " + newpath)
        os.makedirs(newpath)
    else:
        print("WorkDir - All ok - "+get_path())
    print("----------*----------")
def os_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#############CONFIG#############
c_flags= "-O2 -march=native -mtune=native -pipe"
b_use_cuda="TRUE" # TRUE or FALSE
b_cuda_arch="sm_50"   # get this https://developer.nvidia.com/cuda-gpus
i_path="$HOME/Documents/Software/"   #Install Path
b_use_flags="-DWITH_C11=TRUE -DWITH_CXX11=TRUE -DWITH_CODEC_FFMPEG=TRUE -DWITH_MOD_OCEANSIM=TRUE -DWITH_FFTW3=TRUE"
################################
b_flags=b_use_flags+" -DWITH_CYCLES_CUDA_BINARIES="+b_use_cuda+" -DCYCLES_CUDA_BINARIES_ARCH=\""+b_cuda_arch+"\" -DCUDA_NVCC_FLAGS_RELEASE=\"-O2\""
b_path = (get_path()+"blender-git")
info_text="""[0] Git pull all blenders
----------*----------
[b0] Refresh blender(or create)
[b1] Configure Blender
[b2] Build Blender
[b3] Install Blender
[bf] All and Fast
----------*----------
[2b0] Refresh blender(or create)
[2b1] Configure Blender
[2b2] Build Blender
[2b3] Install Blender
[bf28] All and Fast
----------*----------
[b] blender and blender28
----------*----------"""

def sx(inp, p_b, x='b'):
    if inp in [str(x) + '0']:
        os_clear()
        p_b.b0()
    elif inp in [str(x) + '1']:
        os_clear()
        p_b.b1()
    elif inp in [str(x) + '2']:
        os_clear()
        p_b.b2()
    elif inp in [str(x) + '3']:
        os_clear()
        p_b.b3()


def main():
    check_workdir()
    p_b.set_var(b_flags,c_flags,i_path,b_path)
    p_b28.set_var(b_flags,c_flags,i_path,b_path)

    while True:
        print(info_text)
        inp = input()
        sx(inp, p_b)
        sx(inp, p_b28,'2b')
        if inp in ['0']:
            p_b.b0()
            p_b28.b0()
        elif inp in ['bf']:
            os_clear()
            p_b.b0()
            p_b.b1()
            p_b.b2()
            p_b.b3()
        elif inp in ['bf28']:
            os_clear()
            p_b28.b0()
            p_b28.b1()
            p_b28.b2()
            p_b28.b3()
        elif inp in ['b']:
            p_b.b0()
            p_b28.b0()
            p_b.b1()
            p_b.b2()
            p_b.b3()
            p_b28.b1()
            p_b28.b2()
            p_b28.b3()

main()
