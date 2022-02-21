from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys,os,time,threading
from ui_kfq import Ui_MainWindow as MSL2Py
from ui_output import Ui_Output
import SupportLib.RAM as RAM
import SupportLib.download
from download_server_support import Download_Manager as DManager
class Output(QDialog, Ui_Output):
    def __init__(self,server_path):
        super().__init__()
        self.server_path = server_path
        self.setupUi(self)
        self.show()
class ReadingLogs(threading.Thread,Output,QDialog):
    def __init__(self,log_path):
        threading.Thread.__init__(self)
        Output.__init__(self,log_path)
        self.log_path = log_path
	# 覆盖父类的run方法
    def run(self):
        jump = 0
        while True:
            with open(f"{self.log_path}server.log") as f:
                    if jump > 0:
                        for i in range(jump):
                            f.next()
                        try:
                            for whe in range(1, 50):
                                new_logs = f.readline()
                        except:
                            jump = whe
                    else:
                        for whe in range(1, 50):
                            new_logs = f.readline()
            self.show_logs.setText(new_logs)
class MSL2(QMainWindow,MSL2Py,ReadingLogs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setWindowIcon(QIcon("Resource"+os.sep+"我的世界开服器.ico"))
        self.setWindowTitle("我的世界开服器")
        self.setFixedSize(811,384) #设置窗体大小为811*384
        self.using_java = 0 #0为17，1为16，2为8
        self.want_to_download = 0 #同上
        self.java_path=["/usr/lib/jvm/java-17-openjdk-amd64","/usr/lib/jvm/java-16-openjdk-amd64","/usr/lib/jvm/java-8-openjdk-amd64"]
        self.server_path = "" #服务端的路径
        self.server_name = "server.jar" #服务端的名字，需要单独设置
        self.min_mem_G = 1 #最小内存(G)
        self.max_mem_G = RAM.mem()[1] #最大内存(G)
        self.dis_log4j2 = True #是否禁用log4j2
        self.online_mode = True #是否开启正版验证
        self.max_players = 20 #最大玩家数量
        self.serv_port = 19132 #服务器端口
        self.pvp = True #开启PVP
        self.command_block = True #开启命令方块
        self.motd_message = "Welcome!" #服务器选择界面提示
        self.select_card = 0 #打开的选项卡，0为无，1为日志，2为映射，3为关于
        self.server_status = False #服务器状态，False为关闭，True为开启
        self.pbtn_output.setIcon(QIcon("Resource"+os.sep+"Book.gif")) #设置输出摁钮的图案为书
        self.pbtn_frp.setIcon(QIcon("Resource"+os.sep+"Furnace.png")) #设置内网穿透摁钮的图案为熔炉
        self.pbtn_about.setIcon(QIcon("Resource"+os.sep+"Quill.png")) #设置关于摁钮的图案为书和笔
        self.pbtn_ok_adv_set.clicked.connect(self.set_adv)
        self.pbtn_how_to_choice.clicked.connect(self.print_how_to_choice)
        self.pbtn_dis_log4j2.clicked.connect(self.process_log4j2)
        self.pbtn_download.clicked.connect(self.download_java)
        self.pbtn_start_server.clicked.connect(self.start_server)
        self.pbtn_about.clicked.connect(self.about)
        self.pbtn_output.clicked.connect(self.open_logs)
        self.pbtn_show_java_path.clicked.connect(self.show_java_path)
        self.pbtn_select_path.clicked.connect(self.select_server_path)   
        self.pbtn_download_server.clicked.connect(self.download_server)
        if not os.path.isfile("frp.conf"): #判断是否已经配置过SakuraFRP
            self.pbtn_frp.clicked.connect(self.frp_guide("first_use"))
        else:
            self.pbtn_frp.clicked.connect(self.frp_guide("after"))
    def set_adv(self): #读写server.pro...文件修改设置
        self.min_mem_G = self.min_ram.value() #获取最小内存(G)
        self.max_mem_G = self.max_ram.value() #获取最大内存(G)
        self.max_players = int(self.max_player.text()) #获取最大玩家数量
        self.serv_port = int(self.server_port.text()) #获取服务器端口
        self.pvp = bool(self.cbox_pvp) #获取是否启用pvp
        self.command_block = bool(self.cbox_command_block) #获取是否启用命令方块
        self.motd_message = self.motd.text()
        with open(f"{self.server_path}"+os.sep+"server.properties") as f:
            server_lines = f.readlines()
        for i in range(server_lines):
            if "max-players=" in server_lines[i]:
                server_lines[i] = "max-players={}".format(self.max_players)
            if "server-port=" in server_lines[i]:
                server_lines[i] = "server-port={}".format(self.serv_port)
            if "pvp=" in server_lines[i]:
                server_lines[i] = "pvp={}".format(self.pvp)
            if "enable-command-block=" in server_lines[i]:
                server_lines[i] = "enable-command-block={}".format(self.command_block)
        with open(f"{self.server_path}"+os.sep+"server.properties","w"):
            f.write(server_lines)
        self.min_ram.setMinimum(1) #定义最小内存为1G
        self.min_ram.setMaximum(self.max_mem_G) #设置最大内存为当前可用内存
        self.max_ram.setMinimum(self.min_mem_G) #设置最小内存
    def process_log4j2(self):
        self.dis_log4j2 = not(self.dis_log4j2)#反相是否启用log4j2的设置
        if self.dis_log4j2 == True:
            self.pbtn_dis_log4j2.setText("启用log4j2 (不推荐)")
        else:
            self.pbtn_dis_log4j2.setText("通过启动参数禁用Log4j2")
    def print_how_to_choice(self):
        QMessageBox.information(self,"如何选择Java版本","\
        1.18+ --> Java17\n\
        1.14 - 1.17 --> Java8 - Java16\n\
        1.8 - 1.13 --> Java8\n\
        1.7- --> Java7")
    def download_java(self):
        want_to = self.cbox_want_to_download.currentText()
        os.system("sudo apt update && sudo apt upgrade -y") #更新pip源
        if "7" in want_to:
            os.system("sudo apt install openjdk-7-jre -y") #下载Java7
        if "8" in want_to:
            os.system("sudo apt install openjdk-8-jdk -y") #下载Java8
        if "16" in want_to:
            os.system("sudo apt install openjdk-16-jdk -y") #下载Java16
        if "17" in want_to:
            os.system("sudo apt install openjdk-17-jdk -y") #下载Java17
    def start_server(self):
        if self.dis_log4j2 == True:
            os.system("{}java -Xms {}G -Xmx {}G -jar {} -Dlog4j2.formatMsgNoLookups=true".format(self.java_path,self.min_mem_G,self.max_mem_G,self.server_name))
        else:
            os.system("{}java -Xms {}G -Xmx {}G -jar {}".format(self.java_path,self.min_mem_G,self.max_mem_G,self.server_name))
    def open_logs(self):
        rdl = ReadingLogs(log_path=self.server_path)
        rdl.start()
    def about(self):
        QMessageBox.information(self,"软件信息","我的世界开服器Python版1.0(对应Waheal版本2.0)\n由Mojavium制作")
    def show_java_path(self):
        if self.cbox_using_java.currentText() == "Java17":
            QMessageBox.information(self,"Java17路径",str(self.java_path[0]))
        if self.cbox_using_java.currentText() == "Java16":
            QMessageBox.information(self,"Java16路径",str(self.java_path[1]))
        if self.cbox_using_java.currentText() == "Java8":
            QMessageBox.information(self,"Java8路径",str(self.java_path[2]))
    def frp_guide(self,now):
        os.system("sudo python "+"SupportLib"+os.sep+"frpsupport.py"+f"{now}")
    def select_server_path(self):
        self.server_path = QFileDialog.getExistingDirectory(self,"MSL2:选择服务端所在文件夹")
        self.server_name = QFileDialog.getOpenFileName(self,"MSL2:选择服务端文件",filter=("Minecraft Java Edi Server File (*.jar)"))
    def download_server(self):
        download = DManager()
        download.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    msl = MSL2()
    sys.exit(app.exec())