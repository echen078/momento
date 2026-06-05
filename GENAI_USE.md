# Generative AI Use Disclosure

This file documents generative AI assistance used while creating Momento following the course policy format.

```js
// [GenAI Use] Prompt: "..."
// [GenAI Use] LLM Response Start
// ...
// [GenAI Use] LLM Response End
// [GenAI Use] Reflection: "..."
// [GenAI Use] Ownership: "...%"
```

---

# echen078-Authored Feature Disclosures
## Notes

Some prompts below are reconstructed from memory because the exact original chat transcripts were not preserved. The descriptions are intended to accurately represent the type of assistance received and how the generated output was used.

All generated code, suggestions, and documentation were reviewed, modified, tested, and integrated into the project before being committed.

## Overall Ownership Estimate

I feel ownership over approximately 75% of the code I personally committed.

Generative AI was primarily used for implementation guidance, debugging support, React/Express patterns, test generation, and documentation drafting. I reviewed all generated outputs, adapted them to the existing codebase, and verified behavior through manual testing and project requirements before committing changes.


## Sprint 3 Map Integration

```js
// [GenAI Use] Prompt:
// "Sprint 3 — Frontend Map Integration (Ellen). Set up an interactive Leaflet map in our Vite + React app: install react-leaflet and leaflet, import leaflet.css in main.jsx, and fix the default marker icon issue with Vite (L.Icon.Default.mergeOptions with imported icon/shadow images). Build src/components/Map/Map.jsx using MapContainer and TileLayer centered on Los Angeles [34.0522, -118.2437] at zoom 12 with OpenStreetMap tiles. Add a useMapEvents helper inside MapContainer that logs lat/lng on map click. Create a reusable MapPin.jsx component (Marker + Popup, accepts position and children). Demo with 4–5 hardcoded LA pins (Santa Monica Pier, Griffith Observatory, UCLA, Grand Central Market). Style with Map.css so the map is full viewport (100% width, 100vh) with no overflow glitches."

// [GenAI Use] LLM Response Start
// The LLM suggested using React Leaflet components such as MapContainer, TileLayer, Marker, Popup, and useMapEvents. It also suggested creating a reusable MapPin component, importing Leaflet CSS correctly, and styling the map container.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I adapted the suggestions to the existing project structure, created the Map and MapPin components, integrated them into the application, and tested the functionality locally.

// [GenAI Use] Ownership: 70%
//
// I feel ownership over approximately 70% of the map integration code I committed. AI provided guidance on React Leaflet usage and structure, but I integrated the components, adjusted styling and configuration, and verified functionality through testing.
```

---

## Sprint 8 Public Photos and Community Explore Feed

```js
// [GenAI Use] Prompt:
// "Sprint 8 — Public Photos & Community Feed (Ellen). Backend: add optionalAuth middleware in auth.js (valid token sets req.user, missing/invalid token still calls next without 401). Update uploadPhoto to read isPublic from multipart form data (compare to string 'true'). Add getPublicPhotos in photoController.js — query isPublic: true, paginate with page/limit, sort by createdAt desc, populate user username, return { photos, page, totalPages, totalPhotos }. Route GET /api/photos/public before /:id. Change GET /api/photos/:id to optionalAuth so public photos are viewable without login; private photos return 403 for non-owners. Frontend: create ExplorePage.jsx/css — responsive grid of public photos (thumbnail, caption, username, date), Load More pagination, link to /photos/:id, no login required. Add /explore route in App.jsx (not ProtectedRoute) and always-visible Explore link in Navbar. Write tests/test_sprint8_public_photos.py covering isPublic upload, public listing, pagination, optionalAuth access rules. Do NOT add community pins to Map.jsx — Sprint 9 handles heatmap."

// [GenAI Use] LLM Response Start
// The LLM suggested public-photo routes, optional authentication, paginated API responses, React state management, and an Explore page UI for browsing public content.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I reviewed the authorization requirements, integrated the feature with existing backend and frontend patterns, and manually verified functionality.

// [GenAI Use] Ownership: 80%
//
// I feel ownership over approximately 80% of the public-photo/community-feed code I committed. AI assisted with implementation ideas, but I integrated the feature with the existing codebase and validated behavior myself.
```

---

## Sprint 8 Public Photo E2E Tests

