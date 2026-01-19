def read_file(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found!")