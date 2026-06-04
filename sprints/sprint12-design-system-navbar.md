# Sprint 12: Design System Foundation + Navbar

**Assignee:** Anthony
**Goal:** Establish a cohesive CSS design system (CSS custom properties, shared utility classes, Inter font) and restyle the Navbar. Every subsequent sprint depends on the tokens defined here.
**Dependencies:** Sprints 1–11 (all merged into main).
**Parallel notes:** This sprint **must merge first** — Sprints 13–16 all consume the CSS variables and shared classes defined here. The only files modified are `src/index.css`, `src/App.css`, `src/components/Navbar.jsx`, and `src/components/Navbar.css` — no conflicts expected with other sprints.

---

## Before You Start

**Check the README.md** at the project root for instructions on setting up the dev environment and running the app (both frontend and backend).

### Git Workflow

Your typical workflow once you receive a sprint should be:

1. Start on the `main` branch
2. `git pull` + `npm install` (in both root and `server/`) to make sure you are up to date
3. `git switch -c <your-branch>` — e.g. `yourname/sprint12`
4. Do `git add` & `git commit` while working (frequently + descriptive messages)
5. `git push origin <your-branch>` to push your local branch to GitHub
6. When you are done with your sprint, pull from main once more to resolve any merge conflicts early
7. Create a pull request on GitHub with a descriptive description, and then we can merge it safely!

---

## Background (read this first)

The app is functionally complete but has no design system — every CSS file uses hardcoded colors (like `#4a6cf7`, `#007bff`, `#1976d2`), inconsistent spacing, and mismatched shadows/radii. This sprint defines a single source of truth for all visual tokens and provides shared utility classes so the rest of the team can restyle their pages without reinventing styles.

**Key concepts:**
- **CSS custom properties (variables)** — defined once in `:root {}` and referenced everywhere as `var(--token-name)`. Changing the value in one place updates the entire app.
- **Shared utility classes** — `.btn`, `.btn-primary`, `.card`, `.input`, etc. defined in `App.css` so every sprint can use consistent buttons, inputs, and cards without duplicating styles.
- **Inter font** — a clean sans-serif from Google Fonts, imported via `@import` in `index.css`.

