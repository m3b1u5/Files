# ДЗ: Работа с файлами

def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


def main():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
            print(content + '\n')
        with open('data.txt', 'a') as file:
            file.write("\n\n William Shakespeare's play Hamlet (Act 3, Scene 1)")
        for line in read_lines('data.txt'):
            print(line.strip())

        with open('data.txt', 'rb') as file_in, open('data_copy.txt', 'wb') as file_out:
            file_out.write(file_in.read())

    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет прав доступа к файлу.")


if __name__ == '__main__':
    main()
