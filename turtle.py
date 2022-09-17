import turtle as tt             #【1】turtle库导入，取[别名]为tt

tt.setup(650, 350 , 200, 200)   #【2】绘制显示的窗体 (width,height,startx,starty)
tt.penup()                      #【3】画笔抬起
tt.fd(-250)                     #【4】向后倒退250个像素
tt.pendown()                    #【5】画笔落下
tt.pensize(25)                  #【6】画笔的宽度   25像素
tt.pencolor("purple")           #【7】画图的颜色
tt.seth(-40)                     #【8】向右转40度

for i in range(4):              #【9】循环4次
    tt.circle(40, 80)           #【10】在海龟的左侧绘制半径为40，80度的圆
    tt.circle(-40, 80)          #【11】在海龟的右侧绘制半径为40，80度的圆

tt.circle(40, 80/2)             #【12】在海龟的左侧绘制半径为40，40度的圆
tt.fd(40)                       #【13】往前走40像素
tt.circle(16, 180)              #【14】在海龟的左侧绘制半径为16，180度的圆
tt.fd(40 * 2/3)                 #【15】往前
tt.done()                       #【16】程序结束后不要立即退出

