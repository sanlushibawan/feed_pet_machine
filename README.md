# 无双吃饭不愁（基于树莓派zero项目）

---

### 功能设计

1. 定时定量投喂
   - 通过**手机**设置投喂时间和投喂的量
   - 通过**电子称**+**伺服电机**精准控制投喂的量
2. 投喂检测食量+固定投喂量
   - （计划功能）<u>记录每次吃饭速率，将数据同步到**小程序**生成食物消失曲线</u>
3. 未吃饭报警
   - 投餐前检测餐盘中的食物变化量，若*χ*天没有发生变化 则发 **邮件** 通知到主人注意

---

### 参考文章

1. [Raspberry pico+HX711 电子秤](https://mc.dfrobot.com.cn/thread-309230-1-1.html)
2. [Adafruit的树莓派教程：使用伺服马达](https://shumeipai.nxez.com/2014/08/10/adafruit-raspberry-faction-tutorial-using-servo-motor.html)
3. [微信小程序通过wifi和蓝牙控制树莓派](https://blog.csdn.net/qq_38639426/article/details/89109161)
4. [在树莓派中使用python发送邮件](https://www.jianshu.com/p/575839f973ad)

---

### 购买材料

1. 树莓派zero * 1 （已有）
2. tf卡数据卡 * 1 （已有）
3. 伺服电机 * 1
4. 电子称 * 1
5. HX711模块 * 1
6. 电烙铁 * 1