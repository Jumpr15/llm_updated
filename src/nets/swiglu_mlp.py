class SwiGLUMLP_Config():
    def __init__(
        self, 
        hidden_size: int, 
        hidden_act: int, 
        exp_factor: int,
    ):
      self.hidden_size = hidden_size
      self.intermediate_size = hidden_size*exp_factor
      self.hidden_act = hidden_act