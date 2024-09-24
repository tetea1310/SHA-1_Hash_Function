import tkinter as tk
from tkinter import filedialog, messagebox
import os
from hash_functions import sha3_hash, calculate_file_hash, compare_hashes


def main():
    window = tk.Tk()
    window.title("SHA-3 Hash Calculator")
    window.configure(bg='lightblue')  # Change background color

    file_path1 = ""
    file_path2 = ""

    def get_input_string():
        return input_string_entry.get()

    def get_file_path():
        return filedialog.askopenfilename()

    def get_file_path1():
        nonlocal file_path1
        file_path1 = filedialog.askopenfilename()

    def get_file_path2():
        nonlocal file_path2
        file_path2 = filedialog.askopenfilename()

    def display_hashed_value():
        input_string = get_input_string()
        hashed_value = sha3_hash(input_string)
        output_label.config(
            text=f"Giá trị băm SHA-3 của plaintext là: {hashed_value}")

    def display_file_hash():
        file_path = get_file_path()
        if os.path.exists(file_path):
            hashed_value = calculate_file_hash(file_path)
            output_label.config(
                text=f"Giá trị băm SHA-3 của file là: {hashed_value}")
        else:
            messagebox.showerror("Error", "File không tồn tại.")

    def compare_hash_values():
        hash1 = hash1_entry.get()
        hash2 = hash2_entry.get()
        if compare_hashes(hash1, hash2):
            output_label.config(text="Hai giá trị băm giống nhau.")
        else:
            output_label.config(text="Hai giá trị băm khác nhau.")

    def compare_file_hashes():
        if os.path.exists(file_path1) and os.path.exists(file_path2):
            hash1 = calculate_file_hash(file_path1, False)
            hash2 = calculate_file_hash(file_path2, False)
            if compare_hashes(hash1, hash2):
                output_label.config(text="Hai file có giá trị băm giống nhau.")
            else:
                output_label.config(text="Hai file có giá trị băm khác nhau.")
        else:
            messagebox.showerror("Error", "Một trong hai file không tồn tại.")

    title_label1 = tk.Label(
        window, text="Tính giá trị băm SHA-3 với input", font=("Arial", 16), bg='lightblue')
    input_string_label = tk.Label(
        window, text="Nhập xâu văn bản:", bg='lightblue')
    input_string_entry = tk.Entry(window)
    hash_button = tk.Button(window, text="Tạo giá trị băm cho xâu văn bản",
                            command=display_hashed_value, bg='lightgreen')
    title_label5 = tk.Label(
        window, text="Tính giá trị băm SHA-3 với file", font=("Arial", 16), bg='lightblue')
    file_hash_button = tk.Button(
        window, text="Tạo giá trị băm cho file", command=display_file_hash, bg='lightgreen')
    title_label2 = tk.Label(window, text="So sánh giá trị băm với input", font=(
        "Arial", 16), bg='lightblue')
    hash1_label = tk.Label(
        window, text="Nhập giá trị băm thứ nhất:", bg='lightblue')
    hash1_entry = tk.Entry(window)
    hash2_label = tk.Label(
        window, text="Nhập giá trị băm thứ hai:", bg='lightblue')
    hash2_entry = tk.Entry(window)
    compare_button = tk.Button(
        window, text="So sánh giá trị băm", command=compare_hash_values, bg='lightgreen')
    title_label3 = tk.Label(window, text="So sánh giá trị băm với file", font=(
        "Arial", 16), bg='lightblue')
    file1_button = tk.Button(
        window, text="Chọn file thứ nhất", command=get_file_path1, bg='lightgreen')
    file2_button = tk.Button(
        window, text="Chọn file thứ hai", command=get_file_path2, bg='lightgreen')
    compare_file_button = tk.Button(
        window, text="So sánh giá trị băm của hai file", command=compare_file_hashes, bg='lightgreen')
    title_label4 = tk.Label(window, text="Kết quả",
                            font=("Arial", 16), bg='lightblue')
    output_label = tk.Label(window, text="")

    title_label1.pack(anchor="w")
    input_string_label.pack(anchor="w")
    input_string_entry.pack(anchor="w")
    hash_button.pack(anchor="w")
    title_label5.pack(anchor="w")
    file_hash_button.pack(anchor="w")
    title_label2.pack(anchor="w")
    hash1_label.pack(anchor="w")
    hash1_entry.pack(anchor="w")
    hash2_label.pack(anchor="w")
    hash2_entry.pack(anchor="w")
    compare_button.pack(anchor="w")
    title_label3.pack(anchor="w")
    file1_button.pack(anchor="w")
    file2_button.pack(anchor="w")
    compare_file_button.pack(anchor="w")
    title_label4.pack(anchor="w")
    output_label.pack(anchor="w")

    window.mainloop()


if __name__ == "__main__":
    main()
