TMP_DIR: str = ...
execution_params: typing.Dict[str, typing.Union[int, str]] = ...
def benchmark(test_plan, url, gpus, exec_env, concurrency, requests, batch_size, batch_delay, input, workers, content_type, image, docker_runtime, backend_profiling, config_properties, inference_model_url) -> None: ...
def check_torchserve_health() -> typing.Optional[bool]: ...
def custom() -> None: ...
def docker_torchserve_start() -> None: ...
def execute(command, wait: bool = False, stdout=None, stderr=None, shell: bool = True): ...
def extract_entity(data, pattern: typing.Pattern[str], index, delim: str = " "): ...
def extract_metrics() -> None: ...
def failure_exit(msg) -> None: ...
def generate_csv_output() -> typing.Dict[str, str]: ...
def generate_latency_graph() -> None: ...
def generate_profile_graph() -> None: ...
def generate_report() -> None: ...
def getAPIS() -> None: ...
def local_torserve_start() -> None: ...
def prepare_common_dependency() -> None: ...
def prepare_docker_dependency() -> None: ...
def prepare_local_dependency() -> None: ...
def register_model() -> None: ...
def resnet152_batch() -> None: ...
def resnet152_batch_docker() -> None: ...
def run_benchmark() -> None: ...
def soak() -> None: ...
def stop_torchserve() -> None: ...
def unregister_model() -> None: ...
def update_exec_params(input_param) -> None: ...
def vgg11_10000r_100c() -> None: ...
def vgg11_1000r_10c() -> None: ...
def warm_up() -> None: ...
