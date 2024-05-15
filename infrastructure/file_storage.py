import os


class FileStorage:
    MODEL_DIR = "saved_models"

    @classmethod
    def save_model(cls, model, model_name):
        if not os.path.exists(cls.MODEL_DIR):
            os.makedirs(cls.MODEL_DIR)
        model_path = os.path.join(cls.MODEL_DIR, model_name)
        model.save(model_path)

    @classmethod
    def get_saved_models(cls):
        if not os.path.exists(cls.MODEL_DIR):
            return []
        return os.listdir(cls.MODEL_DIR)
