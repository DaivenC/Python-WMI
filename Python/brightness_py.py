#
# A test script to control brightness on Windows for GuestView Guide
#
# Before running, install python3 and module pypiwin32 and wmi first
#  py -m pip install pypiwin32
#  py -m pip install wmi
#
import wmi

class GuestViewControl:
    def __ini__(self):
        _brightness = 50
        self.set_display_brightness(_brightness)

    def set_display_brightness(self, brightness: int) -> None: # 0~100
        if brightness >=0 and brightness <=100:
            self._brightness = brightness
            wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

    def get_display_brightness(self) -> int:
        return self._brightness


def _testBrightness():
    import time
    hw = GuestViewControl()
    hw.set_display_brightness(0)
    print("Brightness: 0", end='\r')
    time.sleep(1)

    # start testing
    for i in range(101):
        hw.set_display_brightness(i)
        print("Brightness: ", hw.get_display_brightness(), end='\r')

if __name__ == '__main__':
    _testBrightness()