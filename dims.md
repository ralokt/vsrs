
# Dimensions

Dimensions are specified in (subclasses of) `VsScaleDimsCalculator`.

They are (absolute or relative) pixel amounts used for skin and UI elements, and always specified as one-line methods returning an integer.

They make use of the following infrastructure:
- `square_size`, the current pixel dimension of squares
- `_scale`, see below

## `_scale`

`_scale` is a helper function used to scale dimensions.

It scales relative to a base square size of `16` by
- multiplying by `square_size`
- performing integer division by `16`
- rounding by increasing by 1 if the modulus was greater than or equal to `8`

This is done in order to not touch floats and be fully deterministic.

Some dimensions may not scale 1:1 with their 16px counterpart even using `_scale`. For example, the counter width ends up being the sum of 4 scaled paddings and 3 scaled numbers to ensure that there CAN be a consistent padding.

## Nomenclature

Dimension names follow the following scheme:

```
<item>_<unit-suffix>[_n]
```

If a `_n` suffix is present, the method takes an `unsigned int` parameter to choose one of `n` positions, for handling digits in the skin. Otherwise, dimensions take no parameters.

### `unit-suffix`

A `unit-suffix` describes the meaning of a dimension - absolute vs relative, coordinates vs offsets, etc. The distance unit is still always the pixel.

### `item`

An `item` is a UI and/or skin element. As an example for something that is both, `sml` is the smilie in both the skin and the UI.

## Definitions

### Unit suffixes

#### List of unit suffixes

- `w` - an absolute width
- `h` - an absolute height
- `d` - an absolute width and height, for square elements
- `x` - an absolute x position in the skin
- `y` - an absolute y position in the skin
- `p` - padding (see below)

##### Paddings

Paddings are currently only used for the counter, and facilitate a hack used to deal with a discrepancy between MSX and vsweep.

MSX skins contain counter numbers with no padding. vsweep adds a pixel on each side.

Note that to be consistent, digits still need to be the whole padding apart. Also, the whole padding is scaled to generate the counter dimension, so the components need to be defined in terms of the total padding.

### Items

#### MSX UI edge pseudoitems

MSX UI edge items are pseudoitems in that they don't describe a specific UI item, but a row or column of them. Combining a row and a column pseudoitem describes a concrete item.

This is because in skins, the edges and corners are laid out in a table, like so:

```
     uil uim uir
uit   +  ---  +
uite  |       |
uim   +  ---  +
uibe  |       |
uib   +  ---  +
```

The upper void between `uim` and `uite` contains the counters and smilie, the lower void between `uim` and `uibe` contains the board.

The names consist of a `ui` prefix and
- `l` - left
- `m` - middle (overloaded, see below)
- `r` - right
- `t` - top
- `te` - top edge
- `be` - bottom edge
- `b` - bottom

`uim` is overloaded, but made unambiguous by the unit suffix.

For example, to get the bar between top bar and board, one would extract the rect `(uim_x, uim_y, uim_w, uim_h)` from the skin, and for the edge/T-corner to the right of it, it would be `(uir_x, uim_y, uir_w, uim_h)`.

#### List of items

- `rd` - red digit
- `rds` - red digit (small)
- `cr` - counter
- `sml` - smilie
- `bg` - background color pixel in skin
- `skin` - the entire base skin (MSX compatible)
- `brd` - board
- `sq` - square
- `sq2` - second row of squares in skin file
- `ui*` - see above
- `vcrre` - vsweep's right counter with tenths (extended skin only)
- `vcrrt` - the tenths digit of the right counter (extended skin only)
- `vcn` - vsweep's closed numbers (extended skin only)
- `vsmle` - vsweep's smilie (extended skin only)
- `vskin` - the entire extended skin, including vsweep-specific features

### Dimension classes and their usage

#### `VsScaleDimsCalculator`

Basic definitions that are needed both for reading a skin and constructing the UI.

#### `VsSkinOffsetCalculator`

Definitions specific to skins, mostly absolute positions of skin elements.
