#!/usr/bin/env python3
"""Plain-text versions of the LaTeX used on the site.

On pages, KaTeX typesets every \\( ... \\) and \\[ ... \\]. Where no typesetting
is possible (link previews, search engines, feeds, share images, the newsletter,
headlines), to_plain() turns the formulas into Unicode mathematics:
\\(\\varepsilon^2 N/(2R^2)\\) becomes ε²N/(2R²), \\(\\sqrt{n}\\) becomes √n.
Run this file to test it.
"""
import re

MATH = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ϵ", "varepsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "varpi": "ϖ", "rho": "ρ",
    "varrho": "ϱ", "sigma": "σ", "varsigma": "ς", "tau": "τ", "upsilon": "υ", "phi": "ϕ",
    "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π",
    "Sigma": "Σ", "Upsilon": "Υ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "approx": "≈",
    "sim": "∼", "simeq": "≃", "cong": "≅", "equiv": "≡", "propto": "∝", "ll": "≪", "gg": "≫",
    "lesssim": "≲", "gtrsim": "≳", "in": "∈", "notin": "∉", "ni": "∋", "subset": "⊂",
    "subseteq": "⊆", "supset": "⊃", "supseteq": "⊇", "cup": "∪", "cap": "∩", "setminus": "∖",
    "emptyset": "∅", "varnothing": "∅", "infty": "∞", "partial": "∂", "nabla": "∇",
    "forall": "∀", "exists": "∃", "neg": "¬", "land": "∧", "lor": "∨", "wedge": "∧", "vee": "∨",
    "to": "→", "rightarrow": "→", "leftarrow": "←", "mapsto": "↦", "Rightarrow": "⇒",
    "implies": "⇒", "Leftrightarrow": "⇔", "iff": "⇔", "uparrow": "↑", "downarrow": "↓",
    "times": "×", "cdot": "·", "cdots": "⋯", "ldots": "…", "dots": "…", "pm": "±", "mp": "∓",
    "div": "÷", "circ": "∘", "ast": "∗", "star": "⋆", "oplus": "⊕", "otimes": "⊗",
    "top": "⊤", "perp": "⊥", "mid": "|", "vert": "|", "lvert": "|", "rvert": "|",
    "Vert": "‖", "lVert": "‖", "rVert": "‖", "|": "‖", "langle": "⟨", "rangle": "⟩",
    "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈", "rceil": "⌉", "prime": "′",
    "sum": "∑", "prod": "∏", "int": "∫", "oint": "∮", "ell": "ℓ", "hbar": "ℏ",
    "{": "{", "}": "}", "%": "%", "$": "$", "&": "&", "#": "#", "_": "_",
}
NAMED = {"log", "ln", "exp", "max", "min", "sup", "inf", "lim", "liminf", "limsup", "det",
         "Pr", "sin", "cos", "tan", "arg", "argmax", "argmin", "deg", "dim", "ker", "tr",
         "Var", "Cov", "sgn", "mod", "gcd"}
SPACES = {",": " ", ";": " ", ":": " ", "!": "", "quad": " ", "qquad": " ", " ": " ", "enspace": " ", "thinspace": " "}
DROP = {"left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr", "biggl",
        "biggr", "Biggl", "Biggr", "displaystyle", "textstyle", "scriptstyle", "limits", "nolimits"}
STYLE = {"mathrm", "text", "textrm", "textit", "operatorname", "mathbf", "boldsymbol", "bm",
         "mathit", "mathsf", "mathtt", "emph", "textbf", "mbox", "mathcal", "mathscr"}
BB = {"R": "ℝ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ", "C": "ℂ", "E": "𝔼", "P": "ℙ", "1": "𝟙"}
ACCENT = {"hat": "̂", "widehat": "̂", "tilde": "̃", "widetilde": "̃",
          "bar": "̄", "overline": "̅", "dot": "̇", "ddot": "̈", "vec": "⃗"}
SUP = dict(zip("0123456789+-=()nijkabcdefghlmoprstuvwxyzABDEGHIJKLMNOPRTUVW",
               "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱʲᵏᵃᵇᶜᵈᵉᶠᵍʰˡᵐᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂ"))
