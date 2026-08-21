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


**Prerequisites:** At least two of CS 162, 161, 168, 152 or equivalent.


**Grading**: Coming soon!


# Syllabus

### Aug 27 (Thu) — Introduction

- [The UNIX Time-Sharing System](/assets/introduction/the_unix_time_sharing_system.pdf)

### Sep 1 (Tue) — Databases

- [A History and Evaluation of System R](/assets/databases/a_history_and_evaluation_of_system_r.pdf)
- [The Design and Implementation of INGRES](/assets/databases/the_design_and_implementation_of_ingres.pdf) (optional)
- [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-ahead Logging](/assets/databases/aries_a_transaction_recovery_method_supporting_fine_granularity_locking_and_partial_rollba.pdf) (optional)

### Sep 3 (Thu) — File Systems

- [A Fast File System for UNIX](/assets/file_systems/a_fast_file_system_for_unix.pdf)
- [The Design and Implementation of a Log-Structured File System](/assets/file_systems/the_design_and_implementation_of_a_log_structured_file_system.pdf)

### Sep 8 (Tue) — Transactions

- [Granularity of Locks and Degrees of Consistency in a Shared Database](/assets/transactions/granularity_of_locks_and_degrees_of_consistency_in_a_shared_database.pdf)
- [Principles of Transaction-Oriented Database Recovery](/assets/transactions/principles_of_transaction-oriented_database_recovery.pdf)

### Sep 10 (Thu) — OS Classics

- [Microkernel Operating System Architecture and Mach](/assets/os_classics/mach.pdf)
- [Exokernel: An Operating System Architecture for Application-Level Resource Management](/assets/os_classics/exokernel_an_operating_system_architecture_for_application_level_resource_management.pdf)

### Sep 15 (Tue) — OS (II)

- [The Scalable Commutativity Rule: Designing Scalable Software for Multicore Processors](/assets/os_ii/the_scalable_commutativity_rule_designing_scalable_software_for_multicore_processors.pdf)
- [The Multikernel: A New OS Architecture for Scalable Multicore Systems](/assets/os_ii/the_multikernel_a_new_os_architecture_for_scalable_multicore_systems.pdf)

### Sep 17 (Thu) — Consensus

- [Paxos Made Simple](/assets/consensus/paxos_made_simple.pdf)
- [Paxos Made Moderately Complex](/assets/consensus/paxos_made_moderately_complex.pdf)
- [In Search of an Understandable Consensus Algorithm (Raft)](/assets/consensus/in_search_of_an_understandable_consensus_algorithm_raft.pdf)

### Sep 22 (Tue) — Distributed Storage

- [The Google File System](/assets/distributed_storage/the_google_file_system.pdf)
- [Bigtable: A Distributed Storage System for Structured Data](/assets/distributed_storage/bigtable_a_distributed_storage_system_for_structured_data.pdf)

### Sep 24 (Thu) — DHTs, KV Stores

