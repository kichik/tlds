#!/usr/bin/env bash

set -eux

./build.py

if [ -z "$(git diff --exit-code)" ]; then
    echo "No changes to the output on this push; exiting."
    exit 0
fi

find .

export VERSION=$(cat version)

export GIT_AUTHOR_NAME="Github update bot"
export GIT_AUTHOR_EMAIL="git@github.com"
export GIT_COMMITTER_NAME=$GIT_AUTHOR_NAME
export GIT_COMMITTER_EMAIL=$GIT_AUTHOR_EMAIL

git add tlds/_data.py version

git commit -m "Update IANA top-level domains to $VERSION"
git tag --annotate --message="Release $VERSION" $VERSION
git push origin HEAD:master $VERSION
