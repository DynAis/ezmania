# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd
from fpioa_manager import fm
from machine import UART
from board import board_info
import screen, note

def init():
    #整体初始化函数
    lcd.init()
    sensor.reset(freq=28000000,set_regs=True,dual_buff=True)# Reset and initialize the sensor. It will
    sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
    sensor.skip_frames(time = 2000)     # Wait for settings take effect.
    sensor.set_vflip(True)
    sensor.run(1)
    fm.register(board_info.PIN15, fm.fpioa.UART1_TX, force=True)
    fm.register(board_info.PIN17, fm.fpioa.UART1_RX, force=True)


#初始化
init()
clock = time.clock()                # Create a clock object to track the FPS.
uart_A = UART(UART.UART1, 115200,8,0,1, timeout=1000, read_buf_len=4096)

#参数设定
roi = (60,110,200,120)
judge_offset = 20
note_offset = 20

#循环
while(True):
    clock.tick()                    # Update the FPS clock.

    img = sensor.snapshot()         # Take a picture and return the image.
    img_prc = screen.draw_judge_area(img, roi)
    screen.draw_judge_cross(img, (roi[0],roi[1]+roi[3]), (roi[0]+roi[2],roi[1]+roi[3]), judge_offset, note_offset)

    keys_state = note.state_detect(img, (roi[0],roi[1]+roi[3]), (roi[0]+roi[2],roi[1]+roi[3]), judge_offset, note_offset)

    lcd.display(img)
    lcd.draw_string(5, 5, str(clock.fps()), lcd.GREEN)
    write_str = "B"+str(keys_state[0])+str(keys_state[1])+str(keys_state[2])+str(keys_state[3])+"E"
    lcd.draw_string(130, 5, write_str, lcd.GREEN)
    uart_A.write(write_str)
    print(write_str)
