import fiftyone as fo
import argparse
import os

def main(args: argparse.Namespace):
    dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    dataset_dir=os.path.join(args.path, "val" if args.val else "train")
    )

    session = fo.launch_app(dataset)
    session.wait()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script to show lpd dataset in the fiftyone")
    parser.add_argument('-p', '--path', help="Path to folder with dataset")
    parser.add_argument('-v', '--val', action="store_true", help="Path to folder with dataset")

    args, unknown = parser.parse_known_args()

    main(args)