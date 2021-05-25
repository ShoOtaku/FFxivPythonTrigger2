FFxivPythonTrigger
===

简介
--
> * FFxivPythonTrigger 是一个以 python 编写，提供基于事件回调触发其他事件的触发器框架
> * 你可以选择用任何你熟悉的语言编写插件 —— 只要最后可以对接上 python 的接口
> * 更多请参阅[开发指南](FFxivPythonTrigger)

注意事项
---
> * 使用本工具有导致账号遭封禁的风险
> * 随缘支持随缘更新
> * 出问题请提供相关log（默认位置为根目录`InjectErr.log`或是`AppData/Core/log_xxxxxxx.txt`）
> * 仅处理最新版本的技术问题（出问题请先尝试更新）

食用方式
---
> * 需求环境：python 3.9.0+ x64 windows 版本
> * 安装py环境，官网：[https://www.python.org/](https://www.python.org/)
> * 安装程序依赖 `pip install -r requirements.txt` _** 注入器自带依赖检测、安装，无需特意手动安装依赖_
> * 运行injecter.py注入游戏
> * 游戏内操作相关请参阅：[Command插件](plugins/Command)
> * 注意：版本初首次需要纯净注入，后续无需
> * 强烈推荐关闭游戏前输入`/e @fpt close`以退出本插件

插件一览
---
> 核心功能/依赖：
> 
> 名字 | 介绍 
> --- |:---:
> [SocketLogger](plugins/SocketLogger)| 作为注入器和程序内核通讯的桥梁，用于传递程序日志
> [HttpApi](plugins/HttpApi) | 提供一个 http api 供其他程序调用本程序功能
> [ChatLog](plugins/ChatLog)| 读取聊天框信息，产生 chatlog 事件（todo:产生聊天框信息）
> [XivMemory](plugins/XivMemory)| 提供对于 FFXIV 相关内存操作的接口
> [XivMagic](plugins/XivMagic)| 提供对于 FFXIV 相关函数调用的接口
> [XivNetwork](plugins/XivNetwork)| 产生网络相关事件
> [CombatMonitor](plugins/CombatMonitor)| 提供战斗分析功能
> [Command](plugins/Command)| 处理游戏内指令，并提供基础内核操作指令
> ---
> 功能插件：
> 
> 名字 | 介绍 
> --- |:---:
> [MoPlus](plugins/MoPlus)| 鼠标功能增强（未完成）
> [ActorQuery](plugins/ActorQuery)| actor 查询
> [XivCraft](plugins/XivCraft)| 生产规划
> [ACTLogLines](plugins/ACTLogLines)| 对接ACT获取 logline 并且产生相关事件（未完成）
> [SendKeys](plugins/SendKeys)| 提供对本游戏传递按键的接口
> [Markings](plugins/Markings)| 提供游戏标点的接口

常见问题
---
> 如何启动默认加载插件：
>* 打开[Entrance.py](Entrance.py)，解除该插件的注译

> 有关中文用户名等：
>* 避免在python路径及fpt路径出现中文
>* 中文用户名默认安装会直接闪退，请自行解决 
>* 非中文用户名也闪退请调整环境变量

>遇到`WinApi err code:5/6/299/etc.`
> * ~~注入器调用api问题，目前未找到妥当解决方法，未来或重构注入器~~
> * 请尝试安装较低版本的pywin32，比如说 `pywin32==228`
 
>如何多开注入：
> * 注入器支援 -p 参数指定pid e.g.`python Injecter.py -p 12345`
> * 目前关于多开还有一些端口问题需要自行处理

>如何回报问题：
> * 提issue
> * Q群1046750894
> 
想到继续补充
