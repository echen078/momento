# Sprint 16: Map Page

**Assignee:** Gokul
**Goal:** Restyle the Map page UI — the upload modal, map view toggle, map pin popups, and any surrounding chrome — using the design system tokens from Sprint 12. The map itself (Leaflet tiles) stays as-is, but everything around it should match the orange+neutral design system.
**Dependencies:** Sprint 12 (design system + navbar) must be merged first. No dependency on Sprints 13, 14, or 15 — can run in parallel with them.
**Parallel notes:** This sprint modifies Map components, PhotoUpload, and MapViewToggle. No other design sprint touches these files.

---

## Before You Start

**Check the README.md** at the project root for instructions on setting up the dev environment and running the app (both frontend and backend).

### Git Workflow

Your typical workflow once you receive a sprint should be:

1. Start on the `main` branch
2. `git pull` + `npm install` (in both root and `server/`) to make sure you are up to date
3. `git switch -c <your-branch>` — e.g. `yourname/sprint16`
4. Do `git add` & `git commit` while working (frequently + descriptive messages)
5. `git push origin <your-branch>` to push your local branch to GitHub
6. When you are done with your sprint, pull from main once more to resolve any merge conflicts early
7. Create a pull request on GitHub with a descriptive description, and then we can merge it safely!

---

## Background (read this first)

The Map page is the app's core screen — users click locations to upload photos, and their pins are displayed on the map. There's also a community heatmap toggle. The map tiles themselves (Leaflet/OpenStreetMap) don't need restyling, but the surrounding UI elements do:

- **PhotoUpload modal** — appears when the user clicks a location on the map. Currently works but uses inconsistent button/input styling.
- **MapViewToggle** — switches between "My Photos" and "Community Heatmap". Currently uses blue (`#1976d2`) which needs to change to the orange design system.
- **MapPin popups** — Leaflet popups that show when clicking a photo pin. These can be styled with CSS.
- **Period buttons** — Week/Month/Year/All time filters for the heatmap view.

