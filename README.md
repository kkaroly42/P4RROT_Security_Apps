# Description
This repository contains the test artifacts and the scripts used to produce them for the paper
'Simplifying the Development of In-Network Security Applications with P4RROT'. 

## Port knocking

The knocking directory contains the following items:
* The P4RROT script generating the data plane code [knocking/codegen.py](knocking/codegen.py)
* The generated P4 files and the template [knocking/result.p4](knocking/result.p4)
* An example control plane script we used to produce the artifacts [knocking/setup_knocking.py](knocking/setup_knocking.py)
* The pcap files recorded during testing [knocking/pcaps](knocking/pcaps)
* A Python script that can be used to send knocking TCP packets [knocking/tcp_forger.py](knocking/tcp_forger.py)

## NTP Guard

The ntp_guard directory contains the following items:
* The P4RROT script generating the data plane code [ntp_guard/codegen.py](ntp_guard/codegen.py)
* The generated P4 files and the template [ntp_guard/result.p4](ntp_guard/result.p4)
* An example control plane script we used to produce the artifacts [ntp_guard/setup_ntp.py](ntp_guard/setup_ntp.py)
* The pcap files recorded during testing [ntp_guard/pcaps](ntp_guard/pcaps)
* A Python script that can be used to send forged NTP packets. The generated packets can be normal or ones that constitute an exploit, chosen randomly [ntp_guard/ntp_forger.py](ntp_guard/ntp_forger.py)

## Usage of the scripts

Please note that the control plane scripts contain hard coded MAC addresses. These have to be modified to run on your own system.
Both the TCP forger and the NTP forger scripts take exactly one argument, the network device you wish to send out the packets on.

For example:
```
python3 tcp_forger.py veth3
```

## P40F

The p40f directory contains the following items:
* The P4RROT script generating the data plane code [p40f/codegen.py](p40f/codegen.py)
* The generated P4 files and the template [p40f/result.p4](p40f/result.p4)

The original implementation and a tutorial on how to use it can be found at [P40f](https://github.com/sherrybai/P40f)

## P4RROT

This repository contains only files relevant to the paper. The source code and an introduction to P4RROT can be read at [P4RROT](https://github.com/Team-P4RROT/P4RROT).
