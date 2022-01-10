python libraries/python/setup.py sdist
rm -rf libraries/python/oodf.egg-info
twine upload libraries/python/dist/*
rm -rf libraries/python/dist
