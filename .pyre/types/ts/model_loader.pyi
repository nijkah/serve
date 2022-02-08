class ModelLoader:
    def load(self, model_name, model_dir, handler, gpu_id, batch_size, envelope=None, limit_max_image_pixels: bool = True): ...

class ModelLoaderFactory:
    def get_model_loader() -> TsModelLoader: ...

class TsModelLoader:
    def _load_default_handler(self, handler) -> types.ModuleType: ...
    def load(self, model_name, model_dir, handler, gpu_id, batch_size, envelope=None, limit_max_image_pixels: bool = True) -> ts.service.Service: ...

