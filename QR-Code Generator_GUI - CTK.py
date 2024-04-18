import customtkinter as ctk
from tkinter import filedialog
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
    output_file_entry.delete(0, ctk.END)
    output_file_entry.insert(0, output_file)
    
def exit_click():
    root.destroy()

# GUI setup
root = ctk.CTk()
root.title("QR Code Generator")

# URL Entry
url_label = ctk.CTkLabel(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

url_entry = ctk.CTkEntry(root, width=150)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Fill Color Entry
fill_color_label = ctk.CTkLabel(root, text="Fill Color:")
fill_color_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

fill_color_entry = ctk.CTkEntry(root, width=50)
fill_color_entry.grid(row=1, column=1, padx=5, pady=5)
fill_color_entry.insert(ctk.END, "")  # Default to blue

# Back Color Entry
back_color_label = ctk.CTkLabel(root, text="Back Color:")
back_color_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

back_color_entry = ctk.CTkEntry(root, width=50)
back_color_entry.grid(row=2, column=1, padx=5, pady=5)
back_color_entry.insert(ctk.END, "")  # Default to white

# Output File Entry
output_file_label = ctk.CTkLabel(root, text="Output File:")
output_file_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

output_file_entry = ctk.CTkEntry(root, width=150)
output_file_entry.grid(row=3, column=1, padx=5, pady=5)

choose_file_button = ctk.CTkButton(root, text="Choose File", command=choose_output_file)
choose_file_button.grid(row=3, column=2, padx=5, pady=5)

# Generate Button
generate_button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Exit Button
exit_button = ctk.CTkButton(root, text="Exit", command=exit_click)
exit_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Status Label
status_label = ctk.CTkLabel(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()