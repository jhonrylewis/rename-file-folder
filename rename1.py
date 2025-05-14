import os

def sanitize_filename(filename):
    """Mengganti spasi dalam nama file dengan underscore."""
    return filename.replace(" ", "_")

def rename_files_with_custom_numbering(folder_path, prefix, start_number_str, suffix, digits):
    """
    Mengubah nama file di dalam folder secara berurutan dengan menambahkan kata depan dan underscore,
    mengatur format nomor awal dengan jumlah digit yang ditentukan dan underscore setelahnya,
    menambahkan kata belakang, dan mengganti spasi dengan underscore pada nama baru yang dihasilkan.

    Args:
        folder_path (str): Path ke folder yang berisi file-file yang akan diubah namanya.
        prefix (str): Kata depan yang akan ditambahkan ke nama file baru.
        start_number_str (str): Nomor awal untuk penamaan file (dalam format string).
        suffix (str): Kata belakang yang akan ditambahkan ke nama file baru.
        digits (int): Jumlah digit yang diinginkan untuk penomoran (misalnya, 4 untuk 0001).
    """
    try:
        files = sorted(os.listdir(folder_path))
        start_number = int(start_number_str)
        count = start_number
        for filename in files:
            if os.path.isfile(os.path.join(folder_path, filename)):
                _, ext = os.path.splitext(filename)
                # Format angka dengan leading zeros sesuai jumlah digit
                formatted_count = f"{count:0{digits}d}"
                # Membuat nama file baru dengan format: prefix_ + nomor_ + suffix + ekstensi
                base_new_filename = f"{prefix.strip()}_{formatted_count}_{suffix.strip()}"
                # Membersihkan spasi pada nama file baru dengan underscore
                new_filename = sanitize_filename(base_new_filename) + ext
                old_filepath = os.path.join(folder_path, filename)
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(old_filepath, new_filepath)
                print(f"Berhasil mengubah nama '{filename}' menjadi '{new_filename}'")
                count += 1
        print(f"Semua file berhasil diubah namanya secara berurutan di folder '{folder_path}' dengan prefix '{prefix}' dan underscore setelahnya, dimulai dari nomor {start_number_str} dengan format {digits} digit dan underscore setelahnya, suffix '{suffix}', dan spasi diganti dengan underscore.")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' tidak ditemukan.")
    except ValueError:
        print("Error: Nomor awal dan jumlah digit harus berupa bilangan bulat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    folder_path = "E:\\SAL"  # Path folder Anda
    prefix = input("Masukkan kata depan yang ingin ditambahkan (biarkan kosong jika tidak ada): ")
    start_number_str = input("Masukkan nomor awal penamaan file (misalnya, 1 atau 0001): ")
    while True:
        digits_str = input("Masukkan jumlah digit untuk penomoran (misalnya, 4 untuk 0001): ")
        try:
            digits = int(digits_str)
            if digits > 0:
                break
            else:
                print("Jumlah digit harus lebih dari 0.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk jumlah digit.")
    suffix = input("Masukkan kata belakang yang ingin ditambahkan (biarkan kosong jika tidak ada): ")

    rename_files_with_custom_numbering(folder_path, prefix, start_number_str, suffix, digits)