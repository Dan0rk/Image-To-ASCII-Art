import unicodedata

def generate_common_utf8_list():
    
    common_chars = []
    start = 500 # After testing found that looks best when skipping first few characters
    for codepoint in range(start, start + 500):
        try:
            char = chr(codepoint)

            if unicodedata.category(char)[0] != "C":
                common_chars.append(char)
        except ValueError:
            continue

    formatted_list = "[\n  " + ", ".join(f'"{char}"' for char in common_chars) + "\n]"
    return formatted_list


formatted_utf8_list = generate_common_utf8_list()

output_file = "utf-8_chars.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_utf8_list)

print(f"List written to {output_file}")
