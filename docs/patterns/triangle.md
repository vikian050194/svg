## Triangle

### Description

Just triangles.

### Options

| Name | Value limitations | Default value | Description |
|:---|:---|:---|:---|
| count | integer equal or greater 1 | no | count of triangles |
| type | `random`, `equilateral` | no | type of triangles |
| radius | integer | no | radius of circumscribed circle |

### Example

**random**

```
name: triangle
type: random
count: 1
```

**equilateral with specific size**

```
name: triangle
type: equilateral
count: 1
radius: 128
```