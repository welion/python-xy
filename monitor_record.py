# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:31:54 2016

面向业务导向对告警进行分析的智能统一监控系统

@author: welion
"""

record = {}
#业务层：
##银行卡交易成功率（TRAN_SUC）
##每分钟交易量（TRAN_TPM）
##平均交易时长(TRAN_TIME)
##交易承兑率(TRAN_ACC)
##冲正率(TRAN_REV)
##交易类型(TRAN_TYPE)
tran_rec = {"TRAN_SUC":"40",
            "TRAN_TPM":"21043",
            "TRAN_TIME":"1.2",
            "TRAN_ACC":"32",
            "TRAN_REV":"56",
            "TRAN_TYPE":"ISO-8583",}
#应用层：
##通讯进程个数(APP_CTP)、
##交易处理进程个数（APP_NOF）
##消息队列个数（APP_MQN)
##消息队列拥堵状况(APP_MQS)
##日志刷新频率(APP_LOG)
##应用句柄数(APP_HAND)
app_rec={"APP_CTP":"128",
         "APP_NOF":"16",
         "APP_MQN":"24",
         "APP_MQS":"12",
         "APP_LOG":"16",
         "APP_HAND":"3792",}
#数据库层：
##数据库CPU使用率(DB_CPU)
##数据库CACHE命中率(DB_HIR)
##数据库索引块分裂（DB_IDXCON）
##oracle锁表(DB_LOCK)
##表空间利用率(DB_TAB)
##数据库等待事件(DB_WAIT)
db_rec={"DB_CPU":"63",
        "DB_HIR":"95",
        "DB_IDXCON":"False",
        "DB_LOCK":"5",
        "DB_TAB":"75",
        "DB_WAIT":"10",}
#操作系统层：
##PING状态（OS_PING)
##CPU(OS_CPU)
##Memory(OS_MEM)
##SWAP(OS_SWAP)
##Storage(OS_STOR)
##磁盘响应时间(OS_IO)
os_rec={"OS_PING":"True",
        "OS_CPU":"67",
        "OS_MEM":"64",
        "OS_SWAP":"0",
        "OS_STOR":"63",
        "OS_IO":"0.0010",}
#网络：
##通断性(NET_LINK)
##丢包率(NET_LOSS)
##连接数(NET_LINKNUM)
##带宽使用率(NET_BW)
net_rec={"NET_LINK":"True",
         "NET_LOSS":"0",
         "NET_LINKNUM":"3420",
         "NET_BW":"14",}
#环境：
##火灾状态(PHY_FIRE)
##渗水报警(PHY_WATER)
##电力供应(PHY_POW)
##电压(PHY_VOL)
##机房温度(PHY_TEM)
##机房湿度(PHY_HUM)
phy_rec={"PHY_FIRE":"True",
         "PHY_WATER":"True",
         "PHY_POW":"True",
         "PHY_VOL":"True",
         "PHY_TEM":"23",
         "PHY_HUM":"45",}

record.update(tran_rec)
record.update(app_rec)
record.update(db_rec)
record.update(os_rec)
record.update(net_rec)
record.update(phy_rec)

print record




