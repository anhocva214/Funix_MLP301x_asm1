import numpy as np
import sys


# Functions
def Log(msg, item):
    print(msg)
    print(item)
    
def IsValidTest(test):
    item_split = test.split(",")
    if len(item_split) != 26:
        Log("Invalid line of data: does not contain exactly 26 values:", test)
        return False
        
    elif len(item_split[0]) != 9 or item_split[0][0] != 'N':
        Log("Invalid line of data: N# is invalid:", test)
        return False
    else:
        try:
            num = int(item_split[0][1:])
            return True
        except:
            Log("Invalid line of data: N# is invalid (# is not number)", test)
            return False

def ScoreOfTest(test_list, answer_key):
    answer_key = answer_key.split(",")
    if len(answer_key) != 25:
        print("answer_key is invalid")
        return -1
    else:
        length = len(answer_key)
        score = 0
        for i in range(0, length):
            test_item = test_list[i].replace("\n","").strip()
            if len(test_item) == 0:
                score += 0
            elif test_item == answer_key[i]:
                score += 4
            else:
                score += -1
        return score
            
def ExportFile(student_list, filename):
    with open(filename+".txt", "w+") as file:
        for student in student_list:
            file.write(student.id + "," +str(student.test_score) + "\n")
    pass            

def AnalyzeFile(filename):
    # Khỏi tạo class Student
    class Student:
        def __init__(self, id, test_list):
            self.id = id # mã học sinh
            self.test_list = test_list # danh sách đáp án của học sinh
        def set_score(self, score):
            self.test_score = score 



    ROOT_DATA = "./Data Files/"
    # filename = input("Enter a class file to grade: ")
    data = []
    try:
        with open(ROOT_DATA+filename+".txt", "r") as file:
            print("Successfully opened "+filename+".txt")
            data = file.readlines()
    except:
        print("File cannot be found.")

    print("**** ANALYZING ****")

    total_valid = len(data)
    total_invalid = 0
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    student_list = []


    for item in data:
        if IsValidTest(item) == False:
            total_valid += -1
            total_invalid += 1
        else:
            item_split = item.split(",")
            student = Student(item_split[0], item_split[1:])
            student.set_score(ScoreOfTest(student.test_list, answer_key))
            student_list.append(student) # thêm tất cả các item hợp lệ vào 1 list

    # Nếu tổng dòng hợp lệ không có sự thay đổi thì không có dòng nào bị lỗi
    if total_valid == len(data): 
        print("No errors found!")


    # Trích xuất tất cả điểm vào 1 list
    score_list = []
    for student in student_list:
        score_list.append(student.test_score)

    # Sắp xếp list
    score_list.sort()
    # Chuyển list sang numpy
    np_score = np.array(score_list)


    print("**** REPORT ****")
    print("Total valid lines of data:", total_valid)
    print("Total invalid lines of data:", total_invalid)
    print("Mean (average) score:", np.mean(np_score))
    print("Highest score:", np.max(np_score))
    print("Lowest score:", np.min(np_score))
    print("Range of scores:",  np.max(np_score) - np.min(np_score))
    print("Median score:", np.median(np_score))

    # Xuất file
    ExportFile(student_list, filename+"_grades")
            
# End functions


# AnalyzeFile("class1")
filename_cmd = sys.argv[1:]
for filename in filename_cmd:
    AnalyzeFile(filename);
    print('\n')




    

