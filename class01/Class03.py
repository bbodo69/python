class TV:
    # 클래스 변수
    power = False
    color = 'white'
    channel = 1

    def on_off(self):

        # power = 지역변수
        # self.power = 인스턴스 변수

        self.power = not self.power

    def channelUp(self):
        self.channel +=1

    def channelDown(self):
        self.channel -=1

    def remote(self, num):
        self.channel = num

    def showInfo(self):
        print("power : ", self.power)
        print("channel : ", self.channel)
        print("color : ", self.color)


my = TV()
my.color = 'green'
my.remote(123)
my.showInfo()

mom = TV()
mom.showInfo()