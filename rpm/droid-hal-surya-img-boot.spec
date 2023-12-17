%define device sagit

%define mkbootimg_cmd mkbootimg --cmdline 'androidboot.console=ttyMSM0 androidboot.hardware=qcom user_debug=31 msm_rtb.filter=0x37 ehci-hcd.park=3 service_locator.enable=1 swiotlb=2048 audit=0 selinux=1 androidboot.selinux=permissive systemd.legacy_systemd_cgroup_controller=yes' --kernel %{kernel} --ramdisk %{initrd} --base 0x00000000 --pagesize 4096 --kernel_offset 0x01000000 --ramdisk_offset 0x01000000 --board '' --output

%define root_part_label userdata

%define display_brightness_path /sys/class/leds/lcd-backlight/max_brightness
%define display_brightness 255

Provides: droid-hal-surya-devel
Obsoletes: droid-hal-surya-devel

%include initrd/droid-hal-device-img-boot.inc

