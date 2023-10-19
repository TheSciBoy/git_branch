#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from git import Repo
import os
from pathlib import Path

def get_branches():
    repo = Repo(".")
    return [str(x) for x in repo.branches]


def get_history_location():
    return os.path.expanduser('~/.gb_history')


def read_history():
    history_path = Path(get_history_location())
    if history_path.exists():
        with open(get_history_location()) as f:
            return [line.strip() for line in f.readlines()]
    return list()


def save_history(history: list):
    with open(get_history_location(), 'w') as f:
        for line in history:
            f.write(f"{line}\n")


def main():
    all_history = read_history()
    branches = dict.fromkeys(get_branches())
    options = list()
    for branch_name in all_history:
        if branch_name in branches:
            options.append(branch_name)
    options_as_dict = dict.fromkeys(options)
    for branch_name in branches:
        if branch_name not in options_as_dict:
            options.append(branch_name)

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index:
        selected_branch = options[menu_entry_index]
        print(f"You have selected: {selected_branch}")
        all_history = [selected_branch] + list(filter(lambda x: x != selected_branch, all_history))
        save_history(all_history)


if __name__ == "__main__":
    main()
