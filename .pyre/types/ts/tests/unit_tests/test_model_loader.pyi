class TestListModels:
    def test_list_models(self) -> None: ...
    def test_list_models_legacy(self) -> None: ...

class TestLoadModels:
    def patches(self, mocker) -> ts.tests.unit_tests.test_model_loader.TestLoadModels.patches.Patches: ...
    def test_load_class_model(self, patches) -> None: ...
    def test_load_func_model(self, patches) -> None: ...
    def test_load_func_model_with_error(self, patches) -> None: ...
    def test_load_model_with_error(self, patches) -> None: ...

class TestModelFactory:
    def test_model_loader_factory(self) -> None: ...

