import torch

def get_device() -> torch.device:
    """
    Returns the appropriate device for PyTorch based on availability.
    """
    if torch.cuda.is_available():
        print("Using CUDA")
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        print("Using Apple Silicon (MPS)")
        return torch.device("mps")
    else:
        print("Using CPU")
        return torch.device("cpu")