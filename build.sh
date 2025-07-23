#!/bin/sh
set -eu

PROJ=${PROJ:-/workspaces/renpay-template}
SDK_DIR=${SDK_DIR:-/opt/renpy}
PACKAGES=${PACKAGES:-"windows linux mac"}   # 空白区切りで列挙
SRC_BASE=${SRC_BASE:-/workspaces}
DEST=${DEST:-/workspaces/renpay-template}

RENpy="$SDK_DIR/renpy.sh"

log () { echo "$(date '+%F %T') $*"; }

log "=== Ren'Py distribute start ==="
log "SDK_DIR=$SDK_DIR  PROJ=$PROJ  PACKAGES=$PACKAGES"

# --package を繰り返し展開
PKG_ARGS=""
for p in $PACKAGES; do
  PKG_ARGS="$PKG_ARGS --package $p"
done

OLDPWD=$(pwd)
cd "$SDK_DIR"
log "Running: $RENpy launcher distribute \"$PROJ\" $PKG_ARGS"
# shellcheck disable=SC2086
"$RENpy" launcher distribute "$PROJ" $PKG_ARGS
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
