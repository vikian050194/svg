## File

Configuration is loaded from `yaml` or `yml` file.

Configuration file is provided to CLI application as first argument:

```
python3 app.py config.yaml
```

`config.yaml` is default configuration file name.

## Scheme

For now there is no validation scheme.

## Top level

There are few top level options that should be specisied.

| Name | Value limitations | Default value | Description |
|:---|:---|:---|:---|
| width | integer or float | `1024` | as-is |
| height | integer or float | `1024` | as-is |
| palette | `dell`, `docker`, `google`, `gravit`, `ikea`, `microsoft`, `polaroid`, `youtube`, `blue`, `violet`, `red`, `orange`, `cyan`, `yellow`, `pink`, `green`, `gray`, `linkedine` | `linkedine` |predefined palette name |
| order | `forward`, `backward`, `mono`, `random` | `forward` | palette contains few colors that could be used in the different order |
| patterns | * | all patterns examples | list of patterns |

## Patterns

Each pattern has at least one required "option" - `name`;
