def build_cmd(test) -> str: ...
def create_file_path(path: typing.Union[os.PathLike[bytes], os.PathLike[str], bytes, str]) -> None: ...
def delete_file_path(path: typing.Union[os.PathLike[bytes], os.PathLike[str], bytes, str]) -> None: ...
def run_test(test, cmd) -> int: ...
def test_default_handlers() -> None: ...
def test_model_archiver() -> None: ...
def validate(test) -> None: ...
def validate_archive_content(test) -> None: ...
def validate_archive_exists(test) -> None: ...
def validate_files(file_list, prefix, default_handler=None) -> None: ...
def validate_manifest_file(manifest, test, default_handler=None) -> None: ...
def validate_mar_archive(test) -> None: ...
def validate_noarchive_archive(test) -> None: ...
def validate_tar_archive(test_cfg) -> None: ...
