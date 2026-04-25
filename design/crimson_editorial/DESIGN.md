---
name: Crimson Editorial
colors:
  surface: '#fff8f7'
  surface-dim: '#f4d2d1'
  surface-bright: '#fff8f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff0ef'
  surface-container: '#ffe9e7'
  surface-container-high: '#ffe1e0'
  surface-container-highest: '#fcdbd9'
  on-surface: '#291716'
  on-surface-variant: '#5d3f3e'
  inverse-surface: '#402b2a'
  inverse-on-surface: '#ffedeb'
  outline: '#926e6d'
  outline-variant: '#e7bdbb'
  surface-tint: '#bf0027'
  primary: '#bb0026'
  on-primary: '#ffffff'
  primary-container: '#e51936'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb3b1'
  secondary: '#535f72'
  on-secondary: '#ffffff'
  secondary-container: '#d7e3fa'
  on-secondary-container: '#596578'
  tertiary: '#00676a'
  on-tertiary: '#ffffff'
  tertiary-container: '#008286'
  on-tertiary-container: '#f2ffff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b1'
  on-primary-fixed: '#410007'
  on-primary-fixed-variant: '#92001c'
  secondary-fixed: '#d7e3fa'
  secondary-fixed-dim: '#bbc7dd'
  on-secondary-fixed: '#101c2c'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#8ef3f7'
  tertiary-fixed-dim: '#70d6da'
  on-tertiary-fixed: '#002021'
  on-tertiary-fixed-variant: '#004f52'
  background: '#fff8f7'
  on-background: '#291716'
  surface-variant: '#fcdbd9'
typography:
  h1:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1140px
  gutter: 24px
---

## Brand & Style

This design system is built for high-impact digital publishing. The brand personality is assertive, energetic, and editorial, designed to evoke a sense of urgency and importance in the content it hosts. By blending a **Minimalist** foundation with **High-Contrast** accents, the system ensures that the "hot red" primary color acts as a navigational beacon without overwhelming the reader's focus.

The target audience consists of digital-native readers who value clarity and a sophisticated, "newsroom" aesthetic. The emotional response is intended to be one of excitement tempered by professional reliability. Every element is stripped back to its essential form, allowing the vibrant red to define the hierarchy and call-to-action path.

## Colors

The palette centers on a "hot red" that serves as the singular driver for engagement and brand recognition. To maintain high readability and a modern feel, this red is paired with a sophisticated range of subtle, cool-toned grays.

- **Primary (Vibrant Red):** Used strictly for high-priority interactions, branding, and active states.
- **Secondary (Subtle Gray):** Used for meta-information, secondary icons, and decorative borders.
- **Neutral Base:** A deep, near-black charcoal used for primary text to ensure maximum contrast against the warm-white background.
- **Surface Tones:** Extremely light grays and off-whites are used to differentiate content sections without the need for heavy borders.

## Typography

This design system utilizes a dual-font approach to balance editorial character with functional clarity. **Work Sans** provides a grounded, professional feel for headlines, while **Inter** ensures effortless readability for long-form body copy across all device types.

Typographic hierarchy is strict. Headlines use tight line-heights and slight negative letter-spacing to appear impactful and modern. Body text utilizes a generous 1.6x line-height to reduce eye strain during extended reading sessions. Labels and meta-tags are rendered in uppercase with increased letter-spacing to distinguish them clearly from the narrative flow.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain optimal line lengths for reading, transitioning to a fluid model for tablet and mobile. A 12-column system is used for landing pages, while a centered, single-column "Reading Lane" (approx. 720px) is mandated for article pages.

Spacing is governed by an 8px rhythmic scale. Generous vertical margins (`xl`) are used between major content sections to emphasize the minimalist aesthetic. Gutters are kept wide to provide "breathing room" around the vibrant red UI accents.

## Elevation & Depth

Depth in this design system is achieved through **Low-Contrast Outlines** and **Tonal Layering** rather than traditional shadows. This maintains the flat, minimalist aesthetic requested.

- **Level 0:** The primary background color.
- **Level 1:** Surface containers (like cards or sidebars) use a subtle gray fill (`surface_subtle_hex`) or a 1px border in a secondary gray.
- **Interactive Depth:** Only the primary red elements may feature a very subtle, high-diffusion shadow when hovered to indicate "lift." Most interactions are signaled by color shifts (e.g., Red to Dark Red) rather than elevation changes.

## Shapes

The design system adopts a **Soft** shape language. All primary buttons, input fields, and featured image containers utilize a subtle 4px (`0.25rem`) corner radius. This softens the aggressive nature of the "hot red" palette without veering into a playful or bubbly aesthetic. It maintains the professional, architectural feel of a modern blog. Large-scale components like containers or hero sections should remain sharp (0px) to anchor the layout.

## Components

### Buttons
Primary buttons are solid "hot red" with white text. They use the `label-sm` typographic style for clarity. Secondary buttons use a transparent background with a 2px "hot red" border and red text.

### Cards
Cards are borderless with a very subtle `surface_subtle_hex` background. Imagery within cards should occupy the top half of the container with a clean 0px top-radius to bleed into the edges, while the bottom corners follow the 4px system standard.

### Chips & Tags
Used for categories, these are small, pill-shaped elements with a light gray background and secondary gray text. When a tag is "active" or "selected," it switches to the primary red with white text.

### Input Fields
Minimalist underline or light gray fills. Focus states must be signaled by a 2px primary red bottom border or ring.

### Reading Progress Bar
A unique component for this design system: a 4px tall "hot red" bar at the very top of the viewport that fills horizontally as the user scrolls through an article.