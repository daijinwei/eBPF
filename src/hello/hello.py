#!/usr/bin/env python3
# 1) import bcc library
from bcc import BPF

# 2) load BPF program
b = BPF(src_file="hello.c")
# 3) attach kprobe
# 以下系统调用，和kernel有关系,我的4.18.0-348.7.1.el8_5.x86_64，用do_sys_open
#b.attach_kprobe(event="do_sys_openat2", fn_name="hello_world")
#b.attach_kprobe(event="do_sys_openat2", fn_name="hello_world")
b.attach_kprobe(event="do_sys_open", fn_name="hello_world")
# 4) read and print /sys/kernel/debug/tracing/trace_pipe
b.trace_print()
