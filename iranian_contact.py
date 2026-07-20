import os
import sys

def generate_vcf(prefix, output_dir="."):
    filename = os.path.join(output_dir, f"{prefix}.vcf")
    total = 10_000_000  # 7 digits: 0000000 to 9999999
    print(f"Generating {prefix}.vcf ({total} numbers)...")
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(total):
            number = f"{prefix}{i:07d}"   # e.g., 09101234567
            f.write("BEGIN:VCARD\n")
            f.write("VERSION:3.0\n")
            f.write(f"FN:{number}\n")
            f.write(f"TEL:{number}\n")
            f.write("END:VCARD\n")
            if i % 100_000 == 0 and i > 0:
                print(f"  {prefix}: {i:,} numbers written...")
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    print(f"✔ {prefix} completed -> {filename} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    prefixes = [
        "0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919",
        "0990", "0991", "0992", "0993", "0994",
        "0930", "0933", "0935", "0936", "0937", "0938", "0939",
        "0901", "0902", "0903", "0904", "0905",
        "0920", "0921", "0922"
    ]

    if len(sys.argv) > 1:
        selected = sys.argv[1]
        if selected in prefixes:
            generate_vcf(selected)
        else:
            print(f"Prefix {selected} is not in the list.")
    else:
        print("Starting generation for all prefixes...")
        for p in prefixes:
            generate_vcf(p)
        print("All done!")