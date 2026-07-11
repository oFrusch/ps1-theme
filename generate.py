#!/usr/bin/env python3
"""Generate the PS1 theme family from palette specs.

One palette dict per (mode, contrast). build_style() expands it into a full
Zed ThemeStyleContent block so every variant stays structurally identical and
only the color values differ. italic flag toggles font_style on comments/emphasis.
"""
import json
from collections import OrderedDict

# The four PlayStation controller buttons — the constant across every variant.
# Cross=blue, Circle=red, Triangle=green, Square=pink. Values retuned per palette
# for contrast, but the *roles* never move.

def alpha(hex6, aa):
    return hex6 + aa

# ---- palette definitions -------------------------------------------------
# Each palette provides the ~30 semantic anchors build_style() needs.

PALETTES = {}

PALETTES[("light", "standard")] = dict(
    # controller buttons (syntax roles) — greens/blues darkened slightly so
    # syntax clears usable contrast on the light beige editor.
    blue="#245d9e", red="#b52a2a", green="#0a7062", pink="#9c2f79",
    amber="#8c6714", cyan="#136d79",
    # surfaces (console-shell beige, editor lighter like the lid)
    bg="#ccc6b5", surface="#bfb9a7", elevated="#d9d4c4", editor="#d6d0c0",
    panel="#bfb9a7", titlebar="#b3ad9a", tab_active="#d6d0c0",
    # borders / guides
    border="#968f7b", border_variant="#aba58f", guide="#b1ab97", guide_active="#968f7b",
    # text
    text="#333028", muted="#665f4f", faint="#837d6b", comment="#84806e",
    line_number="#8a8571",
    # syntax extras
    variable="#333028", property="#544e40", punctuation="#665f4f",
    hint="#6d7f9c", predictive="#8f8a76",
    active_line=alpha("#c4bdaa", "66"),
    scrollbar="#968f7b",
    term_bg="#d8d3c5", term_fg="#3a372e", term_black="#3a372e", term_white="#e6e2d6",
)

PALETTES[("dark", "standard")] = dict(
    blue="#5d94d6", red="#e05252", green="#2fae9a", pink="#d96bb0",
    amber="#cfa93f", cyan="#4aa9ba",
    bg="#1c1b1e", surface="#232227", elevated="#2a292e", editor="#1c1b1e",
    panel="#1e1d21", titlebar="#26252a", tab_active="#28272d",
    border="#39383f", border_variant="#2f2e34", guide="#2f2e34", guide_active="#4a4954",
    text="#e6e3dc", muted="#9d998e", faint="#6f6b62", comment="#6f6b62",
    line_number="#57545c",
    variable="#e6e3dc", property="#c4c0b6", punctuation="#9d998e",
    hint="#8a9ab8", predictive="#6f6b62",
    active_line=alpha("#2a292e", "66"),
    scrollbar="#4a4954",
    term_bg="#161518", term_fg="#e6e3dc", term_black="#2a292e", term_white="#e6e3dc",
)

# High contrast: push text-to-bg apart, saturate accents, lighten/darken shell.
PALETTES[("light", "hc")] = dict(
    blue="#0a4c9c", red="#b81414", green="#03705f", pink="#9c1478",
    amber="#875f00", cyan="#046070",
    bg="#e8e3d4", surface="#ddd8c8", elevated="#f2eee1", editor="#f2eee1",
    panel="#ddd8c8", titlebar="#d0cab8", tab_active="#f2eee1",
    border="#7d7663", border_variant="#9a9380", guide="#c2bca9", guide_active="#928c78",
    text="#161410", muted="#4a4638", faint="#6c6656", comment="#6c6656",
    line_number="#78725f",
    variable="#161410", property="#3a3529", punctuation="#4a4638",
    hint="#3a5a8a", predictive="#78725f",
    active_line=alpha("#cfc8b3", "80"),
    scrollbar="#7d7663",
    term_bg="#f2eee1", term_fg="#161410", term_black="#161410", term_white="#f2eee1",
)

