#!/usr/bin/python3
'''WSSQL'''

'''WSSQL - Work Smart Structured Query Language'''

''' WSSQL is to store the data in the form of a comma separated values file and to implement operations like create,search,delete and retrieve the data from the file'''
from pathlib import Path
import os

def find_help(cmd):
    print("WSSQL is a file storage system.")
    print("The data provided is stored in form file. Each table is stored separated in a file.\n")
    print("List of commands availabe:")
    print("--------------------------------------------------")
    print("CREATE - to create a table with the specified name")
    print("       Usage: create table <tablename>")
    print("VIEW   - to view the data in the table")
    print("       Usage: view from <tablename>")
    print("WRITE  - to write the data in to the created table.")
    print("       Usage: write into <tablename> \nAfter executing successfully you will be prompted to enter the values.")
    print("TABLES - to list the available tables.")
    print("--------------------------------------------------")
def open_w(filename):
    ''' The open_w function opens the given file
        in the write mode and returns the file pointer
        of the opened file'''
    filename = filename+".txt"
    path = "db_files/"+filename
    try:
        file_write = open(path,"w+")
        return file_write
    except IOError:
        print("Cannot open file.")
        exit(0)

def open_r(filename):
    ''' The open_r function opens the given file
        in the read mode and returns the file pointer
        of the opened file'''
    filename = filename+".txt"
    path = "db_files/"+filename
    try:
        file_read = open(path,"r+")
        return file_read
    except IOError:
        print("Reading Error.")
        exit(0)

def open_a(filename):
    ''' The open_a function opens the given file
        in the append mode for updating purpose'''
    filename = filename+".txt"
    path = "db_files/"+filename
    try:
        file_append = open(path,"a+")
        return file_append
    except IOError:
        print("Cannot append ")
        exit(0)
def check_exist(filename):
    ''' To check whether the file exists or not'''
    filename = filename+".txt"
    file_path = "db_files/"+filename
    my_file = Path(file_path)
    if my_file.exists():
        return True
    else:
        return False
def check_empty(filename):
    '''To check whether the file is empty or not'''
    filename = filename+'.txt'
    file_path = "db_files/"+filename
    if os.path.getsize(file_path)==0:
        return True
    else:
        return False
def write_file(cmd):
    ''' To write into the file'''
    if cmd[1] != 'to'or len(cmd) != 3:
        print("Error in syntax. Excepted: 'to'")
        return 
    filename = "tab_"+cmd[2]
    if not check_exist(filename):
        print("Table "+cmd[2]+" does not exists.")
        return 
    else:
        inp = input("value: ")
        inp = inp+'\n'
        fp = open_a(filename)
        fp.write(inp)
        fp.close()


def create_file(cmd):
    '''To create the table'''

    if cmd[1]!='table':
        print("Error in syntax. Excepted:'table'")
        return 
    elif len(cmd)!=3:
        if len(cmd)==2:
            print("Specify the table name to be created.")
        else:
            print("Error in syntax.")
        return
    
    filename = "tab_"+cmd[2]
    if check_exist(filename):
        print("Table "+cmd[2]+" already exists.")
        return 
    else:
        fp = open_w(filename)
        print("Table created successfully.")
        fp.close()

def retrieve_data(cmd):
    '''To view the data in the table'''
    if cmd[1]!='from':
        print("Error in syntax.  Excepted:'from'")
        return
    elif len(cmd)!=3:
        if len(cmd)==2:
            print("Specify the table to view.")
        else:
            print("Error in syntax.")
        return
    filename ="tab_"+cmd[2]
    if not check_exist(filename):
        print("Table "+cmd[2]+" does not exists.")
    else:
        if not check_empty(filename):
            with open_r(filename) as fp:
                lines = fp.readlines()
                for line in lines:
                    print(line.split(','))
        else:
            print("Table is empty.")
def list_tables(cmd_list):
    files = os.listdir("db_files")
    if len(files)==0:
        print("No Tables found.")
        return 
    print("Available Tables: ")
    print("------------------")
    for file in files:
        print(file.rsplit('.')[0].rsplit('_')[1])
    print("------------------")
def main():
    print("Welcome to WSSQL-v1.0")
   #print("\n")
    print("Type 'help' for help and to show the list of commands.")
    print("-----------------------------------------------------")
    while True:
        try:
            cmd = input("\nwssql>")
        except:
            print("\nBye!")
            exit(1)
        cmd_list = cmd.split(' ')
        for i in range(0,len(cmd_list)):
            cmd_list[i]=cmd_list[i].lower()
        if cmd_list[0] == 'create':
            create_file(cmd_list)
        elif cmd_list[0] == 'view':
            retrieve_data(cmd_list)
        elif cmd_list[0] == 'write':
            write_file(cmd_list)
        elif cmd_list[0] == 'help':
            find_help(cmd_list)
        elif cmd_list[0] == 'tables':
            list_tables(cmd_list)
        elif cmd_list[0] == 'exit':
            print("Bye!")
            exit(0)
        else:
            print("Unknown command.")

if __name__ =="__main__":
    main()
