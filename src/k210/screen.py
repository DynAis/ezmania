# Untitled - By: Dynais - 周日 9月 20 2020

import image

def draw_judge_area(src, roi):
    #画出判定区域
    #src: 原图像,image对象
    #roi: 判定区域，元组，格式为(x,y,w,h)
    #dst: 返回图像，是roi内图像，并且经过二值化

    src.to_grayscale()
    dst = src.copy(roi)
    dst.binary([(190,255)])
    src.draw_image(dst,(roi[0],roi[1]))
    src.draw_rectangle(roi, (150,150,150))

    return dst


def draw_judge_cross(src, point1, point2, judge_offset, note_offset):
    #画出表示判定点的十字，一共有两排，下面一排用来判定按键时机
    #上面一排用来辅助下面一排判定Note类型
    #src: 原图像
    #point1, point2: 元组，格式为(x, y)，表示判定线的连线，实际可以取用roi的底部连线
    #judge_offset: 用来调整判定的延迟，数值意味着移动的像素，表现为数值增大时十字会向上方移动
    #note_offset: 用来调整两行十字的间距，数值意味着间距的像素，应使十字间距刚好稍大于单个note

    dis = (int)((point2[0]-point1[0])/5)


    src.draw_cross((point1[0]+dis*1,point1[1]-judge_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*2,point1[1]-judge_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*3,point1[1]-judge_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*4,point1[1]-judge_offset), (150,150,150))


    src.draw_cross((point1[0]+dis*1,point1[1]-judge_offset-note_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*2,point1[1]-judge_offset-note_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*3,point1[1]-judge_offset-note_offset), (150,150,150))
    src.draw_cross((point1[0]+dis*4,point1[1]-judge_offset-note_offset), (150,150,150))
