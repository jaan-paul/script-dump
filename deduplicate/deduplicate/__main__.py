import yaspin
from yaspin import spinners
from . import find_duplicates, command_line


def main() -> None:
    args = command_line.parse_args()

    with yaspin.yaspin(spinners.Spinners.noise, text="finding duplicates"):
        duplicate_groups = find_duplicates(args.dir_path)

    if not duplicate_groups:
        print("no duplicates")

    if not args.keep_filter:
        command_line.interactive_delete(duplicate_groups)
    else:
        command_line.automatic_delete(duplicate_groups, args.keep_filter)


if __name__ == "__main__":
    main()