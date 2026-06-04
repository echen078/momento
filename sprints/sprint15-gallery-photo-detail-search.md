# Sprint 15: Gallery, Photo Detail & Search

**Assignee:** Ellen
**Goal:** Restyle the Gallery page, Photo Detail page/modal, SearchBar, and TagInput using the design system tokens from Sprint 12. These are interconnected components — tags flow between the gallery grid, search filters, and detail views.
**Dependencies:** Sprint 12 (design system + navbar) must be merged first. No dependency on Sprints 13, 14, or 16 — can run in parallel with them.
**Parallel notes:** This sprint modifies Gallery, PhotoDetail, SearchBar, PhotoDetailModal, and TagInput files. No other sprint should be touching these files, so conflicts are unlikely.

---

## Before You Start

**Check the README.md** at the project root for instructions on setting up the dev environment and running the app (both frontend and backend).

### Git Workflow

Your typical workflow once you receive a sprint should be:

1. Start on the `main` branch
2. `git pull` + `npm install` (in both root and `server/`) to make sure you are up to date
3. `git switch -c <your-branch>` — e.g. `yourname/sprint15`
4. Do `git add` & `git commit` while working (frequently + descriptive messages)
5. `git push origin <your-branch>` to push your local branch to GitHub
6. When you are done with your sprint, pull from main once more to resolve any merge conflicts early
7. Create a pull request on GitHub with a descriptive description, and then we can merge it safely!

---

## Background (read this first)

The Gallery page shows the logged-in user's photos with search/filter capabilities. The SearchBar provides text search, date range, and tag filtering. The PhotoDetailPage and PhotoDetailModal show a single photo with its metadata, tags, and edit controls. TagInput is a reusable component for adding/removing tag chips.

All of these currently work but use inconsistent colors (various blues like `#4a6cf7`, `#007bff`) and hardcoded spacing. This sprint replaces everything with the orange+neutral design system from Sprint 12.

**Key concepts:**
- **Tag flow:** Tags appear in multiple places — on gallery cards, as filter chips in SearchBar, in the detail view, and in TagInput. All should use the same `.tag` class (orange pill styling).
- **URL sync:** The gallery currently syncs tag filters to the URL (`?tags=food,beach`). Don't break this behavior — just restyle the UI around it.
- **Shared classes** — `.btn`, `.btn-primary`, `.btn-outline`, `.btn-danger`, `.card`, `.tag`, `.input`, `.overlay`, `.modal` are defined in `App.css` (Sprint 12).

**Useful resources:**
- Check `src/App.css` for all available shared classes
- Check the existing component files to understand current structure before modifying

---

## Tasks

### 1. Restyle the Gallery page

**Files:** `src/pages/GalleryPage.jsx` + `src/pages/GalleryPage.css`

- [ ] **Page background:** `var(--color-bg-page)`
- [ ] **Page title:** "My Gallery" or "Your Photos" — `var(--text-2xl)`, `var(--font-semibold)`
- [ ] **Photo grid:**
  - Responsive grid: `grid-template-columns: repeat(auto-fill, minmax(300px, 1fr))` with `gap: var(--space-6)`
  - Reflows from 3 → 2 → 1 columns
- [ ] **Gallery cards:**
  - Use `.card` class as a base
  - Image: consistent height (e.g., `200px`), `object-fit: cover`, `width: 100%`
  - Card body padding: `var(--space-4)`
  - Caption: `var(--color-text)`, `var(--text-sm)`
  - Tags on cards: use `.tag` class (orange pills) — clicking a tag should still add it to the filter
  - Date: `var(--color-text-secondary)`, `var(--text-xs)`
- [ ] **Empty state:** "No photos yet" message centered with `var(--color-text-secondary)`, maybe with a subtle icon or suggestion to upload from the map

**How to test:**
1. Log in → navigate to `/gallery` → your photos should appear in a styled grid
2. Cards should have images on top, text below with proper spacing
3. Tags on cards should be orange pills (`.tag` class)
4. Click a tag on a card → it should add to the filter (existing behavior preserved)
5. Resize: 3 → 2 → 1 columns
6. With no photos → "No photos yet" message appears

### 2. Restyle the SearchBar

**Files:** `src/components/SearchBar.jsx` + `src/components/SearchBar.css`

- [ ] **Search input:** Use `.input` class, with a search icon or placeholder text "Search photos..."
- [ ] **Date inputs:** Style consistently with `.input` class (same border, focus ring, border-radius)
- [ ] **Active filter chips:** Displayed below the search bar when filters are active:
  - Background: `var(--color-primary-light)`
  - Text: `var(--color-primary)`
  - Border-radius: `var(--radius-full)` (pill shape)
  - × (close) button on each chip: hover darkens to `var(--color-primary-hover)` or shows a subtle background change
- [ ] **"Clear all" link:** `var(--color-text-secondary)`, `text-decoration: underline`, positioned after filter chips
- [ ] **Result count:** Style in `var(--color-text-secondary)`, `var(--text-sm)`

**How to test:**
1. Type in the search bar → input should have orange focus ring
2. Add tag filters → chips should appear as orange pills below the search
3. Click × on a chip → that filter is removed
4. Click "Clear all" → all filters removed, URL cleared
5. Date inputs should match the same styling as the search input

### 3. Restyle PhotoDetailPage + PhotoDetailModal

**Files:** `src/pages/PhotoDetailPage.jsx` + `src/pages/PhotoDetailPage.css` + `src/components/PhotoDetailModal.jsx` + `src/components/PhotoDetailModal.css`

