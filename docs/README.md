# 使用前
- 下载运行环境
	- Python
		- 本版本开服器使用Python编写，由于使用库的限制，请务必更新至Python3.7以上
			- 现在请您先输入python -ver查看现存Python版本，3.6以下都不可以运行
			- 如果您是Python2.x：请在终端输入sudo apt-get remove --auto-remove python2.x  来移除Python(把x换成后面的版本号)然后按照Python3.x-Python3.7一下处理
			- 如果您是Python3.x：
				- Python3.7以上可以直接跳到下载PySide6一节
				- Python3.7以下可以查看[教程](https://cloud.tencent.com/developer/article/1565853)或自己折腾
		
	- 下载PySide6和其他运行环境
	
 		- 如果您已经配置好了Python3.7环境，请在终端执行sudo pip3 install PySide6来下载PySide6运行环境
	      
			- 其他环境安装：将以下库名替换到上面一条命令PySide6的位置
		  
				- tqdm
		  
				- requests
		  
				- multitasking
		  
				- signal
		  
				- retry
		  
				- urllib
		  
				- psutil


环境配置至此完成



# 基本使用方法
- 开启服务器
	- 在主界面点击“开启服务器”即可
	- 注意事项
		- 必须事先选择服务端路径和服务端（服务端没有可以点击服务端路径和“...”选择路径中间的下载摁钮下载）
		- 必须配置好对应版本的Java,不知道如何配置可以点击主页下方的“如何选择”查看帮助
- 配置服务器
	- 主页提供了常用的服务器设置，如是否开启PVP，最大在线人数等
	- 进阶设置可以在服务端路径下的server.properties修改，具体每个选项的释义可以在主界面-帮助 查看
	- 服务端目录结构，开服前准备都可以在主界面-帮助查看

# 进阶设置和疑难解答

- 更改Java的安装路径：见主程序第23行

- 你的系统用不了apt/apt库里没有Java16，17，只有8和11：请自行下载deb包安装（一般情况下带GUI的系统可以直接双击安装），然后在上面的“更改Java路径”解决办法手动指定Java安装路径
	- [Java17](https://www.oracle.com/java/technologies/downloads/)
	
	- [Java16](https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html)
	
	- [Java8](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)
  
  - [命令行安装教程](https://blog.csdn.net/oMcLin/article/details/108725325)
  
  - 仓库相关
	      - 服务器相关问题请自行Bing，不是MSL2的问题不要在仓库提交issues（除非你有好的建议）
	      - 参与讨论可以提交issues
	      - 改好了请直接提交PR，详细描述解决的是什么问题，咋解决的
	  
	  ### 使用自定义域名
		
		 您得先有一个域名 
		然后参照以下教程：
		- [阿里云](https://doc.natfrp.com/#/app/mc?id=srv-aliyun)
		
		- [腾讯云](https://doc.natfrp.com/#/app/mc?id=srv-tencent)
		
		- [CloudFlare](https://doc.natfrp.com/#/app/mc?id=srv-cloudflare)
		
		### 常用指令
		
		 -  /ban <玩家名/玩家IP地址>  封禁玩家名/玩家IP地址
		
     -  /tick <玩家名/玩家IP地址>  临时踢出玩家名/玩家IP地址
    ### 部分常用配置翻译
     server.properties
        - [int]代表一个整数
            - [str]代表一串字符
            - [True/False]代表您只能选择True(是)或者Flase(否)作为值
    
        -  spawn-protection	通过将该值进行 2x+1 的运算来决定出生点的保护半径，设置为0将只保护出生点下方那一个方块。[int]
        
        -  max-tick-time 	设置每个tick花费的最大毫秒数，超时会报错”Can't keep up!“[int]
        
        -  query.port 	服务器的端口号[int]
        
        -  generator-settings 	用于自定义超平坦世界的生成[str]
        
        -  sync-chunk-writes 	为true时区块文件以同步模式写入(跟本地一样加载) [True/False]
        
        -  force-gamemode 	强制玩家加入时为默认游戏模式[True/False]
        
        -  allow-nether 	是否允许下界[True/False]
        
        -  enforce-whitelist 	在服务器上强制使用白名单[True/False]
        
        -  gamemode 	默认游戏模式 [0生存 1创造 2冒险 3旁观]
        
        -  player-idle-timeout 	允许的挂机时间，单位为分钟，超过后自动踢出[int]
        
        -  difficulty 	世界难度  [0和平 1简单 2普通 3困难]
        
        -  spawn-monsters 	生成攻击型生物（怪物）[True/False]
        
        -  op-permission-level 	OP权限等级[int]
        
        -  pvp 	是否允许玩家互相攻击[True/False]
        
        -  entity-broadcast-range-percentage 	实体渲染范围百分比[int]
        
        -  level-type 	地图的生成类型[str]
        
        -  hardcore 	极限模式（死后自动封禁）[True/False]
        
        -  enable-command-block 	启用命令方块[True/False]
        
        -  max-players	服务器最大玩家数限制[int]
        
        -  network-compression-threshold 	网络压缩阈值[int]
        -  -1 代表禁用压缩
        -  0 代表全部压缩
        - 数字越大越节省带宽，但同时也会加重CPU负担
        
        -  max-world-size 	最大世界大小[int]
        
        -  function-permission-level 	设定函数的默认权限等级[int]
        
        -  server-port 	服务器端口[int]
        
        -  server-ip 	服务器ip，若不绑定请留空[int]
        
        -  spawn-npcs 	是否生成村民和其他NPC[True/False]
        
        -  allow-flight 	是否允许玩家飞行[True/False]
        
        -  level-name 	地图名称，不要使用中文[str]
        
        -  view-distance 	服务器发送给客户端的数据量，决定玩家能设置的视野[int]
        
        -  resource-pack 	统一资源标识符 (URI) 指向一个资源包。玩家可选择是否使用[str]
        
        -  spawn-animals	是否生成动物[True/False]
        
        -  white-list 	是否开启白名单[True/False]
        
        -  generate-structures 	生成世界时生成结构（如村庄）禁止后地牢和地下要塞仍然生成[True/False]
        
        -  online-mode 	Minecraft在线（正版）验证[True/False]
        
        -  max-build-height 	玩家在服务器放置方块的最高高度[True/False]
        
        -  level-seed 	地图种子[int/str]
        
        -  prevent-proxy-connections 	是否允许玩家使用网络代理进入服务器[True/False]
        
        -  use-native-transport 	是否使用针对Linux平台的数据包收发优化 [ 仅Linux ][True/False]
        
		     -  motd 	服务器信息展示 （MOTD）[str]
    
    - 更多详见[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/Server.properties?variant=zh)
    

