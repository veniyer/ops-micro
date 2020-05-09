#!/bin/sh
workingdir=$1
app=$2
fn=$3

cd $workingdir && fn create app $app && fn -v build && fn deploy --app $app --local

echo "http://localhost:8080/invoke/"$(fn inspect function $app $(fn list functions $app --output json | jq -r '.[].name') | jq -r '.id')