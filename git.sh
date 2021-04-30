#!/bin/sh
cd /home/divya/tact/Dailylogs
git add .
echo "added"
git commit -m "Updates for $(date +%F)"
echo "comitted"
git push  
echo "pushed"
        