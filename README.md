# Yaml Config Merger

A simple python3 library to merge yaml configs.

# requirements

* python >= 3.8

# install

install after cloning source code
```sh
pip install .
```

or, install from github
```sh
pip install -U git+https://github.com/Gavin1937/yaml_config_merger.git
```

# usage

```python
from yaml_config_merge import *

parent_config = load_config('/path/to/parent_config.yaml')
child_config = load_config('/path/to/child_config.yaml')
# use child_config to update parent_config
parent_config = merge_config(parent_config, child_config)

child_config_2 = {'hello':'world', 'list':[1,2,3], 'num':3.14, 'bool':False}
# use parent_config to update child_config_2
parent_config = merge_config(child_config_2, parent_config)

dump_config('/path/to/new_config.yaml', parent_config, ensure_ascii=False, indent=4)
```