PALETTES[("dark", "hc")] = dict(
    blue="#8ab8f0", red="#ff7a7a", green="#4fd4bd", pink="#f593d0",
    amber="#f0c860", cyan="#6fcfdf",
    bg="#111013", surface="#191820", elevated="#201f28", editor="#111013",
    panel="#151419", titlebar="#1c1b23", tab_active="#22212a",
    border="#4a4954", border_variant="#33323a", guide="#33323a", guide_active="#5a5966",
    text="#f6f4ee", muted="#b8b4a9", faint="#847f74", comment="#847f74",
    line_number="#6a6772",
    variable="#f6f4ee", property="#d8d4ca", punctuation="#b8b4a9",
    hint="#a8bce0", predictive="#847f74",
    active_line=alpha("#201f28", "80"),
    scrollbar="#5a5966",
    term_bg="#0c0b0e", term_fg="#f6f4ee", term_black="#33323a", term_white="#f6f4ee",
)

# Soft / low-contrast: desaturate accents, pull text toward mid, gentle shell.
PALETTES[("light", "soft")] = dict(
    blue="#5885b0", red="#c06a6a", green="#4f9488", pink="#b070a0",
    amber="#a8894f", cyan="#5b8f97",
    bg="#d4cfc1", surface="#c9c3b3", elevated="#ded9cb", editor="#dbd6c8",
    panel="#c9c3b3", titlebar="#c0bAA8".replace("A","b"), tab_active="#dbd6c8",
    border="#a49d89", border_variant="#b4ae9b", guide="#bab4a1", guide_active="#a49d89",
    text="#4a463c", muted="#736d5d", faint="#8f8a79", comment="#94907e",
    line_number="#948f7d",
    variable="#4a463c", property="#635d4f", punctuation="#736d5d",
    hint="#7885a0", predictive="#948f7d",
    active_line=alpha("#c8c1ae", "55"),
    scrollbar="#a49d89",
    term_bg="#d4cfc1", term_fg="#4a463c", term_black="#4a463c", term_white="#ded9cb",
)

PALETTES[("dark", "soft")] = dict(
    blue="#6f97c4", red="#cc6f6f", green="#54a596", pink="#c07fac",
    amber="#c2a35c", cyan="#5fa0af",
    bg="#212026", surface="#28272e", elevated="#2f2e36", editor="#212026",
    panel="#232228", titlebar="#2b2a32", tab_active="#2d2c34",
    border="#3f3e47", border_variant="#34333b", guide="#34333b", guide_active="#4d4c56",
    text="#d4d1c9", muted="#928e84", faint="#6b675f", comment="#6b675f",
    line_number="#57545c",
    variable="#d4d1c9", property="#b3afa6", punctuation="#928e84",
    hint="#8695ac", predictive="#6b675f",
    active_line=alpha("#2f2e36", "55"),
    scrollbar="#4d4c56",
    term_bg="#1b1a1f", term_fg="#d4d1c9", term_black="#2f2e36", term_white="#d4d1c9",
)


