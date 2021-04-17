#!/bin/sh
cd /home/ubuntu/Desktop/dailylogs
git add .
echo "added"
git commit -m "Updates for $(date +%F)"
echo "comitted"
git push  
echo "pushed"
        