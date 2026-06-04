# Sprint 13: Login & Signup Pages

**Assignee:** Ho Lok
**Goal:** Restyle the Login and Signup pages using the design system tokens from Sprint 12. Both pages should feel visually consistent — same card layout, same input styling, same error handling patterns.
**Dependencies:** Sprint 12 (design system + navbar) must be merged first. No dependency on Sprints 14–16 — can run in parallel with them.
**Parallel notes:** This sprint only modifies `LoginPage.jsx`, `LoginPage.css`, `signup.jsx`, and `signup.css`. No conflicts expected with other sprints.

---

## Before You Start

**Check the README.md** at the project root for instructions on setting up the dev environment and running the app (both frontend and backend).

### Git Workflow

Your typical workflow once you receive a sprint should be:

1. Start on the `main` branch
2. `git pull` + `npm install` (in both root and `server/`) to make sure you are up to date
3. `git switch -c <your-branch>` — e.g. `yourname/sprint13`
4. Do `git add` & `git commit` while working (frequently + descriptive messages)
5. `git push origin <your-branch>` to push your local branch to GitHub
6. When you are done with your sprint, pull from main once more to resolve any merge conflicts early
7. Create a pull request on GitHub with a descriptive description, and then we can merge it safely!

---

## Background (read this first)

The Login and Signup pages currently work but use hardcoded colors and inconsistent styling. This sprint applies the design system established in Sprint 12 — CSS variables for colors, the `.input` class for form fields, `.btn .btn-primary` for submit buttons, and a centered `.card` container for the form.

Both pages should end up looking like siblings — same card dimensions, same spacing, same error treatment. The only differences are the title text, the fields shown, and the footer link direction.

**Key concepts:**
- **Design tokens** — all colors, spacing, radii, and shadows come from CSS variables defined in `:root` (Sprint 12). Reference them as `var(--token-name)`.
- **Shared classes** — `.btn`, `.btn-primary`, `.input`, `.card` are defined in `App.css` (Sprint 12). Use them instead of writing custom button/input styles.
- **Error UX** — errors should be visually distinct (red text on light red background) and should disappear when the user starts correcting their input.