SUP.update({"−": "⁻", "′": "′", "*": "*", "∗": "*", "⊤": "ᵀ", "T": "ᵀ"})
SUB = dict(zip("0123456789+-=()aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ"))
SUB.update({"−": "₋"})
RELATIONS = set("=<>≤≥≠≈∼≃≅≡∝≪≫≲≳∈∉⊂⊆⊃⊇→←↦⇒⇔")


def _group(s, i):
    """Read one argument starting at s[i]: a {braced group}, a command or one character."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        depth, j = 1, i + 1
        while j < len(s) and depth:
            depth += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        return s[i + 1:j - 1], j
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def _script(text, table, mark):
    if text and all(ch in table for ch in text):
        return "".join(table[ch] for ch in text)
    return mark + (text if len(text) == 1 else "(" + text + ")")


def _convert(s):
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        if ch == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            name, i = m.group(1), i + len(m.group(0))
            if name in DROP:
                continue
            if name in SPACES:
                out.append(SPACES[name])
            elif name == "frac" or name in ("dfrac", "tfrac"):
                a, i = _group(s, i)
                b, i = _group(s, i)
                a, b = _convert(a), _convert(b)
                wrap = lambda x: x if re.fullmatch(r"[\w′.]+|√\S+", x) else "(" + x + ")"
                out.append(wrap(a) + "/" + wrap(b))
            elif name == "sqrt":
                a, i = _group(s, i)
                a = _convert(a)
                out.append("√" + (a if re.fullmatch(r"[\w.]+", a) else "(" + a + ")"))
            elif name == "mathbb":
                a, i = _group(s, i)
                out.append("".join(BB.get(c, c) for c in a))
            elif name in STYLE:
                a, i = _group(s, i)
                out.append(_convert(a))
            elif name in ACCENT:
                a, i = _group(s, i)
                a = _convert(a)
                out.append(a + ACCENT[name] if len(a) == 1 else a)
            elif name in NAMED:
                out.append(name + " ")
            elif name in SYMBOLS:
                out.append(SYMBOLS[name])
            else:
                out.append(name)
        elif ch in "^_":
            a, i = _group(s, i + 1)
            a = _convert(a).replace(" ", "")
            out.append(_script(a, SUP if ch == "^" else SUB, ch))
        elif ch in "{}":
            i += 1
        elif ch == " ":
            i += 1                      # spaces in TeX mathematics are not printed
        elif ch == "-":
            out.append("−")
            i += 1
        elif ch == "~":
            out.append(" ")
            i += 1
        else:
            out.append(ch)
            i += 1
    text = "".join(out)
    text = re.sub(r"\s*([" + "".join(RELATIONS) + r"])\s*", r" \1 ", text)
    text = re.sub(r"\s*,\s*", ", ", text)
    text = re.sub(r"(\w) ([)\]|/])", r"\1\2", text)
    text = re.sub(r"\b(" + "|".join(sorted(NAMED, key=len, reverse=True)) + r") \(", r"\1(", text)
    return re.sub(r"\s+", " ", text).strip()


def to_plain(text):
    """Replace every formula in text by its Unicode form."""
    if not isinstance(text, str) or ("\\(" not in text and "\\[" not in text):
        return text
    return MATH.sub(lambda m: _convert(m.group(1) if m.group(1) is not None else m.group(2)), text)


if __name__ == "__main__":
    tests = {
        r"decays like \(\exp\bigl(-(1+o(1))\,\varepsilon^2 N/(2R^2 s^2)\bigr)\), where":
            "decays like exp(−(1+o(1)) ε²N/(2R²s²)), where",
        r"an error of order \(\sqrt{d\,\lambda_{\max}}\,\log N / N\)": "an error of order √(d λₘₐₓ) log N/N",
        r"order \(d\), the VC dimension": "order d, the VC dimension",
        r"rate \(O(1/\sqrt{n})\)": "rate O(1/√n)",
        r"\(\mathbb{E}[X] \le \frac{1}{2}\)": "𝔼[X] ≤ 1/2",
        r"\(x_i \in \mathbb{R}^d\)": "xᵢ ∈ ℝᵈ",
        r"\(f'(x)\)": "f'(x)",
        "no maths here": "no maths here",
    }
    bad = 0
    for src, want in tests.items():
        got = to_plain(src)
        if got != want:
            bad += 1
            print("MISMATCH", repr(src), "\n   got ", repr(got), "\n   want", repr(want))
    print("ok" if not bad else f"{bad} mismatches")
