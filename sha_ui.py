import tkinter as tk
from tkinter import filedialog, messagebox
import functions  # Import file chứa các chức năng


def main():
    window = tk.Tk()
    window.title("SHA-1 Hash Calculator")

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
        hashed_value = functions.sha1_hash(input_string)
        output_label.config(
            text=f"Giá trị băm SHA-1 của xâu văn bản là: {hashed_value}")

    def display_file_hash():
        file_path = get_file_path()
        if functions.os.path.exists(file_path):
            hashed_value = functions.calculate_file_hash(file_path)
            output_label.config(
                text=f"Giá trị băm SHA-1 của file là: {hashed_value}")
        else:
            messagebox.showerror("Error", "File không tồn tại.")

    def compare_hash_values():
        hash1 = hash1_entry.get()
        hash2 = hash2_entry.get()
        if functions.compare_hashes(hash1, hash2):
            output_label.config(text="Hai giá trị băm giống nhau.")
        else:
            output_label.config(text="Hai giá trị băm khác nhau.")

    def compare_file_hashes():
        if functions.os.path.exists(file_path1) and functions.os.path.exists(file_path2):
            hash1 = functions.calculate_file_hash(file_path1, False)
            hash2 = functions.calculate_file_hash(file_path2, False)
            if functions.compare_hashes(hash1, hash2):
                output_label.config(text="Hai file có giá trị băm giống nhau.")
            else:
                output_label.config(text="Hai file có giá trị băm khác nhau.")
        else:
            messagebox.showerror("Error", "Một trong hai file không tồn tại.")

    title_label1 = tk.Label(
        window, text="Tính giá trị băm SHA-1 với input", font=("Arial", 16))
    input_string_label = tk.Label(window, text="Nhập xâu văn bản:")
    input_string_entry = tk.Entry(window)
    hash_button = tk.Button(
        window, text="Tạo giá trị băm cho xâu văn bản", command=display_hashed_value)
    title_label5 = tk.Label(
        window, text="Tính giá trị băm SHA-1 với file", font=("Arial", 16))
    file_hash_button = tk.Button(
        window, text="Tạo giá trị băm cho file", command=display_file_hash)
    title_label2 = tk.Label(
        window, text="So sánh giá trị băm với input", font=("Arial", 16))
    hash1_label = tk.Label(window, text="Nhập giá trị băm thứ nhất:")
    hash1_entry = tk.Entry(window)
    hash2_label = tk.Label(window, text="Nhập giá trị băm thứ hai:")
    hash2_entry = tk.Entry(window)
    compare_button = tk.Button(
        window, text="So sánh giá trị băm", command=compare_hash_values)
    title_label3 = tk.Label(
        window, text="So sánh giá trị băm với file", font=("Arial", 16))
    file1_button = tk.Button(
        window, text="Chọn file thứ nhất", command=get_file_path1)
    file2_button = tk.Button(
        window, text="Chọn file thứ hai", command=get_file_path2)
    compare_file_button = tk.Button(
        window, text="So sánh giá trị băm của hai file", command=compare_file_hashes)
    title_label4 = tk.Label(window, text="Kết quả", font=("Arial", 16))
    output_label = tk.Label(window, text="")

    title_label1.pack()
    input_string_label.pack()
    input_string_entry.pack()
    hash_button.pack()
    title_label5.pack()
    file_hash_button.pack()
    title_label2.pack()
    hash1_label.pack()
    hash1_entry.pack()
    hash2_label.pack()
    hash2_entry.pack()
    compare_button.pack()
    title_label3.pack()
    file1_button.pack()
    file2_button.pack()
    compare_file_button.pack()
    title_label4.pack()
    output_label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
