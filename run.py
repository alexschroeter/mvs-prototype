import cupy as cp

if __name__ == "__main__":
    print(cp.cuda.Device(0).compute_capability)