- [Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications](/assets/dhts_kv_stores/chord_a_scalable_peer_to_peer_lookup_service_for_internet_applications.pdf)
- [Dynamo: Amazon's Highly Available Key-value Store](/assets/dhts_kv_stores/dynamo_amazon_s_highly_available_key_value_store.pdf)

### Sep 29 (Tue) — Distributed Coordination

- [Coordination Avoidance in Database Systems](/assets/distributed_coordination/coordination_avoidance_in_database_systems.pdf)
- [CRDTs: Consistency without Concurrency Control](/assets/distributed_coordination/crdts_consistency_without_concurrency_control.pdf)

### Oct 1 (Thu) — Virtualization

- [Formal Requirements for Virtualizable Third Generation Architectures](/assets/virtualization/formal_requirements_for_virtualizable_third_generation_architectures.pdf)
- [Disco: Running Commodity Operating Systems on Scalable Multiprocessors](/assets/virtualization/disco_running_commodity_operating_systems_on_scalable_multiprocessors.pdf)
- [Xen and the Art of Virtualization](/assets/virtualization/xen_and_the_art_of_virtualization.pdf)

### Oct 6 (Tue) — Cluster Management

- [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](/assets/cluster_mgmt/mesos_a_platform_for_fine_grained_resource_sharing_in_the_data_center.pdf)
- [Large-scale Cluster Management at Google with Borg](/assets/cluster_mgmt/large_scale_cluster_management_at_google_with_borg.pdf)
- [Borg, Omega, and Kubernetes](/assets/cluster_mgmt/borg_omega_and_kubernetes.pdf) (optional)

### Oct 8 (Thu) — Scheduling

- [Lottery Scheduling: Flexible Proportional-Share Resource Management](/assets/scheduling/lottery_scheduling_flexible_proportional_share_resource_management.pdf)
- [CFS Scheduler Design (Linux kernel documentation)](https://docs.kernel.org/scheduler/sched-design-CFS.html)
- [Dominant Resource Fairness: Fair Allocation of Multiple Resource Types](/assets/scheduling/dominant_resource_fairness_fair_allocation_of_multiple_resource_types.pdf)

### Oct 13 (Tue) — Datacenter Applications

- [Web Search for a Planet: The Google Cluster Architecture](/assets/datacenter_applications/web_search_for_a_planet_the_google_cluster_architecture.pdf)
- [The Tail at Scale](/assets/datacenter_applications/the_tail_at_scale.pdf)
- [Attack of the Killer Microseconds](/assets/datacenter_applications/attack_of_the_killer_microseconds.pdf)

### Oct 15 (Thu) — Distributed Data Processing

- [MapReduce: Simplified Data Processing on Large Clusters](/assets/distributed_data_processing/mapreduce_simplified_data_processing_on_large_clusters.pdf)
- [Spark: Cluster Computing with Working Sets](/assets/distributed_data_processing/spark_cluster_computing_with_working_sets.pdf)

### Oct 20 (Tue) — Serverless

- [Firecracker: Lightweight Virtualization for Serverless Applications](/assets/serverless/firecracker_lightweight_virtualization_for_serverless_applications.pdf)
- [Unifying Serverless and Microservice Workloads with SigmaOS](/assets/serverless/unifying_serverless_and_microservice_workloads_with_sigmaos.pdf)

### Oct 22 (Thu) — Disaggregated/CXL

- [LegoOS: A Disseminated, Distributed OS for Hardware Resource Disaggregation](/assets/disaggregated_cxl/legoos_a_disseminated_distributed_os_for_hardware_resource_disaggregation.pdf)
- [Tigon: A Distributed Database for a CXL Pod](/assets/disaggregated_cxl/tigon_a_distributed_database_for_a_cxl_pod.pdf)

### Oct 27 (Tue) — Security & Privacy

- [Capability Myths Demolished](/assets/security_privacy/capability_myths_demolished.pdf)
- [Private Web Search with Tiptoe](/assets/security_privacy/private_web_search_with_tiptoe.pdf)
- [Intel SGX Explained](/assets/security_privacy/intel_sgx_explained.pdf) (optional)

### Oct 29 (Thu) — Verification

- [seL4: Formal Verification of an OS Kernel](/assets/verification/sel4_formal_verification_of_an_os_kernel.pdf)
- [Using Crash Hoare Logic for Certifying the FSCQ File System](/assets/verification/using_crash_hoare_logic_for_certifying_the_fscq_file_system.pdf)
- [Push-Button Verification of File Systems via Crash Refinement (Yggdrasil)](/assets/verification/push_button_verification_of_file_systems_via_crash_refinement_yggdrasil.pdf)
- [Hyperkernel: Push-Button Verification of an OS Kernel](/assets/verification/hyperkernel_push_button_verification_of_an_os_kernel.pdf)

### Nov 3 (Tue) — Parallel Programming

- [Ray: A Distributed Framework for Emerging AI Applications](/assets/parallel_programming/ray_a_distributed_framework_for_emerging_ai_applications.pdf)
- [Halide: A Language and Compiler for Optimizing Parallelism, Locality, and Recomputation in Image Processing Pipelines](/assets/parallel_programming/halide_a_language_and_compiler_for_optimizing_parallelism_locality_and_recomputation_in_im.pdf)

### Nov 5 (Thu) — ML Programming Frameworks

- [TensorFlow: A System for Large-Scale Machine Learning](/assets/ml_programming_frameworks/tensorflow_a_system_for_large_scale_machine_learning.pdf)
- [PyTorch: An Imperative Style, High-Performance Deep Learning Library](/assets/ml_programming_frameworks/pytorch_an_imperative_style_high_performance_deep_learning_library.pdf)

### Nov 10 (Tue) — Pre-training

- *Readings TBD*

### Nov 12 (Thu) — Post-training

- *Readings TBD*

### Nov 17 (Tue) — Inference (I)

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)](/assets/inference_i/efficient_memory_management_for_large_language_model_serving_with_pagedattention_vllm.pdf)
- [NanoFlow: Towards Optimal Large Language Model Serving Throughput](/assets/inference_i/nanoflow_towards_optimal_large_language_model_serving_throughput.pdf)

### Nov 19 (Thu) — Inference (II): Multi-modal, MoT

- [StreamDiffusion: A Pipeline-level Solution for Real-Time Interactive Generation](/assets/inference_ii_multi_modal_mot/streamdiffusion_a_pipeline_level_solution_for_real_time_interactive_generation.pdf)
- [M\*: A Modular, Extensible, Serving System for Multimodal Models](/assets/inference_ii_multi_modal_mot/m_a_modular_extensible_serving_system_for_multimodal_models.pdf)
- [Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models](/assets/inference_ii_multi_modal_mot/mixture_of_transformers_a_sparse_and_scalable_architecture_for_multi_modal_foundation_mode.pdf)

### Nov 24 (Tue) — Thanksgiving

- *No class*

### Nov 26 (Thu) — Thanksgiving

- *No class*

### Dec 1 (Tue) — AI for Systems

- *Guest lecture; readings TBD*

### Dec 3 (Thu) — Systems Support for Agents

- *Guest lecture; readings TBD*

### Dec 8 (Tue) — OSDI Deadline

- *No class*

### Dec 10 (Thu) — Poster Day

- *No class*
