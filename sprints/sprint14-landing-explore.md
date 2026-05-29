# Sprint 14: Landing Page + Explore Page

**Assignee:** TBD
**Goal:** Restyle the Landing Page and Explore Page using the design system tokens from Sprint 12. The Landing Page is the first thing visitors see — it needs to feel polished and inviting. The Explore Page shows public photos in a clean grid.
**Dependencies:** Sprint 12 (design system + navbar) must be merged first. No dependency on Sprints 13, 15, or 16 — can run in parallel with them.
**Parallel notes:** This sprint only modifies `LandingPage.jsx`, `LandingPage.css`, `ExplorePage.jsx`, `ExplorePage.css`, and the `ExploreCard` component. No conflicts expected with other sprints.

---

## Before You Start

**Check the README.md** at the project root for instructions on setting up the dev environment and running the app (both frontend and backend).

### Git Workflow

Your typical workflow once you receive a sprint should be:

1. Start on the `main` branch
2. `git pull` + `npm install` (in both root and `server/`) to make sure you are up to date
3. `git switch -c <your-branch>` — e.g. `yourname/sprint14`
4. Do `git add` & `git commit` while working (frequently + descriptive messages)
5. `git push origin <your-branch>` to push your local branch to GitHub
6. When you are done with your sprint, pull from main once more to resolve any merge conflicts early
7. Create a pull request on GitHub with a descriptive description, and then we can merge it safely!

---

## Background (read this first)

The Landing Page is the app's front door — it should communicate what Momento does and encourage visitors to sign up or explore. The Explore Page shows public photos from all users in a browsable grid. Both pages are accessible without authentication.

The current versions work but use inconsistent styling. This sprint applies the design system: CSS variables for all colors, `.btn` classes for buttons, `.card` for photo cards, and responsive grid layouts.

**Key concepts:**
- **Design tokens** — all colors, spacing, radii, and shadows come from CSS variables defined in `:root` (Sprint 12). Reference them as `var(--token-name)`.
- **Shared classes** — `.btn`, `.btn-primary`, `.btn-outline`, `.card`, `.tag` are defined in `App.css` (Sprint 12). Use them instead of writing custom styles.
- **Responsive grid** — use CSS Grid with `grid-template-columns: repeat(auto-fill, minmax(300px, 1fr))` (or similar) to get a grid that naturally reflows from 3 → 2 → 1 columns.
- **ExploreCard** — a component in `src/components/ExploreCard.jsx` that renders a single public photo card. It has built-in image error handling.

