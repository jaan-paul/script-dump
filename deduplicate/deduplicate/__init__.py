if __name__ == "__main__":
    import sys
    from . import cli

    cli.execute(sys.argv)
else:
    from .duplicate import find_duplicates
    from .delete import delete_duplicates
    from . import keep, fileinfo
