import math

model_list = []

class MyopiaModel(object):
    def select_model(self):
        # 选择模型
        select_model = int(input("请选择您要测试的模型类型：【1】近视模型p值【2】肥胖模型p值"))
        if select_model == 1:
            num = -5.169
            model_list.append(num)
            economic_zones = int(input("请选择经济片区值：【1】好【2】中"))
            if economic_zones == 1:
                econum = 0.2167
                model_list.append(econum)
            elif economic_zones == 2:
                econum = 0.2689
                model_list.append(econum)
            else:
                print("请输入正确的值")
        elif select_model == 2:
            print('肥胖模型暂未开放')
        else:
            print("请输入正常的模型类型")

    def select_gender(self):

        gender = int(input("请选择性别值：【1】男【2】女"))
        if gender == 1:
            gennum = 0
            model_list.append(gennum)
        elif gender == 2:
            gennum = 0.3954
            model_list.append(gennum)
        else:
            print("请输入正确的值")

    def select_age(self):
        age = int(input("请填写您的年龄值："))
        age_num = age * 0.1838
        model_list.append(age_num)

    def select_height(self):
        height = int(input("请填写您的身高(cm)："))
        height_num = height * 0.019
        model_list.append(height_num)

    def select_myopia(self):

        parental_myopia = int(input("请选择父母近视情况：【1】都不近视【2】父亲近视【3】母亲近视【4】父母都近视"))
        if parental_myopia == 1:
            parnum = 0
            model_list.append(parnum)
        elif parental_myopia == 2:
            parnum = 0.5972
            model_list.append(parnum)
        elif parental_myopia == 3:
            parnum = 0.5781
            model_list.append(parnum)
        elif parental_myopia == 4:
            parnum = 1.0413
            model_list.append(parnum)
        else:
            print("请输入正确的值")

    def select_class(self):
        class_active = int(input("课间活动在哪里：【1】教学楼【2】户外"))
        if class_active == 1:
            actnum = 0
            model_list.append(actnum)
        elif class_active == 2:
            actnum = -0.3106
            model_list.append(actnum)
        else:
            print("请输入正确的值")

    def select_run(self):
        run_day = int(input("中高强度运动天数：【1】0-3天【2】4-6天【3】7天"))
        if run_day == 1:
            run_data = 0
            model_list.append(run_data)

        elif run_day == 2:
            run_data = -0.0714
            model_list.append(run_data)

        elif run_day == 3:
            run_data = -0.1376
            model_list.append(run_data)

        else:
            print("请输入正确的值")

    def select_read(self):
        read_day = int(input("放学后做作业天数：【1】不到1小时【2】1-2h【3】2-3h【4】大于3h"))
        if read_day == 1:
            read_data = 0
            model_list.append(read_data)

        elif read_day == 2:
            read_data = 0.0293
            model_list.append(read_data)

        elif read_day == 3:
            read_data = 0.1951
            model_list.append(read_data)

        elif read_day == 4:
            read_data = 0.2505
            model_list.append(read_data)

        else:
            print("请输入正确的值")

    def select_cultural(self):
        cultural_week = int(input("文化补习班天数：【1】不到1小时【2】1-2h【3】2-3h【4】大于3h"))
        if cultural_week == 1:
            cul_data = 0
            model_list.append(cul_data)

        elif cultural_week == 2:
            cul_data = 0.0776
            model_list.append(cul_data)

        elif cultural_week == 3:
            cul_data = 0.1759
            model_list.append(cul_data)

        elif cultural_week == 4:
            cul_data = 0.127
            model_list.append(cul_data)

        else:
            print("请输入正确的值")

    def select_posture(self):
        posture = int(input("读写姿势：【1】不正确【2】正确"))
        if posture == 1:
            actnum = 0
            model_list.append(actnum)

        elif posture == 2:
            actnum = -0.2006
            model_list.append(actnum)

        else:
            print("请输入正确的值")

    def select_short(self):

        short_sum = sum(model_list)
        print('您输入的近视数据为：%s' % model_list)
        fz = math.exp(short_sum)
        fm = 1 + fz
        result = fz / fm
        print('你患近视的风险p值为：%s' % result)



if __name__ == '__main__':
    try:
        myopia = MyopiaModel()
        myopia.select_model()
        myopia.select_age()
        myopia.select_height()
        myopia.select_myopia()
        myopia.select_class()
        myopia.select_run()
        myopia.select_read()
        myopia.select_cultural()
        myopia.select_posture()
        myopia.select_short()
    except (ValueError):
        print('请输入正确的值')
