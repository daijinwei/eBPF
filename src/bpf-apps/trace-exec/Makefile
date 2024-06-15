APPS = execsnoop

$(APPS).bpf:
	clang -g -O2 -target bpf -D__TARGET_ARCH_x86_64 -I/usr/include/x86_64-linux-gnu -I. -c execsnoop.bpf.c -o execsnoop.bpf.o
	bpftool gen skeleton execsnoop.bpf.o > execsnoop.skel.h


$(APPS):
	clang -g -O2 -Wall -I . -c execsnoop.c -o execsnoop.o
	clang -Wall -O2 -g execsnoop.o -static -lbpf -lelf -lz -o execsnoop

vmlinux:
	bpftool btf dump file /sys/kernel/btf/vmlinux format c > vmlinux.h
