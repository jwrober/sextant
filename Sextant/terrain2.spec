
[spec]

; Format and options of this spec file:
options = "Freeciv-2.6-spec Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi> [TR]
    GriffonSpade [GS]
"

[file]
gfx = "Sextant/terrain2"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 30
dy = 30
pixel_border = 1

tiles = {"row", "column", "tag"

; Shallow Ocean base layer

; [TR][GS]
  0,  0, "t.l0.coast_cell_u000"
  0,  0, "t.l0.coast_cell_u100"
  0,  0, "t.l0.coast_cell_u001"
  0,  0, "t.l0.coast_cell_u101"
  0,  0, "t.l0.coast_cell_r000"
  0,  0, "t.l0.coast_cell_r100"
  0,  0, "t.l0.coast_cell_r001"
  0,  0, "t.l0.coast_cell_r101"
  0,  0, "t.l0.coast_cell_l000"
  0,  0, "t.l0.coast_cell_l100"
  0,  0, "t.l0.coast_cell_l001"
  0,  0, "t.l0.coast_cell_l101"
  0,  0, "t.l0.coast_cell_d000"
  0,  0, "t.l0.coast_cell_d100"
  0,  0, "t.l0.coast_cell_d001"
  0,  0, "t.l0.coast_cell_d101"

  0,  1, "t.l0.coast_cell_u010"
  0,  1, "t.l0.coast_cell_u110"
  0,  1, "t.l0.coast_cell_u011"
  0,  1, "t.l0.coast_cell_u111"

  0,  2, "t.l0.coast_cell_r010"
  0,  2, "t.l0.coast_cell_r110"
  0,  2, "t.l0.coast_cell_r011"
  0,  2, "t.l0.coast_cell_r111"

  0,  3, "t.l0.coast_cell_l010"
  0,  3, "t.l0.coast_cell_l110"
  0,  3, "t.l0.coast_cell_l011"
  0,  3, "t.l0.coast_cell_l111"

  0,  4, "t.l0.coast_cell_d010"
  0,  4, "t.l0.coast_cell_d110"
  0,  4, "t.l0.coast_cell_d011"
  0,  4, "t.l0.coast_cell_d111"

; Deep Ocean base layer

; [TR][GS]
  0,  5, "t.l0.floor_cell_u000"
  0,  5, "t.l0.floor_cell_u100"
  0,  5, "t.l0.floor_cell_u001"
  0,  5, "t.l0.floor_cell_u101"
  0,  5, "t.l0.floor_cell_r000"
  0,  5, "t.l0.floor_cell_r100"
  0,  5, "t.l0.floor_cell_r001"
  0,  5, "t.l0.floor_cell_r101"
  0,  5, "t.l0.floor_cell_l000"
  0,  5, "t.l0.floor_cell_l100"
  0,  5, "t.l0.floor_cell_l001"
  0,  5, "t.l0.floor_cell_l101"
  0,  5, "t.l0.floor_cell_d000"
  0,  5, "t.l0.floor_cell_d100"
  0,  5, "t.l0.floor_cell_d001"
  0,  5, "t.l0.floor_cell_d101"

  0,  6, "t.l0.floor_cell_u010"
  0,  6, "t.l0.floor_cell_u110"
  0,  6, "t.l0.floor_cell_u011"
  0,  6, "t.l0.floor_cell_u111"

  0,  7, "t.l0.floor_cell_r010"
  0,  7, "t.l0.floor_cell_r110"
  0,  7, "t.l0.floor_cell_r011"
  0,  7, "t.l0.floor_cell_r111"

  0,  8, "t.l0.floor_cell_l010"
  0,  8, "t.l0.floor_cell_l110"
  0,  8, "t.l0.floor_cell_l011"
  0,  8, "t.l0.floor_cell_l111"

  0,  9, "t.l0.floor_cell_d010"
  0,  9, "t.l0.floor_cell_d110"
  0,  9, "t.l0.floor_cell_d011"
  0,  9, "t.l0.floor_cell_d111"

; Lake base layer

; [TR][GS]
  0, 10, "t.l0.lake_cell_u000"
  0, 10, "t.l0.lake_cell_u100"
  0, 10, "t.l0.lake_cell_u001"
  0, 10, "t.l0.lake_cell_u101"
  0, 10, "t.l0.lake_cell_r000"
  0, 10, "t.l0.lake_cell_r100"
  0, 10, "t.l0.lake_cell_r001"
  0, 10, "t.l0.lake_cell_r101"
  0, 10, "t.l0.lake_cell_l000"
  0, 10, "t.l0.lake_cell_l100"
  0, 10, "t.l0.lake_cell_l001"
  0, 10, "t.l0.lake_cell_l101"
  0, 10, "t.l0.lake_cell_d000"
  0, 10, "t.l0.lake_cell_d100"
  0, 10, "t.l0.lake_cell_d001"
  0, 10, "t.l0.lake_cell_d101"

  0, 11, "t.l0.lake_cell_u010"
  0, 11, "t.l0.lake_cell_u110"
  0, 11, "t.l0.lake_cell_u011"
  0, 11, "t.l0.lake_cell_u111"

  0, 12, "t.l0.lake_cell_r010"
  0, 12, "t.l0.lake_cell_r110"
  0, 12, "t.l0.lake_cell_r011"
  0, 12, "t.l0.lake_cell_r111"

  0, 13, "t.l0.lake_cell_l010"
  0, 13, "t.l0.lake_cell_l110"
  0, 13, "t.l0.lake_cell_l011"
  0, 13, "t.l0.lake_cell_l111"

  0, 14, "t.l0.lake_cell_d010"
  0, 14, "t.l0.lake_cell_d110"
  0, 14, "t.l0.lake_cell_d011"
  0, 14, "t.l0.lake_cell_d111"

 ; Inaccessible Ocean base layer
 
; [TR][GS]
  0, 15, "t.l0.inaccessible_cell_u000"
  0, 15, "t.l0.inaccessible_cell_u100"
  0, 15, "t.l0.inaccessible_cell_u001"
  0, 15, "t.l0.inaccessible_cell_u101"
  0, 15, "t.l0.inaccessible_cell_r000"
  0, 15, "t.l0.inaccessible_cell_r100"
  0, 15, "t.l0.inaccessible_cell_r001"
  0, 15, "t.l0.inaccessible_cell_r101"
  0, 15, "t.l0.inaccessible_cell_l000"
  0, 15, "t.l0.inaccessible_cell_l100"
  0, 15, "t.l0.inaccessible_cell_l001"
  0, 15, "t.l0.inaccessible_cell_l101"
  0, 15, "t.l0.inaccessible_cell_d000"
  0, 15, "t.l0.inaccessible_cell_d100"
  0, 15, "t.l0.inaccessible_cell_d001"
  0, 15, "t.l0.inaccessible_cell_d101"


  0, 16, "t.l0.inaccessible_cell_u010"
  0, 16, "t.l0.inaccessible_cell_u110"
  0, 16, "t.l0.inaccessible_cell_u011"
  0, 16, "t.l0.inaccessible_cell_u111"

  0, 17, "t.l0.inaccessible_cell_r010"
  0, 17, "t.l0.inaccessible_cell_r110"
  0, 17, "t.l0.inaccessible_cell_r011"
  0, 17, "t.l0.inaccessible_cell_r111"


  0, 18, "t.l0.inaccessible_cell_l010"
  0, 18, "t.l0.inaccessible_cell_l110"
  0, 18, "t.l0.inaccessible_cell_l011"
  0, 18, "t.l0.inaccessible_cell_l111"

  0, 19, "t.l0.inaccessible_cell_d010"
  0, 19, "t.l0.inaccessible_cell_d110"
  0, 19, "t.l0.inaccessible_cell_d011"
  0, 19, "t.l0.inaccessible_cell_d111"

 ; Jungle Terrain

; [TR][GS]
  0, 20, "t.l0.jungle_cell_r000"
  0, 20, "t.l0.jungle_cell_r010"
  0, 20, "t.l0.jungle_cell_d000"
  0, 20, "t.l0.jungle_cell_d010"
  0, 20, "t.l0.jungle_cell_l000"
  0, 20, "t.l0.jungle_cell_l010"
  0, 20, "t.l0.jungle_cell_u000"
  0, 20, "t.l0.jungle_cell_u010"
  0, 21, "t.l0.jungle_cell_r100"
  0, 21, "t.l0.jungle_cell_r110"
  0, 21, "t.l0.jungle_cell_u001"
  0, 21, "t.l0.jungle_cell_u011"
  0, 22, "t.l0.jungle_cell_r001"
  0, 22, "t.l0.jungle_cell_r011"
  0, 22, "t.l0.jungle_cell_d100"
  0, 22, "t.l0.jungle_cell_d110"
  0, 23, "t.l0.jungle_cell_r101"
  0, 23, "t.l0.jungle_cell_r111"
  0, 24, "t.l0.jungle_cell_d001"
  0, 24, "t.l0.jungle_cell_d011"
  0, 24, "t.l0.jungle_cell_l100"
  0, 24, "t.l0.jungle_cell_l110"
  0, 25, "t.l0.jungle_cell_d101"
  0, 25, "t.l0.jungle_cell_d111"
  0, 26, "t.l0.jungle_cell_l001"
  0, 26, "t.l0.jungle_cell_l011"
  0, 26, "t.l0.jungle_cell_u100"
  0, 26, "t.l0.jungle_cell_u110"
  0, 27, "t.l0.jungle_cell_l101"
  0, 27, "t.l0.jungle_cell_l111"
  0, 28, "t.l0.jungle_cell_u101"
  0, 28, "t.l0.jungle_cell_u111"

; Plains terrain


; [TR][GS]
  1,  0, "t.l0.plains_cell_r000"
  1,  0, "t.l0.plains_cell_r010"
  1,  0, "t.l0.plains_cell_d000"
  1,  0, "t.l0.plains_cell_d010"
  1,  0, "t.l0.plains_cell_l000"
  1,  0, "t.l0.plains_cell_l010"
  1,  0, "t.l0.plains_cell_u000"
  1,  0, "t.l0.plains_cell_u010"
  1,  1, "t.l0.plains_cell_r100"
  1,  1, "t.l0.plains_cell_r110"
  1,  2, "t.l0.plains_cell_r001"
  1,  2, "t.l0.plains_cell_r011"
  1,  3, "t.l0.plains_cell_r101"
  1,  3, "t.l0.plains_cell_r111"

  1,  4, "t.l0.plains_cell_d100"
  1,  4, "t.l0.plains_cell_d110"
  1,  5, "t.l0.plains_cell_d001"
  1,  5, "t.l0.plains_cell_d011"
  1,  6, "t.l0.plains_cell_d101"
  1,  6, "t.l0.plains_cell_d111"

  1,  7, "t.l0.plains_cell_l100"
  1,  7, "t.l0.plains_cell_l110"
  1,  8, "t.l0.plains_cell_l001"
  1,  8, "t.l0.plains_cell_l011"
  1,  9, "t.l0.plains_cell_l101"
  1,  9, "t.l0.plains_cell_l111"

  1,  10, "t.l0.plains_cell_u100"
  1,  10, "t.l0.plains_cell_u110"
  1,  11, "t.l0.plains_cell_u001"
  1,  11, "t.l0.plains_cell_u011"
  1,  12, "t.l0.plains_cell_u101"
  1,  12, "t.l0.plains_cell_u111"

; Desert Terrain

; [TR][GS]
  1, 13, "t.l0.desert_cell_r000"
  1, 13, "t.l0.desert_cell_r010"
  1, 13, "t.l0.desert_cell_d000"
  1, 13, "t.l0.desert_cell_d010"
  1, 13, "t.l0.desert_cell_l000"
  1, 13, "t.l0.desert_cell_l010"
  1, 13, "t.l0.desert_cell_u000"
  1, 13, "t.l0.desert_cell_u010"

  1, 14, "t.l0.desert_cell_r100"
  1, 14, "t.l0.desert_cell_r110"
  1, 15, "t.l0.desert_cell_r001"
  1, 15, "t.l0.desert_cell_r011"
  1, 16, "t.l0.desert_cell_r101"
  1, 16, "t.l0.desert_cell_r111"

  1, 17, "t.l0.desert_cell_d100"
  1, 17, "t.l0.desert_cell_d110"
  1, 18, "t.l0.desert_cell_d001"
  1, 18, "t.l0.desert_cell_d011"
  1, 19, "t.l0.desert_cell_d101"
  1, 19, "t.l0.desert_cell_d111"

  1, 20, "t.l0.desert_cell_l100"
  1, 20, "t.l0.desert_cell_l110"
  1, 21, "t.l0.desert_cell_l001"
  1, 21, "t.l0.desert_cell_l011"
  1, 22, "t.l0.desert_cell_l101"
  1, 22, "t.l0.desert_cell_l111"

  1,  23, "t.l0.desert_cell_u100"
  1,  23, "t.l0.desert_cell_u110"
  1,  24, "t.l0.desert_cell_u001"
  1,  24, "t.l0.desert_cell_u011"
  1,  25, "t.l0.desert_cell_u101"
  1,  25, "t.l0.desert_cell_u111"

; Swamp terrain

; [TR][GS]
  2,  0, "t.l0.swamp_cell_r000"
  2,  0, "t.l0.swamp_cell_r010"
  2,  0, "t.l0.swamp_cell_d000"
  2,  0, "t.l0.swamp_cell_d010"
  2,  0, "t.l0.swamp_cell_l000"
  2,  0, "t.l0.swamp_cell_l010"
  2,  0, "t.l0.swamp_cell_u000"
  2,  0, "t.l0.swamp_cell_u010"

  2,  1, "t.l0.swamp_cell_r100"
  2,  1, "t.l0.swamp_cell_r110"
  2,  2, "t.l0.swamp_cell_r001"
  2,  2, "t.l0.swamp_cell_r011"
  2,  3, "t.l0.swamp_cell_r101"
  2,  3, "t.l0.swamp_cell_r111"

  2,  4, "t.l0.swamp_cell_d100"
  2,  4, "t.l0.swamp_cell_d110"
  2,  5, "t.l0.swamp_cell_d001"
  2,  5, "t.l0.swamp_cell_d011"
  2,  6, "t.l0.swamp_cell_d101"
  2,  6, "t.l0.swamp_cell_d111"

  2,  7, "t.l0.swamp_cell_l100"
  2,  7, "t.l0.swamp_cell_l110"
  2,  8, "t.l0.swamp_cell_l001"
  2,  8, "t.l0.swamp_cell_l011"
  2,  9, "t.l0.swamp_cell_l101"
  2,  9, "t.l0.swamp_cell_l111"

  2,  10, "t.l0.swamp_cell_u100"
  2,  10, "t.l0.swamp_cell_u110"
  2,  11, "t.l0.swamp_cell_u001"
  2,  11, "t.l0.swamp_cell_u011"
  2,  12, "t.l0.swamp_cell_u101"
  2,  12, "t.l0.swamp_cell_u111"

; Tundra Terrain

; [TR][GS]
  2, 13, "t.l0.tundra_cell_r000"
  2, 13, "t.l0.tundra_cell_r010"
  2, 13, "t.l0.tundra_cell_d000"
  2, 13, "t.l0.tundra_cell_d010"
  2, 13, "t.l0.tundra_cell_l000"
  2, 13, "t.l0.tundra_cell_l010"
  2, 13, "t.l0.tundra_cell_u000"
  2, 13, "t.l0.tundra_cell_u010"
  
  2, 14, "t.l0.tundra_cell_r100"
  2, 14, "t.l0.tundra_cell_r110"
  2, 15, "t.l0.tundra_cell_r001"
  2, 15, "t.l0.tundra_cell_r011"
  2, 16, "t.l0.tundra_cell_r101"
  2, 16, "t.l0.tundra_cell_r111"

  2, 17, "t.l0.tundra_cell_d100"
  2, 17, "t.l0.tundra_cell_d110"
  2, 18, "t.l0.tundra_cell_d001"
  2, 18, "t.l0.tundra_cell_d011"
  2, 19, "t.l0.tundra_cell_d101"
  2, 19, "t.l0.tundra_cell_d111"

  2, 20, "t.l0.tundra_cell_l100"
  2, 20, "t.l0.tundra_cell_l110"
  2, 21, "t.l0.tundra_cell_l001"
  2, 21, "t.l0.tundra_cell_l011"
  2, 22, "t.l0.tundra_cell_l101"
  2, 22, "t.l0.tundra_cell_l111"

  2,  23, "t.l0.tundra_cell_u100"
  2,  23, "t.l0.tundra_cell_u110"
  2,  24, "t.l0.tundra_cell_u001"
  2,  24, "t.l0.tundra_cell_u011"
  2,  25, "t.l0.tundra_cell_u101"
  2,  25, "t.l0.tundra_cell_u111"

  2, 13, "t.l0.arctic_cell_r000"
  2, 13, "t.l0.arctic_cell_r010"
  2, 13, "t.l0.arctic_cell_d000"
  2, 13, "t.l0.arctic_cell_d010"
  2, 13, "t.l0.arctic_cell_l000"
  2, 13, "t.l0.arctic_cell_l010"
  2, 13, "t.l0.arctic_cell_u000"
  2, 13, "t.l0.arctic_cell_u010"

  2, 14, "t.l0.arctic_cell_r100"
  2, 14, "t.l0.arctic_cell_r110"
  2, 15, "t.l0.arctic_cell_r001"
  2, 15, "t.l0.arctic_cell_r011"
  2, 16, "t.l0.arctic_cell_r101"
  2, 16, "t.l0.arctic_cell_r111"

  2, 17, "t.l0.arctic_cell_d100"
  2, 17, "t.l0.arctic_cell_d110"
  2, 18, "t.l0.arctic_cell_d001"
  2, 18, "t.l0.arctic_cell_d011"
  2, 19, "t.l0.arctic_cell_d101"
  2, 19, "t.l0.arctic_cell_d111"

  2, 20, "t.l0.arctic_cell_l100"
  2, 20, "t.l0.arctic_cell_l110"
  2, 21, "t.l0.arctic_cell_l001"
  2, 21, "t.l0.arctic_cell_l011"
  2, 22, "t.l0.arctic_cell_l101"
  2, 22, "t.l0.arctic_cell_l111"

  2,  23, "t.l0.arctic_cell_u100"
  2,  23, "t.l0.arctic_cell_u110"
  2,  24, "t.l0.arctic_cell_u001"
  2,  24, "t.l0.arctic_cell_u011"
  2,  25, "t.l0.arctic_cell_u101"
  2,  25, "t.l0.arctic_cell_u111"

}
