# Untitled - By: Dynais - 周日 9月 20 2020

import sensor, image, time

def state_detect(src, point1, point2, judge_offset, note_offset):
    #检测Note状态，从而判断发送什么按键
    #src: 原图像
    #point1, point2: 元组，格式为(x, y)，表示判定线的连线，实际可以取用roi的底部连线
    #judge_offset: 用来调整判定的延迟，数值意味着移动的像素，表现为数值增大时十字会向上方移动
    #note_offset: 用来调整两行十字的间距，数值意味着间距的像素，应使十字间距刚好稍大于单个note

    dis = (int)((point2[0]-point1[0])/5)

    pixel_state_1_d = src.get_pixel((point1[0]+dis*1,point1[1]-judge_offset))
    pixel_state_2_d = src.get_pixel((point1[0]+dis*2,point1[1]-judge_offset))
    pixel_state_3_d = src.get_pixel((point1[0]+dis*3,point1[1]-judge_offset))
    pixel_state_4_d = src.get_pixel((point1[0]+dis*4,point1[1]-judge_offset))

    pixel_state_1_u = src.get_pixel((point1[0]+dis*1,point1[1]-judge_offset))
    pixel_state_2_u = src.get_pixel((point1[0]+dis*2,point1[1]-judge_offset-note_offset))
    pixel_state_3_u = src.get_pixel((point1[0]+dis*3,point1[1]-judge_offset-note_offset))
    pixel_state_4_u = src.get_pixel((point1[0]+dis*4,point1[1]-judge_offset-note_offset))

    #key1状态判断
    if(src.get_pixel((point1[0]+dis*1-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*1-1,point1[1]-judge_offset-note_offset-1))==0):
        key_state_1 = 1
    elif(src.get_pixel((point1[0]+dis*1-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*1-1,point1[1]-judge_offset-note_offset-1))==255):
        key_state_1 = 2
    else:
        key_state_1 = 0

    #key2状态判断
    if(src.get_pixel((point1[0]+dis*2-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*2-1,point1[1]-judge_offset-note_offset-1))==0):
        key_state_2 = 1
    elif(src.get_pixel((point1[0]+dis*2-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*2-1,point1[1]-judge_offset-note_offset-1))==255):
        key_state_2 = 2
    else:
        key_state_2 = 0

    #key3状态判断
    if(src.get_pixel((point1[0]+dis*3-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*3-1,point1[1]-judge_offset-note_offset-1))==0):
        key_state_3 = 1
    elif(src.get_pixel((point1[0]+dis*3-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*3-1,point1[1]-judge_offset-note_offset-1))==255):
        key_state_3 = 2
    else:
        key_state_3 = 0

    #key4状态判断
    if(src.get_pixel((point1[0]+dis*4-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*4-1,point1[1]-judge_offset-note_offset-1))==0):
        key_state_4 = 1
    elif(src.get_pixel((point1[0]+dis*4-1,point1[1]-judge_offset-1))==255 and src.get_pixel((point1[0]+dis*4-1,point1[1]-judge_offset-note_offset-1))==255):
        key_state_4 = 2
    else:
        key_state_4 = 0

    return(key_state_1,key_state_2,key_state_3,key_state_4)
