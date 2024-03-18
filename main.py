"""Main loop."""

from WarehouseSystem.userInteraction.menu import TerminalMenu


def main() -> None:
    """Run the main loop."""
    menu = TerminalMenu()
    menu.run()


if __name__ == "__main__":
    main()
