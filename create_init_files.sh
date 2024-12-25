#!/usr/bin/env bash
#
# create_init_files.sh
# Recursively scan all subdirectories from a specified base path,
# and create an empty __init__.py in each directory that doesn't have one.

# If the user provided a path as an argument, use that. Otherwise, use current dir.
BASE_DIR="${1:-.}"

echo "Creating __init__.py files in all directories under: $BASE_DIR"

# Find every directory inside BASE_DIR (including BASE_DIR itself),
# then check if __init__.py exists. If not, create it.
while IFS= read -r -d '' DIR; do
  INIT_FILE="$DIR/__init__.py"
  if [ ! -f "$INIT_FILE" ]; then
    touch "$INIT_FILE"
    echo "  Created: $INIT_FILE"
  fi
done < <(find "$BASE_DIR" -type d -print0)

echo "Done!"

