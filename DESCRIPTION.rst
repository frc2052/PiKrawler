Raspberry Pi
=======================
Picrawler gait Library for Raspberry Pi


Updata
================
:Time: 2021.7.29
:作者: 凌活龙



- step_list 

    一些步态（如站立、坐下等）的 **字典** ，值是4条腿的触点的（x,y,z）坐标

    ::
   
        step_list = {
            "stand":[
                [50, 50, -80],
                [50, 50, -80],
                [50, 50, -80],
                [50, 50, -80]
            ],
            ....
        }

    在当前步态的基础上，让蜘蛛的某一个脚摆出特定的动作。 

    -leg                0~3，which leg
    -coodinate          动作的触点坐标
    -speed              动作的速度
     
    return : none

- def current_step_leg_value(leg)

    返回当前步态下特定脚的坐标值 # 把这个值放入do single leg是可以运行的。

    -leg               0~3，哪一条腿

    return : arry,坐标值 [x,y,z]

- def current_step_all_leg_value()   

    返回当前步态下特定脚的坐标值

    return : list, [ [x0,y0,z0], [x1,y1,z1], [x2,y2,z2], [x3,y3,z3] ]

- def mix_step(step_name,leg,coodinate=[50,50,-33])

    在某个现有步态中，修改（覆盖）某个脚的坐标值，返回一个新的步态值 

    -step_name      str，现有步态字典中的键名
    -leg            0~3,which leg
    -coodinate      arry,修改值（x,y,z）

    return : list,修改后的四条的坐标列表














