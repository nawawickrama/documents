#!/bin/bash
# Sets up the projects on a new Mac after the Documents repo is cloned into ~/Documents.
# Run it from anywhere:  bash ~/Documents/setup-new-mac.sh
# It only clones code repos that are missing and installs their packages. It never deletes anything.
set -u
D="$HOME/Documents"

clone() { # folder, repo
  if [ -d "$D/$1/.git" ]; then echo "already there: $1"; return; fi
  if [ -e "$D/$1" ] && [ -n "$(ls -A "$D/$1" 2>/dev/null)" ]; then echo "SKIPPED (folder not empty): $1"; return; fi
  echo "cloning $2 -> $1"
  git clone "git@github.com:$2.git" "$D/$1"
}

clone "Coredile/Coredile website"               Coredile-com/website
clone "Coredile/Content automation"             Coredile-com/content-automation
clone "Coredile/Coredile POS/Source code"       Coredile-com/pos
clone "Coredile/Coredile POS/Website"           Coredile-com/pos-website
clone "Coredile/Coredile POS/Video studio"      Coredile-com/pos-videos-
clone "Coredile/Let's Ride/Source code/backend"  Let-s-Ride/backend
clone "Coredile/Let's Ride/Source code/frontend" Let-s-Ride/frontend
clone "Coredile/Let's Ride/Source code/admin"    Let-s-Ride/admin
clone "Coredile/Let's Ride/Source code/landing"  Let-s-Ride/landing
clone "Coredile/Let's Ride/Source code/mobile"   Let-s-Ride/mobile
clone "Coredile/Let's Ride/Video studio"         Let-s-Ride/video-studio
clone "YouTube/Studio"                           nawawickrama/terrachart-studio

echo "--- installing packages (skips folders that already have node_modules)"
for p in "Coredile/Coredile website" "Coredile/Content automation" "Coredile/Coredile POS/Website" \
         "Coredile/Coredile POS/Video studio" "Coredile/Let's Ride/Video studio" "YouTube/Studio" \
         "Coredile/Let's Ride/Source code/frontend" "Coredile/Let's Ride/Source code/admin" "Coredile/Let's Ride/Source code/landing"; do
  [ -f "$D/$p/package.json" ] && [ ! -d "$D/$p/node_modules" ] && (cd "$D/$p" && echo "npm install: $p" && npm install --no-audit --no-fund)
done
[ -d "$D/Coredile/Coredile POS/Source code" ] && [ ! -d "$D/Coredile/Coredile POS/Source code/node_modules" ] && \
  (cd "$D/Coredile/Coredile POS/Source code" && echo "pnpm install: POS" && pnpm install)
for p in "Coredile/Coredile POS/Source code/backend" "Coredile/Let's Ride/Source code/backend"; do
  [ -f "$D/$p/composer.json" ] && [ ! -d "$D/$p/vendor" ] && (cd "$D/$p" && echo "composer install: $p" && composer install)
done
[ -d "$D/Coredile/Let's Ride/Source code/mobile" ] && (cd "$D/Coredile/Let's Ride/Source code/mobile" && flutter pub get)

echo "--- YouTube rules shortcut"
mkdir -p "$HOME/.claude/skills"
[ -e "$HOME/.claude/skills/youtube-channel-compliance" ] || ln -s "$D/YouTube/Guidelines" "$HOME/.claude/skills/youtube-channel-compliance"

echo "Done. Next steps by hand are in README.md, 'Setting up a new computer'."
