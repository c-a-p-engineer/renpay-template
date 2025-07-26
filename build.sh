#!/bin/sh
set -eu

# Windows (Cygwin/MSYS/MinGW)上での実行を抑止
if uname | grep -qE "CYGWIN_NT|MINGW(32|64)_NT|MSYS_NT"; then
  echo "Error: This script cannot be run on Windows because it cannot handle the permissions of the Linux/Mac distributions." >&2
  echo "Please run this in a Dev Container." >&2
  exit 1
fi

PROJ=${PROJ:-/workspaces/renpay-template}
SDK_DIR=${SDK_DIR:-/opt/renpy}
PACKAGES=${PACKAGES:-"windows linux mac"}   # 空白区切りで列挙
SRC_BASE=${SRC_BASE:-/workspaces}
DEST=${DEST:-/workspaces/renpay-template}

RENpy="$SDK_DIR/renpy.sh"

log () { echo "$(date '+%F %T') $*"; }

log "=== Ren'Py distribute start ==="
log "SDK_DIR=$SDK_DIR  PROJ=$PROJ  PACKAGES=$PACKAGES"

OLDPWD=$(pwd)
cd "$SDK_DIR"

# --package 引数を組み立て
set --
for p in $PACKAGES; do
  set -- "$@" --package "$p"
done

log "Running: $RENpy launcher distribute \"$PROJ\" $*"
"$RENpy" launcher distribute "$PROJ" "$@"
cd "$OLDPWD"
log "Distribute finished."

# *-dists の移動
for d in "$SRC_BASE"/*-dists; do
  [ -d "$d" ] || continue
  base=$(basename "$d")
  target="$DEST/$base"
  if [ -e "$target" ]; then
    log "Existing directory found: $target -> removing"
    rm -rf "$target"
  fi
  log "Moving $d -> $DEST/"
  mv "$d" "$DEST"/
done

log "=== Done ==="
