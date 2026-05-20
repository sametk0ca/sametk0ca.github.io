# OS Protection Rings and System Calls

- **Source:** [[ka-os-and-virtualisation]]
- **Tags:** #os #privilege #rings #syscalls

## Overview
Protection rings provide a hierarchical layering of privilege enforced by hardware. They ensure that less trusted code (user-space) cannot directly execute sensitive instructions or access privileged data.

## Hierarchical Privilege Layers
- **Ring 3 (User-space):** Least privileged. Standard applications run here.
- **Ring 1-2:** Historically used for drivers or system services, but mostly unused in modern general-purpose OSs.
- **Ring 0 (Kernel-space):** Most privileged. The OS kernel interacts directly with hardware here.
- **Ring -1 (Hypervisor):** Allows a hypervisor to manage multiple Ring 0 kernels in VMs.
- **Ring -2 (SMM):** System Management Mode used by firmware for power management and system control.
- **Ring -3 (Management Engine):** Autonomous subsystems (like Intel ME) that run even when the main CPU is powered off.

## System Calls (Syscalls)
A system call is the mechanism for a Ring 3 process to request a service from the Ring 0 kernel.
- **Transition:** Triggered via software interrupts (traps) or specialized instructions (e.g., `SYSCALL`, `SYSENTER`).
- **Mediation:** The kernel inspects syscall arguments at predefined entry points to prevent security violations.
- **Data Safety:** The kernel must ensure that buffers returned to user-space are properly initialized (e.g., zero-initialized) to prevent leaking sensitive kernel data.

## Related Vulnerabilities
- **Confused Deputy:** Tricking a privileged service (deputy) into misusing its authority.
- **SROP (Sigreturn-Oriented Programming):** Corrupting signal frames on the stack to hijack control flow during a `sigreturn` syscall.

## Related Concepts
- [[os-security-domains]]
- [[os-hardening-techniques]]
- [[capability-based-security]]
