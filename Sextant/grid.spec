
[spec]

; Format and options of this spec file:
options = "Freeciv-2.6-spec Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Jason Dorje Short <jdorje@freeciv.org>
"

[file]
gfx = "Sextant/grid"

[grid_main]

x_top_left = 2
y_top_left = 2
dx = 60
dy = 60
pixel_border = 2

tiles = { "row", "column", "tag"
  0, 0, "grid.main.we"
  1, 0, "grid.main.ns"
  0, 1, "grid.city.we"
  1, 1, "grid.city.ns"
  0, 2, "grid.worked.we"
  1, 2, "grid.worked.ns"
  0, 3, "grid.unavailable"
  1, 3, "grid.nonnative"
  0, 4, "grid.selected.we"
  1, 4, "grid.selected.ns"
  0, 5, "grid.coastline.we"
  1, 5, "grid.coastline.ns"

  2, 0, "grid.borders.n"
  2, 1, "grid.borders.s"
  2, 2, "grid.borders.w"
  2, 3, "grid.borders.e"
}
