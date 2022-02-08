class MetricsStore:
    def __init__(self, request_ids, model_name) -> None: ...
    def _add_or_update(self, name, value, req_id, unit, metrics_method=None, dimensions=None) -> None: ...
    def add_counter(self, name, value, idx=None, dimensions=None) -> None: ...
    def add_error(self, name, value, dimensions=None) -> None: ...
    def add_metric(self, name, value, unit, idx=None, dimensions=None) -> None: ...
    def add_percent(self, name, value, idx=None, dimensions=None) -> None: ...
    def add_size(self, name, value, idx=None, unit: str = "MB", dimensions=None) -> None: ...
    def add_time(self, name, value, idx=None, unit: str = "ms", dimensions=None) -> None: ...

