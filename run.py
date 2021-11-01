import argparse
import extract


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="File of URLs to be analyzed")
    parser.add_argument("output", help="Output File")
    args = parser.parse_args()

    if args.input and args.output:
        # Starts extraction
        #print('Starts extraction...')
        extract.main(args.input, args.output)

if __name__ == "__main__":
    main()
