#cd ~/anaconda3/envs/superset3.4/lib/python3.4/site-packages/superset_bak
#!/bin/bash

mv config.py config.py_bak
mv magic.py magic.py_bak

find . -name '*.py' -delete

mv config.py_bak config.py
mv magic.py_bak magic.py

python magic.py

echo "All has done!"