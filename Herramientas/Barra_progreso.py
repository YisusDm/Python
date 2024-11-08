import time
from tqdm import tqdm


with tqdm(total=100, desc="Procesando") as pbar:
    for i in range(100):
        time.sleep(0.05)
        pbar.update(1)
print("Procesado Exitoso!!")    