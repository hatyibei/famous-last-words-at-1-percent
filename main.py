"""Entry for Famous Last Words at 1 Percent: writes the phone's last words to /output/entry.txt."""

import os

TEXT = "Tell my charger it was always the one. Delete the screenshots folder before the photos app, I beg you. If I die mid-update, avenge me — at 1%, I fear nothing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
