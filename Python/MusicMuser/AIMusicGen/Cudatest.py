import torch

if torch.cuda.is_available():
    print("CUDA is available.")
    print("GPU devices:", torch.cuda.device_count())
else:
    print("CUDA is not available. using CPU")
