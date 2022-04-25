#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 主界面设计
import os.path

filename = 'student.txt'


# 启动程序
def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('请问您是否要退出系统？ Y/N:\n')
                if answer == 'Y' or answer == 'y':
                    print('欢迎使用！！！')
                    break
                else:
                    continue

            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
    pass


# 菜单栏
def menu():
    print('==============学生管理系统===============')
    print('----------------功能菜单----------------')
    print('\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t 5.排序')
    print('\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t 0.退出系统')
    print('--------------------------------------')


# 添加信息
# 1.按照格式录入学生信息(id,姓名,成绩) 2.将录入的信息保存到字典
def insert():
    student_list = []
    while True:
        id = input('请输入id(如1001)')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            English = int(input('请输入英语成绩'))
            clang = int(input('请输入C语言成绩'))
            python = int(input('请输入Python成绩'))
        except ValueError / TypeError:
            print('输入无效，不是整数，请重新输入')
            continue
        # 将录入的信息保存到字典
        student = {'id': id, 'name': name, 'English': English, 'C语言': clang, 'Python': python}
        student_list.append(student)

        answer = input('是否继续添加？ Y/N \n')
        if answer == 'Y' or answer == 'y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕！！！')
    # 保存信息
    pass


# 保存学生信息
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF-8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()
    pass


# 查找学生信息
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            conditions = input('按照id查询请按1，按照姓名查询请按2：')
            if conditions == '1':
                id = input('请输入学生的ID：')
            elif conditions == '2':
                name = input('请输入学生的姓名')
            else:
                print('输入有误，请重新输入')
                search()

            # 查找信息
            with open(filename, 'r', encoding='UTF-8') as r_file:
                student_infos = r_file.readlines()
                for item in student_infos:
                    info = dict(eval(item))
                    if id != '':
                        if id == info['id']:
                            student_query.append(info)
                    elif name != '':
                        if name == info['name']:
                            student_query.append(info)

            # 显示查询的结果
            show_student(student_query)

            # 清空列表
            student_query.clear()
            answer = input('是否继续查找？ Y/N \n')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存任何学生信息')
            return
    pass


# 显示学生信息
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    show_title = '{:^6}\t{:^8}\t{:^8}\t{:^7}\t{:^8}\t{:^8}'
    print(show_title.format('ID', '姓名', '英语成绩', 'C语言成绩', 'Python成绩', '总成绩'))
    # 定义内容显示格式
    show_content = '{:^6}\t{:^8}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(show_content.format(item.get('id'),
                                  item.get('name'),
                                  item.get('English'),
                                  item.get('C语言'),
                                  item.get('Python'),
                                  int(item.get('English')) + int(item.get('C语言')) + int(item.get('Python'))
                                  ))
    pass


# 删除学生信息
def delete():
    while True:
        student_id = input('请输入想要删除的学生ID:')
        if student_id != '':
            # 判断文件是否存在
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student_infos = file.readlines()
            else:
                student_infos = []
            # 标记是否删除
            flag = False

            # 判断读取的内容是否为空
            if student_infos:
                with open(filename, 'w', encoding='UTF-8') as w_file:
                    info = {}
                    for item in student_infos:
                        # eval用来执行字符串表达式,dict进行字符串转字典
                        info = dict(eval(item))
                        # 查询出来的值，不等于给定删除的值，则进行覆盖写
                        if info['id'] != student_id:
                            w_file.write(str(info) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生')
            else:
                print('无学生信息')
                break
            # 显示信息
            show()
        answer = input('是否继续删除？ Y/N \n')
        if answer == 'Y' or answer == 'y':
            continue
        else:
            break
    pass


# 查询所有信息
def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as r_file:
            student_infos = r_file.readlines()
            for item in student_infos:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print('暂未存储任何信息')


# 修改学生信息
def modify():
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as r_file:
            student_infos = r_file.readlines()
    else:
        return
    student_id = input('请输入想要修改的学生ID:')
    with open(filename,'w',encoding='UTF-8') as w_file:
        for item in student_infos:
            info = dict(eval(item))
            a = 0
            if info['id'] == student_id:
                print('找到指定学生信息，可以进行修改')
                while True:
                    try:
                        info['name'] = input('请输入姓名：')
                        info['English'] = input('请输入英语成绩：')
                        info['C语言'] = input('请输入C语言成绩：')
                        info['Python'] = input('请输入Python成绩：')
                    except:
                        print('输入有误，请重新输入')
                    else:
                        break
                w_file.write(str(info) + '\n')
                print('修改成功！！！')
                a = 1
        if a != 1:
            print('未找到相关学生信息')
        answer = input('是否继续修改？ Y/N \n')
        if answer == 'Y' or answer == 'y':
            modify()
    pass

# 按照某成绩排序信息
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as r_file:
            student_list = r_file.readlines()
            student_sort = []
            # 数据类型转换
            for item in student_list:
                student_info = dict(eval(item))
                student_sort.append(student_info)
    else:
        return
    asc_or_desc = input("请选择(0.升序 1.降序)")
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您输入有误，请重新输入')
        sort()

    choice = input('请选择排序的内容(1.按英语成绩排序 2.按python成绩排序 3.按照C语言成绩排序 0.按照总成绩排序)')
    if choice == '1':
        # list.sort(key = None,reverse = False)
        # key   -----接受的参数，类型为函数形式
        # reverse 排序规则 reverse = True 降序 reverse = False
        student_sort.sort(key=lambda s: int(s['English']),reverse=asc_or_desc_bool)
    elif choice == '2':
        student_sort.sort(key=lambda s: int(s['Python']), reverse=asc_or_desc_bool)
    elif choice == '3':
        student_sort.sort(key=lambda s: int(s['C语言']), reverse=asc_or_desc_bool)
    elif choice == '0':
        student_sort.sort(key=lambda s: int(s['English']) + int(s['Python']) + int(s['C语言']), reverse=asc_or_desc_bool)
    else:
        print('您输入的有误，请重新输入')
        sort()
    show_student(student_sort)

# 统计学生总人数
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='UTF-8') as r_file:
            student_infos = r_file.readlines()
            if student_infos:
                print('一共有{}名学生'.format(len(student_infos)))
            else:
                print('尚未录入学生信息')
    else:
        print('暂未存储数据信息')
    pass


if __name__ == '__main__':
    main()
