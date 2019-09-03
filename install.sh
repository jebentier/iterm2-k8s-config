
#!/bin/bash

set -e

iterm_scripts_dir="$HOME/Library/Application Support/iTerm2/Scripts"
autolaunch_dir="$iterm_scripts_dir/AutoLaunch"

mkdir -p "$autolaunch_dir"

echo Linking main.py to AutoLaunch folder $autolaunch_dir
ln -si main.py "$autolaunch_dir/iterm2-k8s-config.py"
