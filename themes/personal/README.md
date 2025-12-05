# Personal Theme

## Color Guide

This theme uses the [Catppuccin](https://catppuccin.com/) Mocha color palette.
All colors are defined in `assets/css/main.css` in the `@theme` block.

**License:** Catppuccin is licensed under the MIT License. See [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).

### How to Use in Templates

Use Tailwind utility classes with Catppuccin color names:

```html
<div class="bg-base text-text">
  <h1 class="text-mauve">Heading</h1>
  <a href="..." class="text-sapphire hover:text-sky">Link</a>
</div>
```

### Color Categories & Usage

#### Base Colors (Backgrounds)
- `bg-base` - Main background (#1e1e2e)
- `bg-mantle` - Slightly darker than base (#181825)
- `bg-crust` - Darkest background (#11111b)

**Use for:** Page backgrounds, panels, cards

#### Surface Colors (UI Elements)
- `bg-surface-0` - Elevated surfaces (#313244)
- `bg-surface-1` - More elevated (#45475a)
- `bg-surface-2` - Most elevated (#585b70)

**Use for:** Buttons, inputs, code blocks, borders

#### Overlay Colors (Muted Elements)
- `text-overlay-0` - Muted text (#6c7086)
- `text-overlay-1` - Less muted (#7f849c)
- `text-overlay-2` - Least muted (#9399b2)

**Use for:** Disabled states, placeholders, subtle text

#### Text Colors
- `text-subtext-0` - Secondary text (#a6adc8)
- `text-subtext-1` - Slightly lighter secondary (#bac2de)
- `text-text` - Main text color (#cdd6f4)

**Use for:** Body text, headings, descriptions

#### Accent Colors (Semantic)

##### For Emphasis
- `text-mauve` - Primary accent, headers (#cba6f7)
- `text-blue` - Secondary accent, links (#89b4fa)
- `text-sapphire` - Tertiary accent (#74c7ec)

##### For Status/Actions
- `text-green` - Success, positive (#a6e3a1)
- `text-red` - Error, danger (#f38ba8)
- `text-yellow` - Warning, caution (#f9e2af)
- `text-peach` - Info, highlight (#fab387)

##### For Syntax/Code
- `text-pink` - Keywords (#f5c2e7)
- `text-teal` - Functions (#94e2d5)
- `text-sky` - Variables (#89dceb)
- `text-lavender` - Constants (#b4befe)

##### Decorative
- `text-rosewater` - Soft accent (#f5e0dc)
- `text-flamingo` - Soft accent (#f2cdcd)
- `text-maroon` - Rich accent (#eba0ac)

### Examples

#### Card Component
```html
<div class="bg-surface-0 border border-surface-1 rounded-lg p-6">
  <h2 class="text-xl font-bold text-mauve mb-2">Card Title</h2>
  <p class="text-subtext-0">Description text</p>
  <a href="#" class="text-sapphire hover:text-sky">Read more →</a>
</div>
```

#### Code Block
```html
<pre class="bg-mantle border border-surface-0 rounded p-4">
  <code class="text-text">
    <!-- code here -->
  </code>
</pre>
```

#### Navigation
```html
<nav class="bg-crust border-b border-surface-0">
  <a href="#" class="text-blue hover:text-sapphire">Home</a>
  <a href="#" class="text-subtext-1 hover:text-text">About</a>
</nav>
```

### Admonitions (Callouts)

The theme includes built-in support for Obsidian-style admonitions with Catppuccin colors.

#### Usage

```markdown
> [!note]
> This is a note admonition

> [!warning]
> This is a warning

> [!definition]
> A **binary tree** is a tree data structure where each node has at most two children.

> [!example]+
> This is a foldable example (click to expand)
```

#### Available Types & Colors

Following Catppuccin's semantic guidelines:

| Admonition Type | Color | Usage |
|----------------|-------|-------|
| `note` | Blue | General information and notes |
| `example` | Peach | Examples and demonstrations |
| `important` | Mauve | Emphasis and important points |
| `warning` | Yellow | Cautions and warnings |
| `lemma` | Lavender | Mathematical lemmas and propositions |
| `definition` | Teal | Definitions and foundational concepts |
| `quote` | Sapphire | Quotations and citations |
| `question` | Sky | Questions and inquiries |

#### Foldable Admonitions

Add `+` or `-` after the type to make it foldable:

```markdown
> [!lemma]+
> If G is a connected graph with n vertices, then G has at least n-1 edges.

> [!question]-
> Why does this property hold for all connected graphs?
```

#### Adding New Admonition Types

To add a new admonition type (e.g., `theorem`):

1. **Add the icon mapping** in `layouts/_default/_markup/render-blockquote-alert.html`:

```go
{{- $icons := dict
  "note"       "file-pen-solid.svg"
  "theorem"    "lightbulb-solid.svg"  // Add your new type here
  // ... other types
}}
```

Available icons are in `themes/personal/layouts/partials/admonitions/icons/`. Common choices:
- `lightbulb-solid.svg` - ideas, insights
- `file-pen-solid.svg` - notes, writing
- `circle-exclamation-solid.svg` - important, alerts
- `person-chalkboard-solid.svg` - teaching, examples
- `file-lines-solid.svg` - documents, definitions
- `circle-info-solid.svg` - information
- `triangle-exclamation-solid.svg` - warnings
- `circle-question-solid.svg` - questions
- `quote-right-solid.svg` - quotations
- `circle-check-solid.svg` - success
- `circle-xmark-solid.svg` - errors
- `flask-solid.svg` - experiments
- `bell-solid.svg` - notifications
- `code-solid.svg` - code
- `list-check-solid.svg` - tasks
- `bullseye-solid.svg` - goals
- `file-circle-check-solid.svg` - completion

2. **Add the styling** in `assets/css/main.css` in the `@layer components` section:

```css
/* Theorem - Green (proven statements) */
.admonition-theorem {
  @apply border-green bg-green/10;
}

.admonition-theorem .admonition-header {
  @apply text-green;
}

.admonition-theorem .admonition-header svg {
  @apply fill-green;
}
```

**Available Catppuccin colors:** `blue`, `sapphire`, `sky`, `teal`, `green`, `yellow`, `peach`, `maroon`, `red`, `pink`, `mauve`, `lavender`, `rosewater`, `flamingo`

3. **Use it** in your markdown:

```markdown
> [!theorem]
> The sum of angles in a triangle equals 180°.
```

### Changing the Palette

To switch to a different Catppuccin flavor (Latte, Frappé, Macchiato):

1. Get color values from https://catppuccin.com/palette
2. Update the `@theme` block in `assets/css/main.css`
3. Keep the same color names, just change the hex values
4. Hugo will auto-reload!

### Color Contrast

Following Catppuccin's guidelines:
- **High contrast**: `text-text` on `bg-base`
- **Medium contrast**: `text-subtext-0` on `bg-base`
- **Low contrast**: `text-overlay-0` on `bg-base`

Always test readability!

## Acknowledgements

This theme uses code and assets from the following projects:

- **[Catppuccin](https://catppuccin.com/)** - The Catppuccin Mocha color palette is used throughout this theme. Licensed under the MIT License. See [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) for full license text.

- **[hugo-admonitions](https://github.com/oreo-dtx-lab/hugo-admonitions)** - The admonition system (render hooks and SVG icons) is adapted from hugo-admonitions by oreo-dtx-lab. Licensed under the MIT License. See [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) for full license text.
