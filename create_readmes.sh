#!/usr/bin/env bash
#
# create_readmes.sh
# Recursively scan all subdirectories from a specified base path,
# and create a simple README.md in each directory if one doesn't exist.

# If the user provided a path as an argument, use that. Otherwise, use current dir.
BASE_DIR="${1:-.}"

echo "Creating README.md in all directories under: $BASE_DIR"

while IFS= read -r -d '' DIR; do
  README_FILE="$DIR/README.md"
  
  if [ ! -f "$README_FILE" ]; then
    # Simple text in each README
    echo "## $(basename "$DIR")" > "$README_FILE"
    echo "This directory contains Python scripts." >> "$README_FILE"
    
    echo "Created: $README_FILE"
  fi
done < <(find "$BASE_DIR" -type d -print0)

echo "Done!"

