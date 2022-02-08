class Context:
    def __eq__(self, other) -> bool: ...
    def __init__(self, model_name, model_dir, manifest, batch_size, gpu, mms_version, limit_max_image_pixels: bool = True) -> None: ...
    def get_request_id(self, idx: int = 0): ...
    def set_all_response_status(self, code: int = 200, phrase: str = "") -> None: ...
    def set_response_content_type(self, idx, value) -> None: ...
    def set_response_header(self, idx, key, value) -> None: ...
    def set_response_status(self, code: int = 200, phrase: str = "", idx: int = 0) -> None: ...

class RequestProcessor:
    def __init__(self, request_header) -> None: ...
    def add_response_property(self, key, value) -> None: ...
    def get_response_status_code(self) -> int: ...
    def report_status(self, code: int, reason_phrase=None) -> None: ...

