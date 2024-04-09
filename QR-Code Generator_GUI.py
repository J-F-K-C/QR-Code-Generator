import tkinter as tk
from tkinter import ttk, filedialog
import qrcode

def generate_qr():
    url = url_entry.get()
    output_file = output_file_entry.get()
    
    qr = qrcode.QRCode(
        version=10,
        box_size=10,
        border=4
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color_entry.get(), back_color=back_color_entry.get())
    img.save(output_file)
    status_label.config(text=f"QR-Code saved as '{output_file}'")

def choose_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file)

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")

# URL Entry
url_label = ttk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

url_entry = ttk.Entry(root, width=30)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Fill Color Entry
fill_color_label = ttk.Label(root, text="Fill Color:")
fill_color_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

fill_color_entry = ttk.Entry(root, width=10)
fill_color_entry.grid(row=1, column=1, padx=5, pady=5)
fill_color_entry.insert(tk.END, "")  # Default to blue

# Back Color Entry
back_color_label = ttk.Label(root, text="Back Color:")
back_color_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

back_color_entry = ttk.Entry(root, width=10)
back_color_entry.grid(row=2, column=1, padx=5, pady=5)
back_color_entry.insert(tk.END, "")  # Default to white

# Output File Entry
output_file_label = ttk.Label(root, text="Output File:")
output_file_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

output_file_entry = ttk.Entry(root, width=30)
output_file_entry.grid(row=3, column=1, padx=5, pady=5)

choose_file_button = ttk.Button(root, text="Choose File", command=choose_output_file)
choose_file_button.grid(row=3, column=2, padx=5, pady=5)

# Generate Button
generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Status Label
status_label = ttk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
