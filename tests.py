#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main() :
    working_dir ="calculator"
    
    #Get Files info Test run

    #root_contents = get_files_info(working_dir)
    #print(root_contents)
    
    #pkg_contents = get_files_info(working_dir,"pkg")
    #print(pkg_contents)


    #pkg_contents = get_files_info(working_dir,"/bin") #Exception test
    #print(pkg_contents)

    #pkg_contents = get_files_info(working_dir,"../") #Exception test
    #print(pkg_contents)

    #Read File Contents Test run

    # file_content = get_file_content(working_dir,"lorem.txt")
    # print(file_content)

    # file_content = get_file_content(working_dir,"main.py")
    # print(file_content)

    # file_content = get_file_content(working_dir,"pkg/calculator.py")
    # print(file_content)

    # file_content = get_file_content(working_dir,"pkg/notexists.py") #Exception test
    # print(file_content)

    # file_content = get_file_content(working_dir,"/bin/cat") #Exception test
    # print(file_content)


    #Write file Test run 

    # print(write_file(working_dir,"lorem.txt","wait, this is not lorem ipsum"))

    # print(write_file(working_dir,"pkg/morelorem.txt","more lorem ipsum file.."))

    # print(write_file(working_dir,"/tmp/tmp.txt","this should not be allowed.."))

    # print(write_file(working_dir,"pkg2/tmp.txt","this should  be allowed.."))


    #Run Python File Test run

    # print(run_python_file(working_dir,"main.py"))
    # print(run_python_file(working_dir,"tests.py"))
    # print(run_python_file(working_dir,"../main.py"))
    # print(run_python_file(working_dir,"nonexistent.py"))
    print(run_python_file(working_dir,"main.py",["3 + 5"]))



main()    