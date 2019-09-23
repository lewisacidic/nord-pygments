# nord-pygments
A [nord](https://www.nordtheme.com/)-inspired style for pygments.

## Installing

With `pip`:

```sh
pip install nord-pygments
```

With `conda`:

```shell
conda install -c lewisacidic nord-pygments
```

## Usage

Within Python:

```python
from nord_pygments import Nord

...
```

Or using the pygments API:

```python
>>> from pygments.styles import get_style_by_name
>>> get_style_by_name("nord")
<class 'nord_pygments.Nord'>

```

