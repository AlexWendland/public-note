# Personal Theme

Custom Hugo theme with Tailwind CSS.

## Features

- Tailwind CSS for styling
- Dark mode support
- Typography plugin for prose content
- Math support (MathJax)
- Responsive design

## Development

Test the theme locally:

```bash
# From repo root
hugo server --theme personal

# Or use the hugo-dev command
hugo-dev
```

## Requirements

- Hugo 0.152.0+
- Node.js (for Tailwind CSS)
- @tailwindcss/typography plugin

## Structure

- `layouts/` - Hugo templates
- `assets/css/` - Tailwind CSS entry point
- `static/` - Static assets
- `tailwind.config.js` - Tailwind configuration
- `postcss.config.js` - PostCSS configuration
