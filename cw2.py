import argparse
import sys
from GUIs import guiCode
from tasks import task3,task4,task2,task5And6
from os import path





def TaskManager(argsdic):  #calls respective tasks with id
      if (argsdic['task_id'].strip() == '2a'):
          if argsdic['document_uuid']:
              task2.task2a(argsdic['filename'].strip()).VeiwCountry(argsdic['document_uuid'].strip())
          else:
              print('Document_uuid not Entered for this task, Application terminated')
              return;

      elif(argsdic['task_id'].strip() == '2b'):
          if argsdic['document_uuid']:
              task2.task2b(argsdic['filename'].strip()).VeiwContient(argsdic['document_uuid'].strip())
          else:
              print('Document_uuid not Entered for this task, Application terminated')
              return;
      elif(argsdic['task_id'].strip() == '4'):
          dta = task4.task4d(argsdic['filename'].strip()).avid_readers()
          print(dta.head(10))
          dta.to_json('./Output/task4.json')
          return;

      elif(argsdic['task_id'].strip() == '3a'):
          if argsdic['document_uuid']:
              task3.task3a(argsdic['filename'].strip()).VeiwBrowserDoc(argsdic['document_uuid'].strip())
          else:
              task3.task3a(argsdic['filename'].strip()).VeiwBrowser()
          return;

      elif (argsdic['task_id'].strip() == '3b'):
          if argsdic['document_uuid']:
              task3.task3b(argsdic['filename'].strip()).VeiwBrowserNameDoc(argsdic['document_uuid'].strip())
          else:
              task3.task3b(argsdic['filename'].strip()).VeiwBrowserName()
          return;
      elif(argsdic['task_id'].strip() == '5d'):
          if argsdic['document_uuid']:
              if argsdic['user_uuid']:
                  a = task5And6.task5(argsdic['filename'].strip()).AlsoLikes(argsdic['document_uuid'].strip(),argsdic['user_uuid'].strip())
                  print(a.head(10))
                  a.to_json('./Output/task5d.json')
              else:
                  a = task5And6.task5(argsdic['filename'].strip()).AlsoLikes(argsdic['document_uuid'].strip())
                  print(a.head(10))
                  a.to_json('./Output/task5d.json')

          else:
              print('Document_uuid not Entered for this task, Application terminated')
              return;
      elif(argsdic['task_id'].strip() == '6'):
          if argsdic['document_uuid']:
              if argsdic['user_uuid']:
                  task5And6.task6(argsdic['filename'].strip()).DotPlot(argsdic['document_uuid'].strip(),
                                                                       argsdic['user_uuid'].strip())
              else:
                  task5And6.task6(argsdic['filename'].strip()).DotPlot(argsdic['document_uuid'].strip())


          else:
              print('Document_uuid not Entered for this task, Application terminated')
              return;
      else:
          print('Error with Inputs, Application terminated')
      return;








# Define the arguments for command line usage
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, help=" Name or Path of file(.json)(Reqiured)")
parser.add_argument("-u", "--user_uuid", type=str, help="User id of visitor ")
parser.add_argument("-d", "--document_uuid", type=str, help="Document id of the document")
parser.add_argument("-t", "--task_id", type=str,choices=('2a', '2b', '3a','3b' ,'4' ,'5d' , '6', '7'), help="ID of task (Required)")

# Reads the arguments from command line
try:                                   #Try and catch to prevent any wrong entries
    args =parser.parse_args()
except IOError as msg:
    parser.error(str(msg))


argparse_dict = vars(args)
print(argparse_dict)

if path.exists(argparse_dict['filename'].strip()):
    if (argparse_dict['filename'].strip()[-5:] == '.json'):  # Checks if file is json and makes sure file is added

        if (len(sys.argv) == 5) & (
                argparse_dict['task_id'].strip() == '7'):  # There will always be one argument which is this file's name

            try:  # Try and catch to prevent any wrong entries
                print("Loading GUI")
                guiCode.GuiDOCLi(argparse_dict['filename']).Guiload()

            except IOError as msg:
                parser.error(str(msg))
        elif str(argparse_dict['task_id'].strip()):
            if (argparse_dict['task_id'].strip() != '7'):
                TaskManager(argparse_dict)
        else:
            print('Error with Inputs, Application terminated')

    else:
        print('Enter a .json file:, Application terminated')
else:
    print('File Not Found:, Application terminated')



