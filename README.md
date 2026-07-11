# PS1 — a PlayStation 1 theme for Zed

The beige console plastic as the canvas; the four controller buttons doing the
syntax work. Warm, retro, and readable.

## The palette

The chrome — panels, tabs, title bar, editor — is the grey-beige of the original
console shell. The syntax is carried by the four **controller-button colors**, and
their roles never move across any variant:

| Button | Color | Syntax role |
|---|---|---|
| ✕ Cross | Blue | keywords, tags, control flow |
| ○ Circle | Red | numbers, booleans, constants |
| △ Triangle | Green | strings |
| ▢ Square | Pink | functions, constructors |

A memory-card **amber** fills in for types and warnings (four colors alone leave
types clashing with keywords), and multiplayer cursors follow the buttons in
controller order.

## Variants

Twelve themes across three axes:

- **Appearance** — Light (beige console shell) and Dark (matte graphite console top).
- **Contrast** — Standard, **High Contrast** (WCAG AA on all text including comments),
  and **Soft** (lower-saturation, gentle for long sessions).
- **Italics** — every variant ships in an italic edition (comments, emphasis, links)
  and a **No Italics** edition.

| | Light | Dark |
|---|---|---|
| Standard | PS1 Light | PS1 Dark |
| High Contrast | PS1 Light High Contrast | PS1 Dark High Contrast |
| Soft | PS1 Light Soft | PS1 Dark Soft |

…each also as `… (No Italics)`.

### A note on contrast

The **High Contrast** pair clears WCAG AA (4.5:1) for body text and syntax including
comments. **Standard** clears AA-large (3:1) on code tokens with comfortable body text.
**Soft** is deliberately gentle — some syntax colors fall below AA by design, in
exchange for a lower-fatigue feel. Pick Soft for vibe, HC for strict accessibility.

## Install

**From the Zed extension registry** (once published): open the Extensions panel
(`cmd-shift-x`), search **PS1**, install.

**Manually / for development:** clone this repo, then in Zed run
`zed: install dev extension` and point it at this directory.

## Pairing with your OS light/dark toggle

```json
{
  "theme": {
    "mode": "system",
    "light": "PS1 Light",
    "dark": "PS1 Dark"
  }
}
```

Swap in any of the variants (e.g. `"PS1 Light High Contrast"` / `"PS1 Dark High Contrast"`).

## License

MIT — see [LICENSE](LICENSE).
