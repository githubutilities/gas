#!/usr/bin/env bash

cd "$(dirname "${BASH_SOURCE}")";

curl -# -C - -LO https://raw.githubusercontent.com/skydark/nstools/master/zhtools/zh_wiki.py
cat >> zh_wiki.py <<EOF
# Referece
#* https://github.com/skydark/nstools
EOF

curl -# -C - -LO https://raw.githubusercontent.com/skydark/nstools/master/zhtools/langconv.py
cat >> langconv.py <<EOF
# Referece
#* https://github.com/skydark/nstools
EOF
