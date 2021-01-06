#------------------------------------------------------------------------------
            #Author: Spandan Halder
            #Date: 23.10.2020
            #OS: Windows 10
#------------------------------------------------------------------------------
import sys
import os
import re

try:
    fullpath = sys.argv[1]
    filename = os.path.splitext(fullpath)[0].split("\\")[len(os.path.splitext(fullpath)[0].split("\\"))-1]
    file_extension = re.findall(r"[^.]+$",fullpath)
    directory = '\\'.join(map(str, os.path.splitext(fullpath)[0].split("\\")[:len(os.path.splitext(fullpath)[0].split("\\"))-1]))
    runner = ''
    compiled = False
    compiled_prefix = ''
    compiled_runner = ''
    #------------------------------------------------------------------------------
                                        #DYNAMICALLY TYPED
    #------------------------------------------------------------------------------
    if file_extension[0] == 'js':
        runner = "node"
    if file_extension[0] == 'dart':
        runner = 'dart'
    if file_extension[0] == 'py':
        runner = 'python'
    if file_extension[0] == 'go':
        runner = 'go run'

    #-------------------------------------------------------------------------------
                                        #COMPILED
    #-------------------------------------------------------------------------------
    if file_extension[0] == 'c':
        compiled_prefix = "gcc -o " + directory + "\\" + filename
        compiled_runner = directory + "\\" + filename
        compiled = True
    if file_extension[0] == 'cpp':
        compiled_prefix = "g++ -o " +  directory + "\\" + filename
        compiled_runner = directory + "\\" + filename
        compiled = True
    if file_extension[0] == 'java':
        compiled_prefix = "javac"
        compiled_runner = "java -cp " + directory + " " + filename
        compiled = True
    if file_extension[0] == 'kt':
        compiled_prefix = "kotlinc " + " -d " + directory + "\\" + filename + ".jar"
        compiled_runner = "java -jar " + directory + "\\" + filename + ".jar"
        compiled = True
        os.system('cmd /c %userprofile% {} {} || (pause & exit) & start %userprofile%\\launch.cmd {}'.format(compiled_prefix,fullpath,compiled_runner))

    #-------------------------------------------------------------------------------
    if compiled and file_extension[0] not in ['kt']:
        os.system('cmd /k %userprofile%\\compile.cmd {} {} && %userprofile%\\launch.cmd {}'.format(compiled_prefix,fullpath,compiled_runner))
    elif compiled == False:
        os.system('start %userprofile%\\launch.cmd {} {}'.format(runner,fullpath))
except IndexError:
    print("Please Enter A File Name ...")