**Useful resources:**
- [CSS custom properties (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- Check `src/App.css` for all available shared classes (`.btn-primary`, `.input`, `.card`, etc.)

---

## Tasks

### 1. Restyle the Login page

**Files:** `src/pages/LoginPage.jsx` + `src/pages/LoginPage.css`

- [ ] **Page background:** `var(--color-bg-page)` — the light gray page background
- [ ] **Centered card container:**
  - Use `.card` class as a base
  - `max-width: 420px`, centered horizontally with `margin: 0 auto`
  - Generous padding: `var(--space-8)` or `var(--space-10)`
  - `box-shadow: var(--shadow-md)` for a medium-depth card
  - Orange accent: add a `border-top: 3px solid var(--color-primary)` for a subtle orange stripe at the top of the card
- [ ] **Title:** "Welcome back" in `var(--text-2xl)`, `var(--font-semibold)`, `var(--color-text)`
- [ ] **Form fields:**
  - Labels above each input: `font-size: var(--text-sm)`, `font-weight: var(--font-medium)`, `color: var(--color-text)`
  - Inputs use the `.input` class (defined in Sprint 12's `App.css`)
  - Vertical gap between fields: `var(--space-4)` (16px)
- [ ] **Submit button:**
  - Use `btn btn-primary` classes
  - Full width: `width: 100%`
  - Margin top: `var(--space-6)` to separate from the last field
- [ ] **Error display:**
  - `color: var(--color-error)` text
  - `background-color: var(--color-error-light)` background
  - `border-radius: var(--radius-md)`, padding: `var(--space-3)`
  - Appears above the form or below the title
  - Error should clear when the user starts typing again (add an `onChange` handler that clears the error state)
- [ ] **Footer link:** Below the card or at the card bottom:
  - Text: "Don't have an account? **Sign up**"
  - "Sign up" is a `<Link>` to `/signup` styled with `color: var(--color-secondary)`
  - `font-size: var(--text-sm)`, centered

**How to test:**
1. Navigate to `/login` — card should be centered with orange top border
2. Enter valid credentials → redirects to `/map`
3. Enter wrong email/password → styled error message appears (red text, light red background)
4. Start typing after an error → error message should disappear
5. Submit with empty fields → validation feedback shown
6. Resize to 375px → card should shrink gracefully, no horizontal overflow

### 2. Restyle the Signup page

**Files:** `src/pages/signup.jsx` + `src/pages/signup.css`

- [ ] **Same card layout as Login** for visual consistency:
  - Same `max-width: 420px`, same padding, same shadow, same orange top border
  - `var(--color-bg-page)` background
- [ ] **Title:** "Create your account" in `var(--text-2xl)`, `var(--font-semibold)`
- [ ] **Form fields:** Username, Email, Password — all with labels and `.input` class
- [ ] **Submit button:** `btn btn-primary`, full width
- [ ] **Error display:** Same pattern as Login (red text, light red background, clears on typing)
- [ ] **Footer link:** "Already have an account? **Log in**" with link to `/login` in `var(--color-secondary)`

**How to test:**
1. Navigate to `/signup` — card should look visually identical to Login (same dimensions, same accent)
2. Fill in all fields → account created, auto-login, redirect to `/map`
3. Use an existing email → styled error message shown
4. Use an existing username → styled error message shown
5. Submit with empty fields → validation feedback
6. Click "Log in" link → navigates to `/login`
7. Resize to 375px → card shrinks gracefully

### 3. Cross-page consistency check

- [ ] Put Login and Signup side by side (two browser tabs) — verify:
  - Same card width, padding, shadow
  - Same input height and border style
  - Same button color, size, and hover effect
  - Same error message styling
  - Same footer link style
- [ ] Tab through all form fields using keyboard → focus ring should be orange (from `.input:focus`)
- [ ] Navigate between Login ↔ Signup via footer links → transitions should feel natural

---

## Bug Testing Checklist

- [ ] Login with valid credentials → redirects to /map
- [ ] Login with wrong email/password → styled error message, form fields NOT cleared
- [ ] Empty form submit → appropriate validation feedback
- [ ] Signup with all valid fields → account created, auto-login, redirect to /map
- [ ] Signup with existing email → error message shown
- [ ] Signup with existing username → error message shown
- [ ] Link from login → signup works and vice versa
- [ ] Tab/keyboard navigation through all form fields and buttons
- [ ] Responsive: card looks good at 1200px, 768px, 375px
- [ ] Error message disappears when user starts typing again (or on next submit)

---

## Merge Conflict Notes

**Very low conflict risk.** This sprint only modifies Login and Signup files. No other sprint should be touching these pages. If somehow there's a conflict in `App.jsx` routes (unlikely), just keep all routes.

---

## Deliverables Checklist

- [ ] Login page uses `.card`, `.input`, `.btn-primary` from Sprint 12
- [ ] Login page has `var(--color-bg-page)` background, orange top border accent
- [ ] Login error messages use `var(--color-error)` + `var(--color-error-light)`
- [ ] Signup page matches Login layout (same card, same spacing, same patterns)
- [ ] Footer links navigate between Login ↔ Signup, styled with `var(--color-secondary)`
- [ ] Both pages are responsive (no overflow at 375px)
- [ ] No hardcoded color values in LoginPage.css or signup.css — all use `var(--*)` tokens
- [ ] Keyboard navigation works through all fields and buttons

## File Structure

```
src/
└── pages/
    ├── LoginPage.jsx            (modified — restyle with design tokens)
    ├── LoginPage.css            (modified — replace hardcoded styles)
    ├── signup.jsx               (modified — restyle with design tokens)
    └── signup.css               (modified — replace hardcoded styles)
```