def build_style(p, italic):
    """Expand a palette into a full Zed ThemeStyleContent block."""
    fs = (lambda v: {"font_style": v}) if False else None

    def maybe_italic(d):
        if italic:
            d = dict(d)
            d["font_style"] = "italic"
        return d

    blue, red, green, pink = p["blue"], p["red"], p["green"], p["pink"]
    amber, cyan = p["amber"], p["cyan"]

    s = OrderedDict()
    s["accents"] = [blue, red, green, pink]

    s["background"] = p["bg"]
    s["surface.background"] = p["surface"]
    s["elevated_surface.background"] = p["elevated"]
    s["panel.background"] = p["panel"]
    s["panel.focused_border"] = blue
    s["panel.indent_guide"] = p["guide"]
    s["panel.indent_guide_active"] = p["guide_active"]
    s["panel.indent_guide_hover"] = p["guide_active"]
    s["title_bar.background"] = p["titlebar"]
    s["title_bar.inactive_background"] = p["panel"]
    s["status_bar.background"] = p["titlebar"]
    s["toolbar.background"] = p["surface"]
    s["tab_bar.background"] = p["panel"]
    s["tab.active_background"] = p["tab_active"]
    s["tab.inactive_background"] = p["panel"]

    s["border"] = p["border"]
    s["border.variant"] = p["border_variant"]
    s["border.focused"] = blue
    s["border.selected"] = blue
    s["border.disabled"] = p["guide"]
    s["border.transparent"] = "#00000000"
    s["pane.focused_border"] = blue
    s["pane_group.border"] = p["border"]

    s["text"] = p["text"]
    s["text.muted"] = p["muted"]
    s["text.placeholder"] = p["faint"]
    s["text.disabled"] = p["faint"]
    s["text.accent"] = blue
    s["icon"] = p["text"]
    s["icon.muted"] = p["muted"]
    s["icon.disabled"] = p["faint"]
    s["icon.placeholder"] = p["faint"]
    s["icon.accent"] = blue

    s["element.background"] = p["surface"]
    s["element.hover"] = p["border_variant"]
    s["element.active"] = p["guide_active"]
    s["element.selected"] = p["guide_active"]
    s["element.disabled"] = alpha(p["surface"], "88")
    s["ghost_element.background"] = "#00000000"
    s["ghost_element.hover"] = alpha(p["border_variant"], "88")
    s["ghost_element.active"] = p["guide_active"]
    s["ghost_element.selected"] = alpha(p["guide_active"], "aa")
    s["ghost_element.disabled"] = alpha(p["surface"], "88")
    s["drop_target.background"] = alpha(blue, "26")
    s["link_text.hover"] = blue

    s["editor.background"] = p["editor"]
    s["editor.foreground"] = p["text"]
    s["editor.gutter.background"] = p["editor"]
    s["editor.subheader.background"] = p["surface"]
    s["editor.active_line.background"] = p["active_line"]
    s["editor.highlighted_line.background"] = alpha(amber, "26")
    s["editor.line_number"] = p["line_number"]
    s["editor.active_line_number"] = p["text"]
    s["editor.invisible"] = p["border_variant"]
    s["editor.wrap_guide"] = p["guide"]
    s["editor.active_wrap_guide"] = p["guide_active"]
    s["editor.indent_guide"] = p["guide"]
    s["editor.indent_guide_active"] = p["guide_active"]
    s["editor.document_highlight.read_background"] = alpha(blue, "1f")
    s["editor.document_highlight.write_background"] = alpha(pink, "1f")
    s["editor.document_highlight.bracket_background"] = alpha(green, "1f")
    s["search.match_background"] = alpha(amber, "40")

    s["scrollbar.thumb.background"] = alpha(p["scrollbar"], "66")
    s["scrollbar.thumb.hover_background"] = alpha(p["scrollbar"], "aa")
    s["scrollbar.thumb.border"] = alpha(p["scrollbar"], "00")
    s["scrollbar.track.background"] = "#00000000"
    s["scrollbar.track.border"] = "#00000000"

    def status(color):
        return (color, alpha(color, "1a"), alpha(color, "66"))

    for key, color in [("error", red), ("warning", amber), ("info", blue),
                       ("success", green), ("hint", p["hint"]), ("predictive", p["predictive"])]:
        c, bgc, bd = status(color)
        s[key] = c
        s[f"{key}.background"] = bgc
        s[f"{key}.border"] = bd

    for key, color in [("created", green), ("deleted", red), ("modified", amber),
                       ("renamed", blue), ("conflict", pink)]:
        c, bgc, bd = status(color)
        s[key] = c
        s[f"{key}.background"] = bgc
        s[f"{key}.border"] = bd

    for key in ["ignored", "hidden", "unreachable"]:
        s[key] = p["faint"]
        s[f"{key}.background"] = "#00000000"
        s[f"{key}.border"] = p["guide"]

    s["players"] = [
        {"cursor": blue, "background": blue, "selection": alpha(blue, "40")},
        {"cursor": red, "background": red, "selection": alpha(red, "40")},
        {"cursor": green, "background": green, "selection": alpha(green, "40")},
        {"cursor": pink, "background": pink, "selection": alpha(pink, "40")},
    ]

    # terminal — button colors on ansi, brights are the pastel controller set
    s["terminal.background"] = p["term_bg"]
    s["terminal.foreground"] = p["term_fg"]
    s["terminal.bright_foreground"] = p["text"]
    s["terminal.dim_foreground"] = p["muted"]
    s["terminal.ansi.background"] = p["term_bg"]
    s["terminal.ansi.black"] = p["term_black"]
    s["terminal.ansi.red"] = red
    s["terminal.ansi.green"] = green
    s["terminal.ansi.yellow"] = amber
    s["terminal.ansi.blue"] = blue
    s["terminal.ansi.magenta"] = pink
    s["terminal.ansi.cyan"] = cyan
    s["terminal.ansi.white"] = p["term_white"]
    s["terminal.ansi.bright_black"] = p["muted"]
    s["terminal.ansi.bright_red"] = "#ff6666"
    s["terminal.ansi.bright_green"] = "#4ecfba"
    s["terminal.ansi.bright_yellow"] = "#e6c25a"
    s["terminal.ansi.bright_blue"] = "#7fb2e5"
    s["terminal.ansi.bright_magenta"] = "#e97fc4"
    s["terminal.ansi.bright_cyan"] = "#6cc7d8"
    s["terminal.ansi.bright_white"] = p["term_white"]
    s["terminal.ansi.dim_black"] = p["faint"]
    s["terminal.ansi.dim_red"] = "#a55050"
    s["terminal.ansi.dim_green"] = "#3d7a6f"
    s["terminal.ansi.dim_yellow"] = "#8a713a"
    s["terminal.ansi.dim_blue"] = "#54749c"
    s["terminal.ansi.dim_magenta"] = "#94537e"
    s["terminal.ansi.dim_cyan"] = "#4a7d87"
    s["terminal.ansi.dim_white"] = p["muted"]

    syn = OrderedDict()
    syn["comment"] = maybe_italic({"color": p["comment"]})
    syn["comment.doc"] = maybe_italic({"color": p["comment"]})
    syn["string"] = {"color": green}
    syn["string.escape"] = {"color": pink}
    syn["string.regex"] = {"color": amber}
    syn["string.special"] = {"color": amber}
    syn["string.special.symbol"] = {"color": green}
    syn["keyword"] = {"color": blue}
    syn["boolean"] = {"color": red}
    syn["number"] = {"color": red}
    syn["constant"] = {"color": red}
    syn["function"] = {"color": pink}
    syn["constructor"] = {"color": pink}
    syn["type"] = {"color": amber}
    syn["enum"] = {"color": amber}
    syn["variable"] = {"color": p["variable"]}
    syn["variable.special"] = {"color": blue}
    syn["property"] = {"color": p["property"]}
    syn["attribute"] = {"color": amber}
    syn["tag"] = {"color": blue}
    syn["operator"] = {"color": p["punctuation"]}
    syn["punctuation"] = {"color": p["punctuation"]}
    syn["punctuation.bracket"] = {"color": p["punctuation"]}
    syn["punctuation.delimiter"] = {"color": p["punctuation"]}
    syn["punctuation.list_marker"] = {"color": blue}
    syn["punctuation.special"] = {"color": pink}
    syn["label"] = {"color": blue}
    syn["link_text"] = {"color": blue}
    syn["link_uri"] = maybe_italic({"color": green})
    syn["title"] = {"color": p["text"], "font_weight": 700}
    syn["emphasis"] = maybe_italic({}) if italic else {"color": p["text"]}
    syn["emphasis.strong"] = {"font_weight": 700}
    syn["text.literal"] = {"color": green}
    syn["embedded"] = {"color": p["text"]}
    syn["preproc"] = {"color": pink}
    syn["primary"] = {"color": p["text"]}
    syn["predictive"] = maybe_italic({"color": p["predictive"]})
    syn["hint"] = {"color": p["hint"]}
    s["syntax"] = syn

    return s


CONTRAST_LABEL = {"standard": "", "hc": " High Contrast", "soft": " Soft"}

themes = []
# order: for each contrast tier, light then dark; italic variants first, then no-italics
for italic in (True, False):
    suffix = "" if italic else " (No Italics)"
    for contrast in ("standard", "hc", "soft"):
        for mode in ("light", "dark"):
            p = PALETTES[(mode, contrast)]
            appearance = mode
            mode_label = "Light" if mode == "light" else "Dark"
            name = f"PS1 {mode_label}{CONTRAST_LABEL[contrast]}{suffix}"
            themes.append(OrderedDict([
                ("name", name),
                ("appearance", appearance),
                ("style", build_style(p, italic)),
            ]))

family = OrderedDict([
    ("$schema", "https://zed.dev/schema/themes/v0.2.0.json"),
    ("name", "PS1"),
    ("author", "Owen Carpenter <owen.carpenter@blueconic.com>"),
    ("themes", themes),
])

import os
out = os.path.join(os.path.dirname(__file__), "themes", "ps1.json")
with open(out, "w") as f:
    json.dump(family, f, indent=2)
    f.write("\n")

print(f"wrote {len(themes)} themes to {out}")
for t in themes:
    print(" -", t["name"], f"({t['appearance']})")
