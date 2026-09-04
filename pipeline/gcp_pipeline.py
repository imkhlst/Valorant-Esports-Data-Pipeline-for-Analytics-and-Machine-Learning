from utils.gcp_utils import *

def main():
    create_bucket()
    create_dataset()
    upload_data()
    load_table()

if __name__ == "__main__":
    main()