#файл с пустыми строками
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Привет\n\n\n\nпока\n\n13243\n")



with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()


non_empty_lines = [line for line in lines if line.strip()]


with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(non_empty_lines)

print("Пустые строки были удалены и сохранены в 'output.txt'.")