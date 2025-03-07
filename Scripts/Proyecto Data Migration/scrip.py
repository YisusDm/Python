import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def select_folder(entry_widget):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)

def sync_folders():
    source = entry_source.get()
    destination = entry_destination.get()
    
    if not source or not destination:
        messagebox.showerror("Error", "Seleccione ambas rutas antes de continuar.")
        return
    
    files_source = set(os.listdir(source))
    files_destination = set(os.listdir(destination))
    
    missing_files = files_destination - files_source
    total_files = len(missing_files)
    copied_files = []
    failed_files = []
    
    progress_bar["maximum"] = total_files
    
    for index, file in enumerate(missing_files, start=1):
        src_path = os.path.join(destination, file)
        dest_path = os.path.join(source, file)
        try:
            shutil.copy2(src_path, dest_path)
            copied_files.append(file)
        except Exception as e:
            failed_files.append({"file": file, "error": str(e)})
        progress_bar["value"] = index
        root.update_idletasks()
    
    report = {
        "copied_files": copied_files,
        "failed_files": failed_files,
        "total_copied": len(copied_files),
        "total_failed": len(failed_files)
    }
    
    with open("sync_report.json", "w") as json_file:
        json.dump(report, json_file, indent=4)
    
    messagebox.showinfo("Proceso finalizado", f"Archivos copiados: {len(copied_files)}\nErrores: {len(failed_files)}")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Sincronizador de Archivos")
root.geometry("500x300")

tl_source = tk.Label(root, text="Ruta (Destino)")
tl_source.pack()
entry_source = tk.Entry(root, width=50)
entry_source.pack()
btn_source = tk.Button(root, text="Seleccionar", command=lambda: select_folder(entry_source))
btn_source.pack()

tl_destination = tk.Label(root, text="Ruta (Origen)")
tl_destination.pack()
entry_destination = tk.Entry(root, width=50)
entry_destination.pack()
btn_destination = tk.Button(root, text="Seleccionar", command=lambda: select_folder(entry_destination))
btn_destination.pack()

progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=10)

btn_sync = tk.Button(root, text="Sincronizar", command=sync_folders)
btn_sync.pack()

root.mainloop()
