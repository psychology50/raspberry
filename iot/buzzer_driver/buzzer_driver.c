#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/gpio.h>
#include <linux/delay.h>
#include <asm/uaccess.h>
#include <linux/io.h>

#define BUZZER_MAJOR 240
#define BUZZER_NAME "BUZZER_DRIVER"
#define BCM2711_PERI_BASE 0xFE000000
#define GPIO_BASE (BCM2711_PERI_BASE + 0x200000)
#define GPIO_SIZE 256
#define GPIO_NUMBER 23

char buzzer_usage = 0;
static void *buzzer_map;
volatile unsigned *buzzer;

static int buzzer_open(struct inode *inode, struct file *file)
{
    if(buzzer_usage != 0)
        return -EBUSY;

    buzzer_usage = 1;
    buzzer_map = ioremap(GPIO_BASE, GPIO_SIZE);

    if (!buzzer_map)
    {
        printk("error: mapping gpio memory");
        iounmap(buzzer_map);
        return -EBUSY;
    }

    buzzer = (volatile unsigned int *)buzzer_map;
    *(buzzer + 2) &= ~(0x7 << (3 * 3));
    *(buzzer + 2) |= (0x1 << (3 * 3));
    return 0;
}

static int buzzer_release(struct inode *inode, struct file *file)
{
    buzzer_usage = 0;
    if(buzzer)
        iounmap(buzzer);
    return 0;
}

static int buzzer_write(struct file *file, const char *buf, size_t length, loff_t *ofs)
{
    char tmp_buf;

    if(copy_from_user(&tmp_buf, buf, length))
        return -EFAULT;

    if (tmp_buf == 0)
        *(buzzer + 10) = (0x1 << GPIO_NUMBER);
    else
        *(buzzer + 7) = (0x1 << GPIO_NUMBER);
    return length;
}

static struct file_operations buzzer_fops =
{
    .open = buzzer_open,
    .release = buzzer_release,
    .write = buzzer_write,
};

static int buzzer_init(void)
{
    int result;
    result = register_chrdev(BUZZER_MAJOR, BUZZER_NAME, &buzzer_fops);

    if(result < 0) {
        printk(KERN_WARNING "Can't get any major\n");
        return result;
    }
    return 0;
}

static void buzzer_exit(void) {
	unregister_chrdev(BUZZER_MAJOR, BUZZER_NAME);
	printk("BUZZER module removed.\n");
}

module_init(buzzer_init);
module_exit(buzzer_exit);
MODULE_LICENSE("GPL");
