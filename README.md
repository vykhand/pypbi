# Unofficial Python wrapper for PowerBI RestAPI

Important note: this software comes with no warranty and provided as is.

## Intro

This is an unofficial python wrapper around [PowerBI rest API][1]

It only wraps those functions that I needed for my projects

If you are missing something in this project, you are free to do a pull request or to demand your money back :)

## Usage

```
from pypbi.core import PowerBI
p = PowerBI(<user>, <password>, <client_id>)
p.connect()

# Get workspaces list
workspaces = p.get_workspaces()
print([str(i) for i in workspaces])

#Get data set

datasets = workspaces[0].get_datasets()


```

[1]: https://msdn.microsoft.com/en-us/library/mt147898.aspx