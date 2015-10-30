#!/usr/bin/env bash
pandoc markdown/exacloud-tutorial.md -f markdown -t latex -s -o markdown/exacloud-tutorial.pdf
cp scripts/* exacloudTutorial/
cp markdown/exacloud-tutorial.* exacloudTutorial/
cp data/fulldata.csv exacloudTutorial/
cp data/test.csv exacloudTutorial/
tar -cvzf exacloudTutorial.tar.gz exacloudTutorial/
