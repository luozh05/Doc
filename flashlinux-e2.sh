#fastboot devices # After fastboot device is detected, run commands below.
#fastboot flash EMPTY lk.img
#fastboot continue  # Press Download key before you hit Enter, and only release it until LK fastboot mode is on. Here LK fastboot mode is entered.

fastboot erase mmc0boot0
fastboot erase mmc0
fastboot erase nor0
fastboot flash mmc0boot0 MBR_EMMC_BOOT0 
fastboot flash nor0 MBR_NOR
fastboot flash mmc0 MBR_EMMC
fastboot flash BL1 lk.img 
fastboot flash TEE1 tz.img
fastboot flash BOOTIMG boot.img 
fastboot flash ROOTFS rootfs.ext4
fastboot flash STATE state.ext4 

fastboot reboot 
