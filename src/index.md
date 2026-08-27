title: CS262A: Advanced Topics in Computer Systems
template: standalone.html

# CS262A: Advanced Topics in Computer Systems

**Fall 2026, UC Berkeley**

**Timing:** Tuesday and Thursday, 12:30pm to 2:00pm

**Location:** The Gateway Building B1022

**Instructor:** [Rishabh Iyer](https://rishabh246.github.io/)

**GSI:** [Shubham Mishra](https://grapheo12.in)


**Course description:** This is a graduate survey of Computer Systems covering a breadth of topics including, but not limited to, early/classical systems, file systems, transactions, distributed systems, security and AI systems.
The objective is to get into the habit of reading systems papers, developing the ability to extract the key design insights, and being able to discuss the strengths and weaknesses of the arguments presented in the papers.
Students are expected to lead and contribute to discussions in class, while working towards a group research project of publishable quality.


**Grading**:

- 40%: class participation (includes paper reviews). 
- 20%: paper presentations.
- 40%: course project.


**Paper Reviews**: Please submit your reviews [here](https://docs.google.com/forms/d/e/1FAIpQLSfevQSH0lgyMZtHVAQw7qfHfte2MSNXo9tLWfzcqPvermY3sw/viewform?usp=sharing&ouid=111301588409301165028).


# Schedule

### Aug 27 (Thu) — Introduction

- [The UNIX Time-Sharing System](/assets/introduction/unix_time_sharing.pdf)

### Sep 1 (Tue) — Databases

- [A History and Evaluation of System R](/assets/databases/system_r.pdf)

**Optional:**

- [The Design and Implementation of INGRES](/assets/databases/ingres.pdf)
- [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-ahead Logging](/assets/databases/aries.pdf)

### Sep 3 (Thu) — File Systems

- [A Fast File System for UNIX](/assets/file_systems/fast_file_system.pdf)
- [The Design and Implementation of a Log-Structured File System](/assets/file_systems/log_structured_file_system.pdf)

**Optional:**

- Debates on Log structured file system: [Seltzer's Paper](https://www.seltzer.com/assets/publications/File-System-Logging-versus-Clustering-A-Performance-Comparison.pdf), [Ousterhout's critique](https://www.seltzer.com/assets/publications/ouster_critique2.html), [Seltzer's Response](https://www.seltzer.com/assets/publications/ouster_critique1_rebuttal.html).

- [Analysis and evaluation of Journaling File Systems](/assets/file_systems/journaling_file_systems.pdf)

### Sep 8 (Tue) — Transactions

- [Granularity of Locks and Degrees of Consistency in a Shared Database](/assets/transactions/granularity_of_locks.pdf)
- [Principles of Transaction-Oriented Database Recovery](/assets/transactions/database_recovery.pdf)

### Sep 10 (Thu) — OS Classics

- [Microkernel Operating System Architecture and Mach](/assets/os_classics/mach.pdf)
- [Exokernel: An Operating System Architecture for Application-Level Resource Management](/assets/os_classics/exokernel.pdf)

### Sep 15 (Tue) — OS (II)
<!-- 
- [The Scalable Commutativity Rule: Designing Scalable Software for Multicore Processors](/assets/os_ii/scalable_commutativity_rule.pdf) -->
- [The Multikernel: A New OS Architecture for Scalable Multicore Systems](/assets/os_ii/multikernel.pdf)

- [The eBPF Runtime in the Linux Kernel](/assets/os_ii/ebpf_runtime.pdf)

**Optional:**

- [SPIN - An Extensible Microkernel for Application-specific Operating System Services](/assets/os_ii/spin.pdf)

### Sep 17 (Thu) — Consensus

- [Paxos Made Moderately Complex](/assets/consensus/paxos_made_moderately_complex.pdf)
- [In Search of an Understandable Consensus Algorithm (Raft)](/assets/consensus/raft.pdf)

**Optional:**

- [Paxos Made Simple](/assets/consensus/paxos_made_simple.pdf)


### Sep 22 (Tue) — Distributed Storage

- [The Google File System](/assets/distributed_storage/google_file_system.pdf)
- [Bigtable: A Distributed Storage System for Structured Data](/assets/distributed_storage/bigtable.pdf)

### Sep 24 (Thu) — DHTs, KV Stores

- [Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications](/assets/dhts_kv_stores/chord.pdf)
- [Dynamo: Amazon's Highly Available Key-value Store](/assets/dhts_kv_stores/dynamo.pdf)

### Sep 29 (Tue) — Distributed Coordination

- [Coordination Avoidance in Database Systems](/assets/distributed_coordination/coordination_avoidance.pdf)
- [CRDTs: Consistency without Concurrency Control](/assets/distributed_coordination/crdts.pdf)

### Oct 1 (Thu) — Virtualization

<!-- - [Formal Requirements for Virtualizable Third Generation Architectures](/assets/virtualization/virtualizable_architectures.pdf) -->
- [Disco: Running Commodity Operating Systems on Scalable Multiprocessors](/assets/virtualization/disco.pdf)
- [Xen and the Art of Virtualization](/assets/virtualization/xen.pdf)

### Oct 6 (Tue) — Cluster Management

- [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](/assets/cluster_mgmt/mesos.pdf)
<!-- - [Large-scale Cluster Management at Google with Borg](/assets/cluster_mgmt/borg.pdf) -->
- [Borg, Omega, and Kubernetes](/assets/cluster_mgmt/borg_omega_kubernetes.pdf)

### Oct 8 (Thu) — Scheduling

- [Lottery Scheduling: Flexible Proportional-Share Resource Management](/assets/scheduling/lottery_scheduling.pdf)
<!-- - [CFS Scheduler Design (Linux kernel documentation)](https://docs.kernel.org/scheduler/sched-design-CFS.html) -->
- [Dominant Resource Fairness: Fair Allocation of Multiple Resource Types](/assets/scheduling/dominant_resource_fairness.pdf)

### Oct 13 (Tue) — Datacenter Applications

- [Web Search for a Planet: The Google Cluster Architecture](/assets/datacenter_applications/google_cluster_architecture.pdf)
- [The Tail at Scale](/assets/datacenter_applications/tail_at_scale.pdf)
- [Attack of the Killer Microseconds](/assets/datacenter_applications/killer_microseconds.pdf)
- [IX: A Protected Dataplane Operating System for
High Throughput and Low Latency](/assets/datacenter_applications/ix_dataplane.pdf)

**Optional:**

- [Arrakis: The Operating System is the Control Plane](/assets/datacenter_applications/arrakis.pdf)
- [Shinjuku: Preemptive Scheduling for $\mu$second-scale Tail Latency](/assets/datacenter_applications/shinjuku.pdf)

### Oct 15 (Thu) — Distributed Data Processing

- [MapReduce: Simplified Data Processing on Large Clusters](/assets/distributed_data_processing/mapreduce.pdf)
- [Spark: Cluster Computing with Working Sets](/assets/distributed_data_processing/spark.pdf)

**Optional:**

- [Apache Flink™: Stream and Batch Processing in a Single Engine](/assets/distributed_data_processing/apache_flink.pdf)


### Oct 20 (Tue) — Serverless

- [Firecracker: Lightweight Virtualization for Serverless Applications](/assets/serverless/firecracker.pdf)
- [Unifying Serverless and Microservice Workloads with SigmaOS](/assets/serverless/sigmaos.pdf)

### Oct 22 (Thu) — Disaggregated/CXL

- [LegoOS: A Disseminated, Distributed OS for Hardware Resource Disaggregation](/assets/disaggregated_cxl/legoos.pdf)
- [Tigon: A Distributed Database for a CXL Pod](/assets/disaggregated_cxl/tigon.pdf)

### Oct 27 (Tue) — Security & Privacy

<!-- - [Capability Myths Demolished](/assets/security_privacy/capability_myths.pdf) -->
- [EROS: a fast capability system](/assets/security_privacy/eros.pdf)
- [Private Web Search with Tiptoe](/assets/security_privacy/tiptoe.pdf)
<!-- - [Intel SGX Explained](/assets/security_privacy/intel_sgx.pdf) (optional) -->

**Optional:**

- [Making Information Flow Explicit in HiStar](/assets/security_privacy/histar.pdf)

### Oct 29 (Thu) — Verification

- [seL4: Formal Verification of an OS Kernel](/assets/verification/sel4.pdf)
- [Verus: A Practical Foundation for Systems Verification](/assets/verification/verus.pdf)

**Optional:**

- [Using Crash Hoare Logic for Certifying the FSCQ File System](/assets/verification/fscq.pdf)
<!-- - [Push-Button Verification of File Systems via Crash Refinement (Yggdrasil)](/assets/verification/yggdrasil.pdf)
- [Hyperkernel: Push-Button Verification of an OS Kernel](/assets/verification/hyperkernel.pdf) -->

### Nov 3 (Tue) — Parallel Programming

- [Ray: A Distributed Framework for Emerging AI Applications](/assets/parallel_programming/ray.pdf)
- [Halide: Decoupling Algorithms from Schedules for High-Performance Image Processing](/assets/parallel_programming/halide.pdf)

**Optional:**

- [Erlang: Making reliable distributed systems in the presence of software errors](https://erlang.org/download/armstrong_thesis_2003.pdf)

### Nov 5 (Thu) — ML Programming Frameworks

- [TensorFlow: A System for Large-Scale Machine Learning](/assets/ml_programming_frameworks/tensorflow.pdf)
- [PyTorch: An Imperative Style, High-Performance Deep Learning Library](/assets/ml_programming_frameworks/pytorch.pdf)

### Nov 10 (Tue) — Pre-training

- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](/assets/pre_training/zero_optimizations.pdf)

- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](/assets/pre_training/pytorch_fsdp.pdf)

### Nov 12 (Thu) — Post-training

- [HybridFlow: A Flexible and Efficient RLHF Framework](/assets/post_training/hybridflow.pdf)

- [OpenRLHF: An Easy-to-use, Scalable
and High-performance RLHF Framework](/assets/post_training/openrlhf.pdf)

### Nov 17 (Tue) — Inference (I)

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)](/assets/inference_i/vllm.pdf)
- [NanoFlow: Towards Optimal Large Language Model Serving Throughput](/assets/inference_i/nanoflow.pdf)

### Nov 19 (Thu) — Inference (II): Multi-modal, MoT

- [StreamDiffusion: A Pipeline-level Solution for Real-Time Interactive Generation](/assets/inference_ii_multi_modal_mot/streamdiffusion.pdf)
- [M\*: A Modular, Extensible, Serving System for Multimodal Models](/assets/inference_ii_multi_modal_mot/mstar.pdf)
<!-- - [Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models](/assets/inference_ii_multi_modal_mot/mixture_of_transformers.pdf) -->

### Nov 24 (Tue) — Thanksgiving

- *No class*

### Nov 26 (Thu) — Thanksgiving

- *No class*

### Dec 1 (Tue) — AI for Systems

- *Guest lecture; Readings TBD*

### Dec 3 (Thu) — Systems Support for Agents

- *Guest lecture; Readings TBD*

### Dec 8 (Tue) — OSDI Deadline

- *No class*

### Dec 10 (Thu) — Poster Day

- *No class*
