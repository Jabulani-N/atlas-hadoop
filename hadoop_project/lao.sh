#!/usr/bin/env bash

curl -o lao.txt https://raw.githubusercontent.com/Jabulani-N/atlas-hadoop/refs/heads/main/hadoop_project/assignment_files/lao.txt
hdfs dfs -put lao.txt /holbies/input
rm lao.txt