**Current state (things that already work):**
- PhotoUpload modal is already positioned outside the Leaflet container (z-index 2000)
- TagInput Enter fix is in place (Enter adds tag, doesn't submit form)
- Map takes 100vh, centered on LA (34.0522, -118.2437)
- HEIC upload support exists

**Key concepts:**
- **Leaflet z-index** — Leaflet has its own z-index stacking. The modal must stay above the map at all times. The current z-index of 2000 works, but verify it still layers correctly after restyling.
- **Shared classes** — `.btn`, `.btn-primary`, `.btn-outline`, `.btn-danger`, `.card`, `.tag`, `.input`, `.overlay`, `.modal` are defined in `App.css` (Sprint 12).
- **Leaflet popup styling** — Leaflet popups can be styled by targeting `.leaflet-popup-content-wrapper` and `.leaflet-popup-content` in CSS.

**Useful resources:**
- [Leaflet popup styling](https://leafletjs.com/reference.html#popup)
- Check `src/App.css` for all available shared classes
- Check `src/components/Map/` for existing Map component structure

---

## Tasks

### 1. Restyle the PhotoUpload modal

**Files:** `src/components/PhotoUpload.jsx` + `src/components/PhotoUpload.css`

- [ ] **Overlay:** Use `.overlay` class (or equivalent styling) — fixed fullscreen, `var(--color-overlay)` background, z-index high enough to sit above the map and navbar
- [ ] **Modal container:** Use `.modal` class as a base:
  - White background, `var(--radius-lg)`, `var(--shadow-lg)`
  - `max-width: 500px`, `width: 90%` for responsive sizing
  - Padding: `var(--space-6)` or `var(--space-8)`
- [ ] **Title:** "Upload Photo" — `var(--text-xl)`, `var(--font-semibold)`
- [ ] **File input area:**
  - Style the file drop zone / file input button
  - Use `var(--color-gray-100)` background for the drop zone, dashed `var(--color-border)` border
  - Hover: `var(--color-primary-light)` background
  - Selected file name: `var(--text-sm)`, `var(--color-text-secondary)`
- [ ] **Caption input:** Use `.input` class
- [ ] **Tags:** TagInput component should already be restyled by Sprint 15 — if not, apply `.tag` styling here too
- [ ] **"Share publicly" checkbox:** Clean label with `var(--text-sm)`, properly spaced
- [ ] **Location display:** Show selected coordinates in `var(--color-text-secondary)`, `var(--text-sm)` — maybe with a small map pin icon
- [ ] **Action buttons:**
  - "Upload" — `btn btn-primary`
  - "Cancel" — `btn btn-ghost` or `btn btn-outline`
  - Buttons side by side with `gap: var(--space-3)`
- [ ] **Validation errors:** `var(--color-error)` text, `var(--text-sm)`
- [ ] **Loading state:** Button shows "Uploading..." and is disabled during upload

**How to test:**
1. Click a location on the map → upload modal should appear above the map
2. Modal has dark overlay, white content, orange "Upload" button
3. Select a file → file name appears
4. Fill caption, add tags, toggle public → submit → pin appears on map
5. Submit without file → validation error in red
6. Submit without location selected → validation error
7. Click Cancel → modal closes, form resets
8. Resize to mobile → modal should be nearly full-width with padding

### 2. Restyle the MapViewToggle

**Files:** `src/components/Map/MapViewToggle.jsx` + `src/components/Map/MapViewToggle.css`

- [ ] **Toggle container:** Positioned on the map (e.g., top-right), with `var(--shadow-md)`, `var(--radius-lg)`, white background
- [ ] **Toggle buttons:** "My Photos" and "Community Heatmap":
  - Active tab: `var(--color-primary)` background, white text
  - Inactive tab: white background, `var(--color-text-secondary)` text
  - Replace any existing blue (`#1976d2`) with orange (`var(--color-primary)`)
  - Smooth transition between states
- [ ] **Period filter buttons** (Week/Month/Year/All — visible in heatmap mode):
  - Active: `var(--color-primary-light)` background, `var(--color-primary)` text
  - Inactive: transparent background, `var(--color-text-secondary)` text
  - `var(--radius-full)` for pill shape
  - `var(--text-xs)` or `var(--text-sm)` font size
- [ ] **Z-index:** Must be above the map tiles but below modals. Use a value between Leaflet's default and `var(--z-modal-backdrop)`

**How to test:**
1. Load the map page → toggle should be visible on the map
2. Default: "My Photos" tab is active (orange)
3. Click "Community Heatmap" → tab switches to active (orange), heatmap appears
4. Period buttons appear in heatmap mode: Week/Month/Year/All
5. Active period button is highlighted in light orange
6. No blue (`#1976d2`) visible anywhere in the toggle
7. Toggle layers correctly above map but below the upload modal

### 3. Style MapPin popups

**Files:** `src/components/Map/MapPin.jsx` + `src/components/Map/Map.css`

- [ ] **Popup content wrapper:** Override Leaflet's default popup styling:
  ```css
  .leaflet-popup-content-wrapper {
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    padding: 0;
  }
  .leaflet-popup-content {
    margin: 0;
    font-family: var(--font-family);
  }
  ```
- [ ] **Pin popup content:**
  - Photo thumbnail: rounded top corners, `object-fit: cover`
  - Caption: `var(--text-sm)`, `var(--font-medium)`, padding `var(--space-3)`
  - Tags: `.tag` class (small orange pills)
  - Date: `var(--color-text-secondary)`, `var(--text-xs)`
  - "View Details" link: `var(--color-secondary)`, `var(--text-sm)`

**How to test:**
1. Upload a photo → pin appears on map
2. Click the pin → popup opens with styled content
3. Popup has rounded corners, shadow, clean typography
4. Tags in popup are orange pills
5. Popup doesn't clip or overflow

### 4. General Map page polish

**Files:** `src/components/Map/Map.jsx` + `src/components/Map/Map.css`

- [ ] **Map container:** Ensure full viewport height minus navbar height
- [ ] **Click instruction:** If the map has any instructional text (like "Click to add a photo"), style it with `var(--color-text-secondary)`, `var(--text-sm)`
- [ ] **Z-index stacking:** Verify the stacking order is correct:
  1. Map tiles (base)
  2. Map controls / MapViewToggle (above tiles)
  3. Navbar (above map, `var(--z-navbar)`)
  4. Upload modal overlay + modal (above everything)
- [ ] **No leftover hardcoded colors:** Search `Map.css`, `MapViewToggle.css`, `PhotoUpload.css`, `MapPin.jsx` for hardcoded hex colors and replace with `var(--*)` tokens

**How to test:**
1. Load `/map` → full viewport map with toggle overlay
2. Navbar is above the map (not hidden behind it)
3. Click location → modal opens above everything
4. Close modal → map is interactable again
5. Switch to heatmap view → heatmap renders, toggle stays above
6. No blue/purple hardcoded colors visible anywhere on the map page

---

## Bug Testing Checklist

- [ ] Click map → location selected → upload modal opens above map
- [ ] Upload JPEG/PNG/WEBP with caption + tags → pin appears
- [ ] Upload without file → validation error
- [ ] Upload without location → validation error
- [ ] TagInput Enter adds tag, doesn't submit form
- [ ] Cancel closes modal, resets form
- [ ] "My Photos" ↔ "Community Heatmap" toggle works
- [ ] Period buttons (Week/Month/Year/All) filter heatmap
- [ ] Photo pins show popup on click
- [ ] Modal z-index above map + navbar
- [ ] HEIC upload converts and displays
- [ ] Map is still fully interactive (pan, zoom) when modal is closed
- [ ] No hardcoded blue (#1976d2, #007bff, #4a6cf7) colors visible on the map page

---

## Merge Conflict Notes

**Low conflict risk.** This sprint only modifies Map-related components and PhotoUpload. No other design sprint touches these files. If Sprint 15 restyled TagInput (used inside PhotoUpload), the styles should complement each other — TagInput's `.tag` styling flows into the upload modal automatically.

---

## Deliverables Checklist

- [ ] PhotoUpload modal uses `.overlay` + `.modal` + `.btn-primary` styling
- [ ] MapViewToggle uses `var(--color-primary)` instead of blue `#1976d2`
- [ ] Period buttons use orange design system colors
- [ ] MapPin popups have rounded corners, shadows, and design system typography
- [ ] Tags in popups use `.tag` class
- [ ] File input area has clean styling with hover state
- [ ] All action buttons use `.btn` variants
- [ ] Z-index stacking is correct (tiles < toggle < navbar < modal)
- [ ] No hardcoded color values — all use `var(--*)` tokens
- [ ] Map is fully functional after restyling (upload, pins, heatmap, popups)

## File Structure

```
src/
└── components/
    ├── Map/
    │   ├── Map.jsx              (modified — minor polish)
    │   ├── Map.css              (modified — popup overrides + design tokens)
    │   ├── MapViewToggle.jsx    (modified — orange replacing blue)
    │   ├── MapViewToggle.css    (modified — design tokens)
    │   └── MapPin.jsx           (modified — popup content styling)
    ├── PhotoUpload.jsx          (modified — modal + form styling)
    └── PhotoUpload.css          (modified — design tokens)
```
