#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
	{ 0x637493f3, "__wake_up" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x1ec5db1a, "__register_chrdev" },
	{ 0x92997ed8, "_printk" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x1d37eeed, "ioremap" },
	{ 0x17b8e2f4, "gpio_to_desc" },
	{ 0x5ecd9ee5, "gpiod_to_irq" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0xedc03953, "iounmap" },
	{ 0x7682ba4e, "__copy_overflow" },
	{ 0x51a910c0, "arm_copy_to_user" },
	{ 0xae353d77, "arm_copy_from_user" },
	{ 0x5f754e5a, "memset" },
	{ 0x3ea1b6e4, "__stack_chk_fail" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x78a319e7, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "4CA4CE01EEFA31A03651CE1");
