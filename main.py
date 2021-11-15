import database

lines = []
def main():
    while True:
        line = input()
        if line:
            lines.append(line)
            if line.upper() == 'END':
                break
        else:
            break

    if len(lines) < 1:
        print("No operations found")
        return

    database.run_database(lines)

if __name__ == "__main__":
    main()