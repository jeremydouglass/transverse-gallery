#!/usr/bin/env bash

bundle exec jekyll build --config _config-travis.yml --incremental --verbose
htmlproofer ./_site --disable-external
