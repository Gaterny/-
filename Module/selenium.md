
# selenium  
#### 自动化测试工具，支持多种浏览器，主要用来解决Javascript渲染的问题

```
# 声明浏览器对象
from selenium import webdriver

browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
```
```
# 访问页面
from selenium import webdriver  

browser = webdriver.Chrome()
browser.get('https://www.python.org')
print(browser.page_source)    # 打印网页源代码
browser.close()
```
```
# 查找元素
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')


```
```
# 元素交互操作,获取元素，调用方法
from selenium import webdriver 
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')  #查找q元素，实际为输入框
input.send_keys('iPhone')      #输入框输入iPhone
time.sleep(1)
input.clear()   # 清空输入框
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')   # 查找搜索按钮
button.click()
browser.close()
```
```
# 交互动作，将动作附加到动作链中串行执行
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
button = browser.find_element_by_class_name('tbh-tipoff')   # 找到网上有害信息举报专区
actions = ActionChains(browser)  # 声明动作链对象
actions.click(button)
actions.perform()  #执行动作
# 更多：https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
```
```
# 执行JavaScript
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 执行下拉动作，到网页最底部
browser.execute_script('alert("To Bottom")')    # 弹出提醒，已到底
```
```
# 获取元素信息
1.获取属性、文本值
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.jd.com')
logo = browser.find_element_by_class_name('logo') # 查找 logo对象
print(logo.get_attribute('class'))   # 获取logo属性
print(logo.text)  # 获取logo的文本

2.其他方法
object.id() #获取id值
object.location() # 获取在浏览器中位置
object.tag_name() #获取标签名
object.size() #获取尺寸大小

```
```
# Frame

```
```
隐式等待：如果webdriver没有在DOM中找到元素，将继续等待，超过设定的等待时间后找不到元素时，返回异常，隐式等待默认时间为0
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.facebook.com')
input = browser.find_element_by_class_name('img')
print(input)

显式等待：指定等待条件，指定等待时间，在等待时间内满足等待条件，正常返回；否则返回异常
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser,10)   # 声明对象
input = wait.until(EC.presence_of_element_located((By.ID,'q')))  # 传入等待条件
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)
# 更多：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
```
```
# 前进后退
import time
from selenium import webdriver

url1 = 'http://www.baidu.com'
url2 = 'https://www.zhihu.com'
url3 = 'https://www.taobao.com'
browser = webdriver.Chrome()
browser.get(url1)
browser.get(url2)
browser.get(url3)
browser.back()
time.sleep(2)
browser.forward()
browser.close()
```
```
# Cookies
from selenium import webdriver

browser = webdriver.Chrome()
browser.get_cookies() # 获取cookies
browser.add_cookies({'name':'name','domain':'www.zhihu.com'}) # 添加cookies,
browser.delete_all_cookies() # 删除所有cookies
```
```
# 选项卡管理(模拟js)
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.execute_script(window.open())  # 新打开一个选项卡
browser.switch_to_window(browser.window_handles[1])  #切换到新打开的选项卡
browser.get('https://www.taobao.com') # 在新选项卡打开淘宝
```
```
# 异常处理
from selenium import webdriver
from selenium.common.exception import TimeoutException,NoSuchElementException...
#更多：http://selenium-python.readthedocs.io/api.html#selenium.common.exceptions
```
