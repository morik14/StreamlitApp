class Model:
    def __init__(
        self,
        run_id: int,
        chip_name: str,
        method: str,
        batch_size: int,
    ):
        self.run_id = run_id
        self.chip_name = chip_name
        self.method = method
        self.batch_size = batch_size
