
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
from selenium.webdriver.common.by import By
from selenium.webdriver.commom.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

```
