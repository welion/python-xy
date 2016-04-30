# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:31:54 2016

@author: welion
"""

record = {}
#业务层：
##银行卡交易成功率（TRAN_SUC)、
##交易笔数（TRAN_NUM)、
##交易时长(TRAN_TIME)、
##交易承兑率(TRAN_ACC)、
##冲正率(TRAN_REV)、
##交易类型(TRAN_TYPE)、
tran_rec = {"TRAN_SUC":"",
            "TRAN_NUM":"",
            "TRAN_TIME":"",
            "TRAN_ACC":"",
            "TRAN_REV":"",
            "TRAN_TYPE":"",}



#应用层：
##进程个数(APP_PRC)、
##消息队列个数（APP_MQN)
##消息队列拥堵状况(APP_MQS)、
##日志刷新频率(APP_LOG)、
app_rec={"APP_PRC":"",
         "APP_MQN":"",
         "APP_MQS":"",
         "APP_LOG":"",}
#数据库层：
##oracle锁表(DB_LOCK)、
##表空间利用率(DB_TAB)、
##数据库等待事件(DB_WAIT)、
db_rec={"DB_LOCK":"",
        "DB_TAB":"",
        "DB_WAIT":"",}
#操作系统层：
##PING状态（OS_PING)
##CPU(OS_CPU)、
##Memory(OS_MEM)、
##SWAP(OS_SWAP)、
##Storage(OS_STOR)、
##磁盘响应时间(OS_IO)、
os_rec={"OS_OING":"",
        "OS_CPU":"",
        "OS_MEM":"",
        "OS_SWAP":"",
        "OS_STOR":"",
        "OS_IO":"",}
#网络：
##通断性(NET_LINK)、
##丢包率(NET_LOSS)、
##连接数(NET_LINKNUM)、
##带宽使用率(NET_BW)、
net_rec={"NET_LINK":"",
         "NET_LOSS":"",
         "NET_LINKNUM":"",
         "NET_BW":"",}
#环境：
##火灾状态(PHY_FIRE)、
##渗水报警(PHY_WATER)、
##电力供应(PHY_POW)、
##电压(PHY_VOL)、
##机房温度(PHY_TEM)、
##机房湿度(PHY_HUM)、
phy_rec={"PHY_FIRE":"",
         "PHY_WATER":"",
         "PHY_POW":"",
         "PHY_VOL":"",
         "PHY_TEM":"",
         "PHY_NUM":"",}

record.update(tran_rec)
record.update(app_rec)
record.update(db_rec)
record.update(os_rec)
record.update(net_rec)
record.update(phy_rec)


print record


