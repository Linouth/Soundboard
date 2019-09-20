#!/bin/bash
while inotifywait -r -e close_write ./; do
    sassc --style compact style.sass style.css
done
