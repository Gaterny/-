### os模块

**```os.name```**——判断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix'

**``` os.getcwd()```**——得到当前工作的目录。

**```os.listdir(path)```**——指定所有目录下所有的文件和目录名。以列表的形式全部列举出来，其中没有区分目录和文件。

**```os.remove(path)```**——删除指定文件

**```os.rmdir(path)```**——删除指定目录

**```os.mkdir(path, mode)```**——创建目录

　　注意：这样只能建立一层，要想递归建立可用：**```os.makedirs()```**

**```os.path.isfile(path)```**——判断指定对象是否为文件。是返回True,否则False

**```os.path.isdir(path)```**——判断指定对象是否为目录。是True,否则False。      

**```os.path.exists(path)```**——检验指定的对象是否存在。是True,否则False.

**``` os.path.split(path)```**——返回路径的目录和文件名。

**```os.system(command)```**——执行shell命令。

**注意**：此处运行shell命令时，如果要调用python之前的变量，可以用如下方式：

```
var=123
os.environ['var']=str(var) //注意此处[]内得是 “字符串”
os.system('echo $var')
```

**```os.chdir(path)```**——改变目录到指定目录

**```os.path.getsize(filename)```**——获得文件的大小，如果为目录，返回0

**``` os.path.abspath(path)```**——获得绝对路径。

**```os.path.join(path, name)```**——连接目录和文件名。

**```os.path.basename(path)```**——返回文件名

**``` os.path.dirname(path)```**——返回文件路径
