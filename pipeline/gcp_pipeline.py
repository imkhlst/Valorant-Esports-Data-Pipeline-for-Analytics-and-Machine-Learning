import argparse
from utils.gcp_utils import *

def main():    
    parser = argparse.ArgumentParser(description="Pipeline multi-environment.")

    parser.add_argument("--ci", action="store_true", help="CI mode activated")
    parser.add_argument("--dev", action="store_true", help="Development mode activated")
    parser.add_argument("--prod", action="store_true", help="Production mode activated")

    args = parser.parse_args()
    
    create_bucket()
    create_dataset()
    upload_data()

    if args.dev:
        load_table(dataset_name="dev")
        merge_table(dataset_name="dev")
    elif args.ci:
        load_table(dataset_name="ci")
        merge_table(dataset_name="ci")
    elif args.prod:
        load_table(dataset_name="prod")
        merge_table(dataset_name="prod")

if __name__ == "__main__":
    main()