import torch
import torch.utils.benchmark as benchmark
import time
import gc

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Utilisation du device : {device}")

def allocate_ram(target_gb=10):
    allocated_tensors = []
    try:
        size_per_tensor = (1024, 1024, 128)
        for _ in range(int(target_gb / 0.5)):
            allocated_tensors.append(torch.randn(*size_per_tensor, device="cpu"))
    except RuntimeError:
        print("🚀 10GB de RAM alloués !")
    return allocated_tensors

def allocate_vram(target_gb=4):
    allocated_tensors = []
    try:
        size_per_tensor = (1024, 1024, 128)
        for _ in range(int(target_gb / 0.5)):
            allocated_tensors.append(torch.randn(*size_per_tensor, device="cuda"))
    except RuntimeError:
        print("🚀 4GB de VRAM alloués !")
    return allocated_tensors

ram_tensors = allocate_ram(10)
vram_tensors = allocate_vram(4)

t = benchmark.Timer(
    stmt="torch.matmul(x, y)",
    setup="x = torch.randn(2048, 2048, device=device); y = torch.randn(2048, 2048, device=device)",
    globals={"torch": torch, "device": device}
)

start_time = time.time()
while time.time() - start_time < 120:
    torch.cuda.synchronize()
    result = t.blocked_autorange()
    print(result)

del ram_tensors, vram_tensors
gc.collect()
torch.cuda.empty_cache()

print("Stresstest terminé après 2 minutes !")

