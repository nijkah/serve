class BenchmarkHandler:
    def __init__(self, model_name, benchmark_execution_id, connection=None, is_local_execution: bool = False, benchmark_type: str = "docker") -> None: ...
    def execute_benchmark(self, test_config, ec2_instance_type: str, cuda_version_for_instance, docker_repo_tag_for_current_instance, exec_env: str = "docker", local_virutal_env: str = "python3") -> None: ...