**Useful resources:**
- [CSS Grid (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
- Check `src/App.css` for all available shared classes
- Check `src/components/ExploreCard.jsx` to understand the existing card structure

---

## Tasks

### 1. Restyle the Landing Page

**Files:** `src/pages/LandingPage.jsx` + `src/pages/LandingPage.css`

#### Hero Section
- [ ] **Background:** Use a subtle gradient or wash with `var(--color-primary-lighter)` — e.g., `background: linear-gradient(135deg, var(--color-primary-lighter) 0%, var(--color-bg) 100%)`
- [ ] **Heading:** Large text (`var(--text-3xl)` or bigger), with a key word like "moments" or "memories" highlighted in `var(--color-primary)` using a `<span>` with that color
- [ ] **Subtitle:** Descriptive text in `var(--color-text-secondary)`, `var(--text-lg)`
- [ ] **CTA buttons:** Two buttons side by side with `var(--space-3)` gap:
  - "Get Started" — `btn btn-primary`, links to `/signup`
  - "Explore Photos" — `btn btn-outline`, links to `/explore`
- [ ] **Vertical spacing:** Use `var(--space-12)` or similar for generous hero padding

#### Feature Cards Section
- [ ] **Section title:** "How it works" or similar, centered, `var(--text-2xl)`, `var(--font-semibold)`
- [ ] **Three `.card` elements** arranged in a responsive grid (3 → 2 → 1 columns):
  - Each card has: an emoji or icon at the top, a title (`var(--font-semibold)`), and a short description (`var(--color-text-secondary)`)
  - Example cards: "Pin Your Photos" (map pin emoji), "Build Your Map" (map emoji), "Explore the Community" (globe emoji)
  - Cards use `.card` class with internal padding `var(--space-6)`
- [ ] **Responsive grid:** `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` with `gap: var(--space-6)`

#### General
- [ ] **Authenticated users:** Verify existing redirect behavior — authenticated users should be redirected to `/map` and never see the Landing Page
- [ ] **No horizontal scrollbar** at any viewport width

**How to test:**
1. Log out → navigate to `/` → Landing Page should load with hero + feature cards
2. Verify the hero has a subtle orange-tinted background
3. Click "Get Started" → navigates to `/signup`
4. Click "Explore Photos" → navigates to `/explore`
5. Resize: 1200px → 3 cards in a row; 768px → 2 cards; 480px → 1 card
6. Log in → navigate to `/` → should redirect to `/map`
7. No horizontal scrollbar at any width (check 375px specifically)

### 2. Restyle the Explore Page

**Files:** `src/pages/ExplorePage.jsx` + `src/pages/ExplorePage.css` + `src/components/ExploreCard.jsx` (if it has its own CSS)

- [ ] **Page background:** `var(--color-bg-page)`
- [ ] **Page title:** `var(--text-2xl)`, `var(--font-semibold)`, with appropriate margin using spacing tokens
- [ ] **Photo grid:**
  - Responsive grid: `grid-template-columns: repeat(auto-fill, minmax(300px, 1fr))` with `gap: var(--space-6)`
  - Reflows from 3 → 2 → 1 columns naturally
- [ ] **ExploreCard styling:**
  - Use `.card` class as a base
  - Image: consistent height (e.g., `200px`), `object-fit: cover`, `width: 100%`
  - Caption: `var(--color-text)`, `var(--text-sm)`
  - Username: `var(--color-secondary)`, `var(--text-sm)`
  - Date: `var(--color-text-secondary)`, `var(--text-xs)`
  - Card padding for text content: `var(--space-4)`
- [ ] **Broken image placeholder:**
  - When an image fails to load, show a placeholder div
  - Background: `var(--color-gray-100)`
  - Text: "Image unavailable" in `var(--color-gray-400)`, centered
  - Same height as normal images for consistent grid
- [ ] **"Load More" button:**
  - `btn btn-outline` or `btn btn-primary`
  - Centered below the grid with `var(--space-8)` margin
  - Hidden when there are no more pages
- [ ] **Empty state:** If no public photos exist, show a message like "No photos to explore yet" centered on the page

**How to test:**
1. Navigate to `/explore` (logged out) → public photos should display in a grid
2. Verify responsive grid: 3 columns at 1200px, 2 at 768px, 1 at 375px
3. Verify card styling: image fills top, text content below with proper spacing
4. If any images are broken → placeholder should show (not browser's broken image icon)
5. Click "Load More" → appends next page of photos
6. Click a photo card → navigates to `/photos/:id`
7. Username text should be blue (`var(--color-secondary)`)

---

## Bug Testing Checklist

- [ ] Landing: loads when not authenticated
- [ ] Landing: authenticated user redirected to /map
- [ ] Landing: "Get Started" → /signup
- [ ] Landing: "Explore Photos" → /explore
- [ ] Landing: responsive at 1200px, 768px, 480px, 375px
- [ ] Landing: no horizontal scrollbar at any width
- [ ] Explore: loads without auth at /explore
- [ ] Explore: public photos display with thumbnails
- [ ] Explore: broken/missing images show placeholder (not broken icon)
- [ ] Explore: "Load More" fetches next page
- [ ] Explore: click card → navigates to /photos/:id
- [ ] Explore: responsive grid at all widths
- [ ] Explore: works when logged out

---

## Merge Conflict Notes

**Low conflict risk.** This sprint modifies Landing and Explore page files. The only potential conflict point is if Sprint 11 or another sprint also modified `ExploreCard.jsx` — in that case, merge both changes and apply the new design system styling on top.

---

## Deliverables Checklist

- [ ] Landing Page hero with orange-tinted background, highlighted heading word, two CTA buttons
- [ ] Landing Page feature cards in responsive grid (3 → 2 → 1 columns)
- [ ] Landing Page redirects authenticated users to /map
- [ ] Explore Page uses `var(--color-bg-page)` background
- [ ] Explore cards use `.card` class with design system colors
- [ ] Broken image placeholders use `var(--color-gray-100)` background
- [ ] "Load More" button uses `.btn` styling
- [ ] Username text uses `var(--color-secondary)`
- [ ] Both pages responsive with no overflow
- [ ] No hardcoded color values — all use `var(--*)` tokens

## File Structure

```
src/
├── pages/
│   ├── LandingPage.jsx          (modified — hero + feature cards redesign)
│   ├── LandingPage.css          (modified — replace hardcoded styles)
│   ├── ExplorePage.jsx          (modified — grid layout + styling)
│   └── ExplorePage.css          (modified — replace hardcoded styles)
└── components/
    └── ExploreCard.jsx          (modified — apply .card class + design tokens)
```
