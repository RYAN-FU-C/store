from appium  import webdriver
import time
# appium服务的地址
from appium.webdriver.common.touch_action import TouchAction

server = r"http://localhost:4723/wd/hub"

# 给5大参数
desider = {
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.ss.android.ugc.aweme",
    "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity",
    "unicodeKeyborad":True
}

driver = webdriver.Remote(server, desider)

time.sleep(15)
el1 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/bfd")
el1.click()
time.sleep(10)
TouchAction(driver).press(x=374, y=942).move_to(x=386, y=334).release().perform()

time.sleep(2)
TouchAction(driver).tap(x=647, y=1239).perform()
time.sleep(2)
# TouchAction(driver).press(x=110, y=502).move_to(x=65, y=506).release().perform()
TouchAction(driver).tap(x=96, y=502).perform()
time.sleep(2)
el2 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/gsk")
el2.send_keys("13832228051")
time.sleep(2)
el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/gpp")
el3.send_keys("fuzhenyu1998qq")
time.sleep(2)
TouchAction(driver).tap(x=58, y=407).perform()
time.sleep(2)
# el4 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/ggo")
# el4.click()
driver.tap([(355, 508)])
# TouchAction(driver).tap(x=355, y=508).perform()
time.sleep(6)
el5 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/iq5")
el5.click()
i = 0
while i < 10:
    time.sleep(8)
    driver.swipe(374, 942, 386, 334, duration=500)
    i = i + 1