#### PhotoDetailPage (standalone `/photos/:id` route):
- [ ] **Container:** `.card` class, `max-width: 900px`, centered with `margin: 0 auto`
- [ ] **Page background:** `var(--color-bg-page)`
- [ ] **Image:** `max-height: 500px`, `object-fit: cover` (or `contain` to avoid cropping), `width: 100%`, `border-radius: var(--radius-md)` on top
- [ ] **Caption:** `var(--text-lg)`, `var(--font-medium)`
- [ ] **Tags:** `.tag` class (orange pills)
- [ ] **Metadata** (date, location, etc.): `var(--color-text-secondary)`, `var(--text-sm)`
- [ ] **Delete button:** `btn btn-danger` — only visible if user owns the photo
- [ ] **Edit controls** (caption, tags, public/private toggle): inputs use `.input`, buttons use `.btn` variants
- [ ] **Public/private badge:** Small pill showing "Public" (`var(--color-success)` bg) or "Private" (`var(--color-gray-200)` bg)

#### PhotoDetailModal (opened from Gallery):
- [ ] Use `.overlay` class for the backdrop
- [ ] Use `.modal` class for the content container
- [ ] Same internal layout as PhotoDetailPage (image, caption, tags, controls)
- [ ] Close button (×) in top-right corner: `var(--color-text-secondary)`, hover → `var(--color-text)`
- [ ] Clicking the overlay backdrop should close the modal

**How to test:**
1. Go to Gallery → click a photo → PhotoDetailModal opens
2. Modal has dark overlay backdrop, white modal content on top
3. All tags are orange pills
4. Delete button is red (`.btn-danger`)
5. Close button works (×), clicking backdrop closes modal
6. Navigate directly to `/photos/:id` → PhotoDetailPage loads in a centered card
7. Owner sees edit/delete controls; non-owner sees read-only view
8. Public/private toggle works on owned photos

### 4. Restyle TagInput

**Files:** `src/components/TagInput.jsx` + `src/components/TagInput.css`

- [ ] **Tag chips:** Use `.tag` class styling (orange background, orange text, pill shape)
  - Replace any existing blue chip styling
  - × (remove) button on each chip: default `var(--color-primary)`, hover → `var(--color-error)`
- [ ] **Text input:** Use `.input` class styling
- [ ] **Suggestion buttons** (if present): `var(--color-gray-100)` background, hover → `var(--color-primary-light)` background
- [ ] **Overall container:** Subtle border or background to visually group the input + chips

**How to test:**
1. Go to a photo detail page or upload modal that has TagInput
2. Existing tags should show as orange pills (not blue)
3. Hover over × on a tag → should turn red
4. Type a tag and press Enter → tag added as a new orange pill
5. Press Enter → should add the tag, NOT submit any parent form
6. Suggestion buttons (if any) should have gray backgrounds that lighten on hover

---

## Bug Testing Checklist

- [ ] Gallery loads user's photos
- [ ] Click tag on card → adds filter → chip appears below search → URL updates `?tags=...`
- [ ] Click × on chip → removes that specific filter
- [ ] Multiple tags filter additively
- [ ] Refresh with `?tags=food,beach` → filters preserved and applied
- [ ] Search text + date range work together with tags
- [ ] "Clear all" resets all filters, URL clears
- [ ] Click photo card → PhotoDetailModal opens with all info
- [ ] Delete from modal → photo removed from gallery list
- [ ] /photos/:id direct URL loads PhotoDetailPage correctly
- [ ] Owner sees edit/delete controls; non-owner sees read-only
- [ ] Public/private toggle works on owned photos
- [ ] Tag editing (add/remove) on detail page works and saves
- [ ] Responsive grid: 3 → 2 → 1 columns
- [ ] Empty gallery shows "No photos yet" message

---

## Merge Conflict Notes

**Low conflict risk.** This sprint modifies Gallery, PhotoDetail, SearchBar, and TagInput files. These are not touched by other design sprints (13, 14, 16). The only potential conflict is if Sprint 11 (integration wiring) made changes to GalleryPage or PhotoDetailPage — if so, keep the behavioral changes from Sprint 11 and apply the styling changes from this sprint on top.

---

## Deliverables Checklist

- [ ] Gallery page uses `var(--color-bg-page)` background and `.card` class for photo cards
- [ ] Gallery tags use `.tag` class (orange pills), clicking still filters
- [ ] SearchBar inputs use `.input` class with orange focus ring
- [ ] Filter chips use `var(--color-primary-light)` bg, `var(--color-primary)` text
- [ ] PhotoDetailPage is a centered `.card` with `max-width: 900px`
- [ ] PhotoDetailModal uses `.overlay` + `.modal` classes
- [ ] Delete button uses `.btn-danger`
- [ ] TagInput chips are orange (replacing old blue), × hover turns red
- [ ] All pages responsive (3 → 2 → 1 columns)
- [ ] No hardcoded color values — all use `var(--*)` tokens
- [ ] URL-based tag filtering still works correctly after restyling

## File Structure

```
src/
├── pages/
│   ├── GalleryPage.jsx          (modified — grid layout + design tokens)
│   ├── GalleryPage.css          (modified — replace hardcoded styles)
│   ├── PhotoDetailPage.jsx      (modified — centered card + design tokens)
│   └── PhotoDetailPage.css      (modified — replace hardcoded styles)
└── components/
    ├── SearchBar.jsx            (modified — input + chip styling)
    ├── SearchBar.css            (modified — replace hardcoded styles)
    ├── PhotoDetailModal.jsx     (modified — overlay + modal classes)
    ├── PhotoDetailModal.css     (modified — replace hardcoded styles)
    ├── TagInput.jsx             (modified — orange chips replacing blue)
    └── TagInput.css             (modified — replace hardcoded styles)
```
