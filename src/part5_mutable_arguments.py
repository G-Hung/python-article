def process_data(files: list = None):
    files = files or ["part1", "part2", "part3"]
    print(f"1st batch, process: {[file for file in files]}")
    # we swap the data and continue to process
    files[0], files[1], files[2] = "part4", "part5", "part6"
    print(f"2nd batch, process: {[file for file in files]}")


if __name__ == "__main__":
    process_data()
    process_data()