```js
// [GenAI Use] Prompt:
// "Sprint 8 Task 8 — Write tests/test_sprint8_public_photos.py following test_sprint4_photos.py and conftest.py fixtures. Cover: upload with isPublic=true → 201 isPublic true; upload without isPublic → default false; GET /api/photos/public returns { photos, page, totalPages, totalPhotos } with populated username; private photos excluded; pagination ?page=1&limit=2; public list works without auth; GET /api/photos/:id for public photo without auth → 200; private photo without auth → 403; private photo with owner auth → 200."

// [GenAI Use] LLM Response Start
// The LLM suggested pytest test cases covering authentication, uploads, public-photo retrieval, private-photo protection, and robust assertions.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I reviewed the tests, adjusted assertions, integrated them with the existing test suite, and confirmed that they exercised actual API behavior.

// [GenAI Use] Ownership: 65%
//
// I feel ownership over approximately 65% of the test code I committed. AI generated initial testing patterns, but I modified and validated the tests before submission.
```

---

## Public/Private Sharing Controls in Upload and Photo Detail

```js
// [GenAI Use] Prompt:
// "Reconstructed/generalized prompt: Integrate public/private sharing across the photo upload flow and photo detail view. Users should be able to choose whether a photo is public, owners should be able to edit visibility, and the UI should clearly show public/private status."

// [GenAI Use] LLM Response Start
// The LLM suggested passing an isPublic field through upload forms, updating visibility through API routes, displaying public/private badges, and restricting edit controls to owners.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I adapted these ideas to the existing Photo model and UI components while verifying authorization behavior and owner-only controls.

// [GenAI Use] Ownership: 85%
//
// I feel ownership over approximately 85% of this feature. AI suggested a general implementation approach, but I adapted it to the project architecture and verified final behavior.
```

---

## Upload and Image Handling Improvements

```js
// [GenAI Use] Prompt:
// "Reconstructed/generalized prompt: Improve Momento's upload flow and backend image handling. Support common phone image formats, create the uploads directory if needed, normalize images when possible, and return clearer upload error messages."

// [GenAI Use] LLM Response Start
// The LLM suggested expanding upload validation, ensuring upload directories exist, improving error handling, and supporting additional image formats.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I reviewed the suggestions, integrated them into the existing upload pipeline, and verified expected upload scenarios.

// [GenAI Use] Ownership: 70%
//
// I feel ownership over approximately 70% of these changes. AI suggested approaches, while I adapted them to the project's existing upload architecture and tested the final implementation.
```

---

## Sprint 15 Gallery, Photo Detail & Search Restyle

```js
// [GenAI Use] Prompt:
// "Sprint 15 — Gallery, Photo Detail & Search Restyle (Ellen). After Sprint 12 design system is merged, restyle GalleryPage, SearchBar, PhotoDetailPage, PhotoDetailModal, and TagInput using shared tokens from App.css (var(--color-*), .card, .tag, .input, .btn, .btn-primary, .btn-danger, .overlay, .modal). Gallery: var(--color-bg-page) background, responsive auto-fill grid (minmax 300px, 3→2→1 columns), .card photo cards with cover images, orange .tag pills on cards (click-to-filter must still work), empty state message. SearchBar: .input with orange focus ring, date inputs matching .input, active filter chips with var(--color-primary-light) bg and × remove buttons, Clear all link, result count in var(--color-text-secondary). PhotoDetailPage: centered .card max-width 900px; PhotoDetailModal: .overlay + .modal, owner edit/delete controls, public/private badge pills. TagInput: replace old blue chips with orange .tag pills, × hover turns red, suggestions use gray hover states. Preserve existing URL tag sync (?tags=food,beach) and all search/filter/delete behavior — styling only, no logic regressions."

// [GenAI Use] LLM Response Start
// The LLM suggested React state-management patterns, filter handling, UI improvements, modal editing flows, and responsive layout refinements.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I integrated the ideas into existing gallery and photo-detail components and manually tested the resulting user experience.

// [GenAI Use] Ownership: 85%
//
// I feel ownership over approximately 85% of this work. AI provided implementation suggestions, but I integrated them into the existing application and verified functionality.
```

---

## Explore Revamp, Likes, and View-on-Map Flow

```js
// [GenAI Use] Prompt:
// "Reconstructed/generalized prompt: Improve the Explore page by adding community interactions and navigation. Add likes to public photos, mark my own uploads in the feed, allow owners to edit their own photos, and add a View on Map action from the photo detail modal."

// [GenAI Use] LLM Response Start
// The LLM suggested backend support for likes, frontend state management, conditional rendering for owner actions, and navigation between photo details and the map.
// [GenAI Use] LLM Response End

// [GenAI Use] Reflection:
// I validated authorization rules, integrated backend and frontend updates, and refined the user experience before committing the changes.

// [GenAI Use] Ownership: 85%
//
// I feel ownership over approximately 85% of this feature. AI assisted with implementation ideas, while I integrated the functionality and validated behavior across the application.
```
