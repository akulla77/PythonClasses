import argparse

from pathlib import Path

from commands import AbstractCommand, CommandFactory
from notes.Storage import DatabaseStorage


if __name__ == '__main__':
    factory = CommandFactory(DatabaseStorage(Path('notes.db')))

    parser = argparse.ArgumentParser(
        description='Console app with sub-commands.'
    )

    subparsers = parser.add_subparsers(title='commands', dest='command')

    for command in factory.commands:
        command_parser = subparsers.add_parser(command.name, help=command.help)

        for argument in command.arguments:
            command_parser.add_argument(argument)

    options: dict = vars(parser.parse_args())

    command: AbstractCommand = factory.get_command(options['command'])

    if command:
        command.execute(options)
    else:
        parser.print_help()
