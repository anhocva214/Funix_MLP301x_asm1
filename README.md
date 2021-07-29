# MLP301x_1.2-A_VN Giới thiệu về Học máy - Assignment 1 
## Hướng dẫn sử dụng `project`

1. Cài đặt thư viện:
    ```
    pip install -r requirements.txt
    ```

2. Khởi chạy project;
    ```
    python lastname_firstname_grade_the_exams.py <class_name> <class_name> ... <class_name>
    ```

    Trong đó: <br/>
    `<class_name>` là tên **lớp** bạn muốn phân tích. Tên lớp với trùng với tên file hiện có

3. Kết quả demo:
    ```
    python lastname_firstname_grade_the_exams.py class1
    ```
    ```
    Successfully opened class1.txt
    **** ANALYZING ****
    No errors found!
    **** REPORT ****
    Total valid lines of data: 20
    Total invalid lines of data: 0
    Mean (average) score: 75.6
    Highest score: 91
    Lowest score: 59
    Range of scores: 32
    Median score: 73.0
    ```