**Useful resources:**
- [CSS Custom Properties (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [Google Fonts — Inter](https://fonts.google.com/specimen/Inter)
- [useLocation hook (React Router)](https://reactrouter.com/en/main/hooks/use-location) — for highlighting the active nav link

---

## Design System — Color Palette

**Primary Orange** (warm, Claude-inspired):
| Token | Value | Use |
|-------|-------|-----|
| `--color-primary` | `#D4713D` | Buttons, active states, key CTAs |
| `--color-primary-hover` | `#BF6235` | Hover/pressed states |
| `--color-primary-light` | `#FDF0E9` | Tag chips, tinted backgrounds |
| `--color-primary-lighter` | `#FEF7F3` | Page-level subtle tint |

**Secondary Blue**:
| Token | Value | Use |
|-------|-------|-----|
| `--color-secondary` | `#3B7DD8` | Accent links, info elements |
| `--color-secondary-hover` | `#2E6ABF` | Hover states |
| `--color-secondary-light` | `#EBF2FC` | Light accent backgrounds |

**Neutrals**:
| Token | Value |
|-------|-------|
| `--color-gray-50` | `#F9FAFB` |
| `--color-gray-100` | `#F3F4F6` |
| `--color-gray-200` | `#E5E7EB` |
| `--color-gray-300` | `#D1D5DB` |
| `--color-gray-400` | `#9CA3AF` |
| `--color-gray-500` | `#6B7280` |
| `--color-gray-600` | `#4B5563` |
| `--color-gray-700` | `#374151` |
| `--color-gray-800` | `#1F2937` |
| `--color-gray-900` | `#111827` |

**Semantic**:
| Token | Value | Use |
|-------|-------|-----|
| `--color-error` | `#DC2626` | Delete, errors |
| `--color-error-hover` | `#B91C1C` | Delete hover |
| `--color-error-light` | `#FEF2F2` | Error backgrounds |
| `--color-success` | `#16A34A` | Success states |
| `--color-success-light` | `#F0FDF4` | Success backgrounds |

**Surfaces**:
| Token | Value |
|-------|-------|
| `--color-bg` | `#FFFFFF` |
| `--color-bg-page` | `#F9FAFB` |
| `--color-border` | `#E5E7EB` |
| `--color-text` | `#111827` |
| `--color-text-secondary` | `#6B7280` |
| `--color-overlay` | `rgba(0, 0, 0, 0.5)` |

---

## Design System — Typography, Spacing, Shadows, Radii

**Typography** (Inter from Google Fonts):
```
--font-family: 'Inter', system-ui, -apple-system, sans-serif;
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 2rem;        /* 32px */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

**Spacing** (4px base):
```
--space-1: 4px;   --space-2: 8px;   --space-3: 12px;
--space-4: 16px;  --space-5: 20px;  --space-6: 24px;
--space-8: 32px;  --space-10: 40px; --space-12: 48px;
```

**Border Radius**:
```
--radius-sm: 4px;  --radius-md: 8px;  --radius-lg: 12px;
--radius-xl: 16px; --radius-full: 9999px;
```

**Shadows**:
```
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.15);
```

**Z-index**:
```
--z-dropdown: 100;  --z-sticky: 200;  --z-navbar: 500;
--z-modal-backdrop: 900;  --z-modal: 1000;
```

---

## Tasks

### 1. Add CSS variables and Inter font to `src/index.css`

**File:** `src/index.css`

- [ ] Add `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');` at the very top of the file
- [ ] Add a `:root { }` block containing ALL CSS variables listed above (colors, typography, spacing, radii, shadows, z-index)
- [ ] Update the `body` rule to use the new tokens:
  ```css
  body {
    margin: 0;
    font-family: var(--font-family);
    font-size: var(--text-base);
    color: var(--color-text);
    background-color: var(--color-bg);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  ```
- [ ] Add a universal box-sizing rule:
  ```css
  *, *::before, *::after {
    box-sizing: border-box;
  }
  ```

**How to test:**
1. Open DevTools → Elements → select `:root` → verify all `--color-*`, `--text-*`, `--space-*`, etc. variables appear in the Styles panel
2. Check the Network tab → confirm `fonts.googleapis.com` request for Inter
3. Inspect any text on the page → `font-family` should resolve to `Inter`

### 2. Define shared utility classes in `src/App.css`

**File:** `src/App.css`

Delete the old Vite template styles (the rotating logo animation, `.App` class, etc.) and replace with these shared classes:

- [ ] **`.btn`** — Base button reset:
  ```css
  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 20px;
    font-size: var(--text-sm);
    font-weight: var(--font-semibold);
    font-family: inherit;
    border: 2px solid transparent;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: all 0.2s ease;
    text-decoration: none;
    line-height: 1;
  }
  .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  ```

- [ ] **`.btn-primary`** — Orange filled button:
  ```css
  .btn-primary {
    background-color: var(--color-primary);
    color: white;
    border-color: var(--color-primary);
  }
  .btn-primary:hover:not(:disabled) {
    background-color: var(--color-primary-hover);
    border-color: var(--color-primary-hover);
  }
  ```

- [ ] **`.btn-secondary`** — Blue filled button:
  ```css
  .btn-secondary {
    background-color: var(--color-secondary);
    color: white;
    border-color: var(--color-secondary);
  }
  .btn-secondary:hover:not(:disabled) {
    background-color: var(--color-secondary-hover);
    border-color: var(--color-secondary-hover);
  }
  ```

- [ ] **`.btn-outline`** — Outlined orange button:
  ```css
  .btn-outline {
    background-color: transparent;
    color: var(--color-primary);
    border-color: var(--color-primary);
  }
  .btn-outline:hover:not(:disabled) {
    background-color: var(--color-primary);
    color: white;
  }
  ```

- [ ] **`.btn-danger`** — Red button for destructive actions:
  ```css
  .btn-danger {
    background-color: var(--color-error);
    color: white;
    border-color: var(--color-error);
  }
  .btn-danger:hover:not(:disabled) {
    background-color: var(--color-error-hover);
    border-color: var(--color-error-hover);
  }
  ```

- [ ] **`.btn-ghost`** — Minimal button for secondary actions:
  ```css
  .btn-ghost {
    background-color: transparent;
    color: var(--color-text-secondary);
    border-color: transparent;
  }
  .btn-ghost:hover:not(:disabled) {
    background-color: var(--color-gray-100);
    color: var(--color-text);
  }
  ```

- [ ] **`.input`** — Styled text input:
  ```css
  .input {
    width: 100%;
    padding: 10px 12px;
    font-size: var(--text-sm);
    font-family: inherit;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    background-color: var(--color-bg);
    color: var(--color-text);
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }
  .input:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(212, 113, 61, 0.15);
  }
  .input::placeholder {
    color: var(--color-gray-400);
  }
  ```

- [ ] **`.card`** — Card container:
  ```css
  .card {
    background-color: var(--color-bg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    overflow: hidden;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
  }
  .card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
  }
  ```

- [ ] **`.tag`** — Tag/chip pill:
  ```css
  .tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    font-size: var(--text-xs);
    font-weight: var(--font-medium);
    color: var(--color-primary);
    background-color: var(--color-primary-light);
    border-radius: var(--radius-full);
  }
  ```

- [ ] **`.overlay`** — Modal backdrop:
  ```css
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: var(--color-overlay);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: var(--z-modal-backdrop);
  }
  ```

- [ ] **`.modal`** — Modal content container:
  ```css
  .modal {
    background-color: var(--color-bg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    z-index: var(--z-modal);
    max-height: 90vh;
    overflow-y: auto;
  }
  ```

**How to test:**
1. Temporarily add a test element to any page (e.g., `<button className="btn btn-primary">Test</button>`) and confirm it renders as an orange button with white text
2. Test hover states — `.btn-primary` should darken on hover
3. Test `.input` — should have a gray border that turns orange on focus
4. Test `.card` — should have a subtle shadow that lifts on hover
5. Remove test elements after verifying

### 3. Restyle the Navbar

**Files:** `src/components/Navbar.jsx` + `src/components/Navbar.css`

The current Navbar uses hardcoded colors and basic styling. Redesign it to use design tokens:

- [ ] **Logo:** "Momento" text, styled with:
  - `font-weight: var(--font-bold)`
  - `color: var(--color-primary)`
  - `font-size: var(--text-xl)`
  - Links to `/` (or `/map` if authenticated)

- [ ] **Nav links:** Use `useLocation()` from React Router to detect the current path:
  - Add an `.active` class to the link matching the current route
  - Active link: `color: var(--color-primary)`, subtle bottom border or background highlight
  - Hover: smooth color transition
  - **Authenticated links:** Map | Gallery | Explore
  - **Unauthenticated links:** Explore

- [ ] **Right-side user area:**
  - **Authenticated:** Display username + Logout button using `btn btn-ghost`
  - **Unauthenticated:** Login (`btn btn-outline`) + Sign Up (`btn btn-primary`)

- [ ] **Navbar container styling:**
  - `background-color: var(--color-bg)`
  - `box-shadow: var(--shadow-sm)`
  - `z-index: var(--z-navbar)`
  - `position: sticky; top: 0;`
  - Consistent padding using spacing tokens
  - Flexbox layout: logo left, links center, user area right

- [ ] **Responsive:** Ensure links don't clip or overflow on narrow viewports. At minimum, reduce padding and font size on mobile. A hamburger menu is optional but not required.

**How to test:**
1. Log in → verify: "Momento" logo in orange, Map/Gallery/Explore links visible, username + Logout button on the right
2. Click each nav link → active link should be highlighted (different color or underline)
3. Click Logout → redirects to `/`, navbar shows Explore + Login + Sign Up
4. Log out → verify: Explore link visible, Login (outlined) + Sign Up (filled orange) buttons on the right
5. Resize browser to mobile width → links should not overflow or clip
6. Navigate to each page → active link should update correctly

---

## Merge Conflict Notes

**Very low conflict risk.** This sprint modifies:
- `src/index.css` — usually only touched during initial setup, unlikely to conflict
- `src/App.css` — replacing old template styles with new shared classes. If another sprint added styles here, just keep both.
- `src/components/Navbar.jsx` + `Navbar.css` — if another sprint added nav links, merge them in using the new styling patterns

**Important:** This sprint must merge before Sprints 13–16 start, since they all depend on the CSS variables and shared classes defined here.

---

## Deliverables Checklist

- [ ] `:root` block in `index.css` with all CSS variables (colors, typography, spacing, radii, shadows, z-index)
- [ ] Inter font loads from Google Fonts
- [ ] `body` uses `var(--font-family)`, `var(--color-text)`, `var(--color-bg)`
- [ ] `App.css` contains shared classes: `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn-danger`, `.btn-ghost`, `.input`, `.card`, `.tag`, `.overlay`, `.modal`
- [ ] Navbar uses design tokens throughout (no hardcoded colors)
- [ ] Navbar shows correct links for authenticated vs. unauthenticated users
- [ ] Active nav link is visually highlighted based on current route
- [ ] Logout button works and redirects to `/`
- [ ] Navbar is sticky, has shadow, uses correct z-index
- [ ] No visual regressions on pages not yet restyled (they still use hardcoded colors — that's fine for now)

## File Structure

```
src/
├── index.css                    (modified — add :root variables + Inter font import)
├── App.css                      (modified — replace with shared utility classes)
└── components/
    ├── Navbar.jsx               (modified — full redesign with design tokens)
    └── Navbar.css               (modified — full restyle)
```
