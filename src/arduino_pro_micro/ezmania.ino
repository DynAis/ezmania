#include <Keyboard.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200);
  Keyboard.begin();
  //延时启动10秒
  delay(10000);
}

void loop() {
  // put your main code here, to run repeatedly:
  char check = 0;
  int i = 0;
  if (Serial1.available() > 0) {
    // read the incoming byte:
      check = Serial1.read();

      //起始符号确认
      if(check == 'B'){
        Serial.println("Start to check:");
        char keys[4];
        for(i=0; i<4; i++){
          while(Serial1.available() == 0);  //等待
          check = Serial1.read();
          keys[i] = check;
        }

        //结束符号验证
        while(Serial1.available() == 0);  //等待
        check = Serial1.read();
        if(check == 'E'){
          Serial.println("Start");
          //键盘判断d
          if(keys[0]=='1'){
            Keyboard.press('d');
          }
          else if(keys[0]=='2'){
            Keyboard.press('d');
          }
          else{
            Keyboard.release('d');
          }
          //键盘判断f
          if(keys[1]=='1'){
            Keyboard.press('f');
          }
          else if(keys[1]=='2'){
            Keyboard.press('f');
          }
          else{
            Keyboard.release('f');
          }
          //键盘判断k
          if(keys[2]=='1'){
            Keyboard.press('k');
          }
          else if(keys[2]=='2'){
            Keyboard.press('k');
          }
          else{
            Keyboard.release('k');
          }
          //键盘判断l
          if(keys[3]=='1'){
            Keyboard.press('l');
          }
          else if(keys[3]=='2'){
            Keyboard.press('l');
          }
          else{
            Keyboard.release('l');
          }
          
          for(i=0; i<4; i++){
            Serial.print(keys[i]);
          }
          Serial.print('\n');
        }
        else{
        Serial.println("Failed");
        }
      }
  }
}
