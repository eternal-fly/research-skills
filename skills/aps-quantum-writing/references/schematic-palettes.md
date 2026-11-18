# Color and composition for mechanism schematics

Start with the operation the reader should recognize at column width. Draw its physical objects and connections at a useful scale. Tuck a branch, shared input or local expansion against its interface. A repeated circuit block can sit within one field. An adjacent trace or measured output can share the circuit's identity marks. Draw a second row when it carries an independent comparison, a time sequence or meaningful geometry.

Select one palette by the role it serves. On white or a pale field, give color to an object, an edge, a gate or a connection. Label it or give it a distinctive shape, line style or position. A time-series color, a sign, or the direction of a scalar color map already established in the manuscript takes priority. At insertion size, trace the main path and its return in grayscale. Increase line contrast or change a glyph where an identity disappears.

## Ten examples from paper figures

The HEX values below are the author's approximate samples from PDF renderings. The linked figure pages were visually checked on 2026-11-17. Four are APS versions of record and six are pinned author manuscripts. Use the values as editorial choices. The [machine-readable palette catalog](../assets/schematic-palettes.json) includes the DOI, figure, edition and color assignments.

| Palette | Source figure | Color carriers and transferable idea |
|---|---|---|
| 1. `fourier-layer` | [PRX Quantum, Fig. 1(a,b), version of record](https://harvest.aps.org/v2/journals/articles/10.1103/2tt3-yndr/fulltext#page=3) | module `#C1DDEC`, Fourier node `#66AAD1`, operator `#F4D899`, addition activation `#E59E66`. Carry a pale grouping field across a layer. Reserve amber and orange for operator or junction nodes. |
| 2. `state-transition` | [PRX Quantum, Fig. 1, version of record](https://harvest.aps.org/v2/journals/articles/10.1103/xysy-q3fp/fulltext#page=3) | state `#EBEBEB`, transition `#B187B1`. Keep successive states visually alike and name the transformation beside its arrow. |
| 3. `ion-regions` | [Physical Review Research, Fig. 2, version of record](https://harvest.aps.org/v2/journals/articles/10.1103/b7ck-8wh4/fulltext#page=6) | field `#E3E3E3`, zone pink `#CF9999`, zone green `#B0D197`, zone yellow `#D8DF87`, zone blue `#93AAD3`. Reuse region identities from the chip to its tabular representation. Blue arrows show the mapping. |
| 4. `repeated-blocks` | [Physical Review Applied, Fig. 6, author manuscript](https://arxiv.org/pdf/2512.01120v3#page=11) | group `#F5F5F5`, segment blue `#006EAF`, segment green `#81B366`, gate `#D9E7FB`. Mark segment types with short blue and green strokes and group repeated operations with a dashed boundary. |
| 5. `parallel-samplers` | [Physical Review A, Fig. 1, author manuscript](https://arxiv.org/pdf/2505.00102v1#page=4) | group `#EAEAEA`, sampler 1 `#E2A678`, sampler 2 `#A0BFD6`, sampler n `#8BCEA9`. Carry each sampler's color along its own wires within a common neutral enclosure. |
| 6. `qsp-rounds` | [Physical Review A, Fig. 1(a–c), author manuscript](https://arxiv.org/pdf/2508.20261v3#page=4) | round `#D9D9D9`, phase edge `#104862`, rotation edge `#F2AA84`. Distinguish operations by their gate edges within gray rounds. Red denotes endpoint hybridization and magenta marks excitation-dependent phase shifts in the source. |
| 7. `parameter-encoding` | [Physical Review A, Fig. 1, author manuscript](https://arxiv.org/pdf/2601.05457v2#page=3) | measurement `#F0F2F4`, wire `#293241`, encoding `#FDDD81`. Highlight the parameter-encoding operation along a dark wire leading to a cool neutral measurement block. |
| 8. `bath-ends` | [Physical Review Letters, Fig. 1(a), author manuscript](https://arxiv.org/pdf/2511.05328v2#page=3) | bath `#FEE7E7`, left end `#B4C7E7`, right end `#FFE699`, auxiliary `#CCB5DD`. Treat the bath as a faint field. Use distinct endpoint markers and a third fill for auxiliary sites. |
| 9. `control-trajectory` | [Physical Review B, Fig. 1(a–e), author manuscript](https://arxiv.org/pdf/2504.10803v2#page=4) | control `#ACE4FF`, Bernoulli `#FABBBA`, local gate `#FB8500`. Reuse the control and evolution colors in trajectory strips. A strong orange can mark an individual gate. |
| 10. `reservoir-ports` | [PRX Quantum, Fig. 1(a–c), version of record](https://harvest.aps.org/v2/journals/articles/10.1103/jknv-3tx7/fulltext#page=2) | core `#003399`, input `#FF9D0A`, output `#0ACD0A`. Place dark reservoir nodes on white and confine high chroma to the labeled input and output ports. |

## Floquet circuit example

The Fourier neural operator in example 1 illustrates hierarchy within a layer. Borrow that visual principle for a Floquet circuit. Example 2 supplies a quiet visual treatment for a secondary branch. Example 3 shows how a graph and a tensor can share an identity mark. Use only the parts that carry a meaning in the new figure.

For a repeated Floquet core, use a light blue-gray field `#EDF2F6`, fine boundary `#A7B6C4` and ink-blue labels `#263B4D`. Ordinary gates take mist blue `#D8E6EF`. A modeled reset takes pale mauve `#E8E0EB` and its local return path uses `#8C728E`. Give an actual measurement glyph pale teal `#DDECEB`. In this composition, reserve a warm accent for at most one small node. Use distinct connections for the next cycle, the reset channel and the measured signal.

In a plotting script, `schematic_palette("floquet")` from [aps_figure_style.py](../scripts/aps_figure_style.py) returns these roles. `schematic_palette("ion-regions")["zone_blue"]` retrieves a color by its source role. Reproduce the original [synthetic circuit example](../assets/schematic-examples/README.md) at full size before adapting its geometry.
