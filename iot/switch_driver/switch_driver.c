#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/gpio.h>
#include <asm/uaccess.h>
#include <linux/io.h>

#define SWITCH_MAJOR 100
#define SWITCH_NAME "SWITCH_DRIVER"
#define BCM2711_PERI_BASE 0xFE000000
#define GPIO_BASE (BCM2711_PERI_BASE + 0x200000)
#define GPIO_SIZE 256

char switch_usage = 0;
static void *switch_map;
volatile unsigned *switch_gpio;

static int switch_open(struct inode *inode, struct file *file)
{
    if(switch_usage != 0)
        return -EBUSY;

    switch_usage = 1;
    switch_map = ioremap(GPIO_BASE, GPIO_SIZE);

    if (!switch_map)
    {
        printk("error: mapping gpio memory");
        iounmap(switch_map);
        return -EBUSY;
    }

    switch_gpio = (volatile unsigned int *)switch_map;
    *(switch_gpio+1) &= ~(0x7 << (3 * 3));
	*(switch_gpio+1) |= (0x1 << (3 * 3));
    return 0;
}

static int switch_release(struct inode *inode, struct file *file)
{
    switch_usage = 0;
    if(switch_gpio)
        iounmap(switch_gpio);
    return 0;
}

static ssize_t switch_read(struct file *file, char *buf, size_t length, loff_t *ofs)
{
    int value;
    value = (*(switch_gpio + 13) & (0x1 << 13)) ? 1 : 0;

    if(copy_to_user(buf, &value, sizeof(value)))
        return -EFAULT;

    return sizeof(value);
}

static struct file_operations switch_fops =
{
    .open = switch_open,
    .release = switch_release,
    .read = switch_read,
};

static int switch_init(void)
{
    int result;
    result = register_chrdev(100, SWITCH_NAME, &switch_fops);

    if(result < 0) {
        printk(KERN_WARNING "Can't get any major\n");
        return result;
    }
    return 0;
}

static void switch_exit(void)
{
    unregister_chrdev(SWITCH_MAJOR, SWITCH_NAME);
    printk("Switch module removed.\n");
}

module_init(switch_init);
module_exit(switch_exit);
MODULE_LICENSE("GPL");
