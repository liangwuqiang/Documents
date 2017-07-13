http://linux.alai.net/viewblog.php?id=67175

# Linux下实现SCSI硬盘热插拔及在线识别


Attached devices:

Host: scsi0 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST3500413AS      Rev: JC49
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi1 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST3500413AS      Rev: JC45
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi2 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: WDC WD20EARS-00M Rev: AB51
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi3 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST31000528AS     Rev: CC38
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi4 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST31000528AS     Rev: CC38
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi5 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST31000528AS     Rev: CC71
  Type:   Direct-Access                    ANSI  SCSI revision: 05

Host: scsi6 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ADATA SP900      Rev: 2   
  Type:   Direct-Access                    ANSI  SCSI revision: 05
  
  
-----------------------------------------------
例如：


  echo "scsi add-single-device 0 0 2 0" > /proc/scsi/scsi
  echo "scsi add-single-device 0 0 2 0" > /proc/scsi/scsi

  echo "scsi remove-single-device 0 0 2 0" > /proc/scsi/scsi
  
  ------------------------------------------------
  
  以root用户运行命令：

echo "scsi add-single-device x y z u" > /proc/scsi/scsi

其中：
x是硬盘所在SCSI控制器号（一般机器就一个SCSI控制器，所以就是0）；
y是硬盘所在SCSI通道的编号（一般单通道的就是0，多通道的要看是哪个通道了）；
z是硬盘的SCSI ID号（可以通过具体插入的硬盘插槽来判断）；
u是硬盘的lun号（默认情况都是0）



如果要移除硬盘，那么可以这样操作：

以root用户运行命令：

echo "scsi remove-single-device x y z u" > /proc/scsi/scsi







