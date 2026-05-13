# Momento — AI Agent Project Guide

## What Is Momento?

Momento is a photo-centric mapping app for Los Angeles. It serves two purposes:

1. **Personal memory vault** — Users upload photos, pin them to map locations, and build a visual record of everywhere they've explored in LA. A personal heatmap shows which neighborhoods they've visited most.
2. **Community discovery** — A community heatmap aggregates public photo activity across all users, showing where people are actually going. Users can toggle between weekly, monthly, and yearly views to spot trends, then browse authentic photos from any area before deciding to visit.

## Architecture Overview

```
momento/                  # Monorepo — frontend at root, backend in server/
├── src/                  # React frontend (Vite)
│   ├── main.jsx          # Entry point, Leaflet CSS + icon fix
│   ├── App.jsx           # Root component
│   └── components/
│       └── Map/
│           ├── Map.jsx       # MapContainer centered on LA, demo pins
│           ├── MapPin.jsx    # Reusable Marker + Popup component
│           └── Map.css       # Full-viewport map styling
├── server/               # Express backend
│   ├── index.js          # Server entry, middleware, route mounting
│   ├── config/
│   │   └── db.js         # MongoDB Atlas connection via Mongoose
│   ├── models/
│   │   └── User.js       # User schema (username, email, hashed password)
│   ├── controllers/
│   │   └── authController.js  # register, login, getMe
│   ├── routes/
│   │   └── authRoutes.js      # POST /register, POST /login, GET /me
│   └── middleware/
│       └── auth.js       # JWT verification middleware
└── sprints/              # Sprint specs (task breakdowns per feature)
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend framework | React 19 |
| Build tool | Vite |
| Mapping | Leaflet + React Leaflet |
| Routing (planned) | React Router |
| HTTP client (planned) | Axios |
| Backend framework | Express 5 |
| Database | MongoDB Atlas via Mongoose |
| Authentication | JWT (jsonwebtoken) + bcryptjs |
| File uploads (planned) | Multer (local disk storage) |

## API Endpoints

### Implemented

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/health` | No | Health check |
| POST | `/api/auth/register` | No | Create account (username, email, password) |
| POST | `/api/auth/login` | No | Login, returns JWT |
| GET | `/api/auth/me` | Yes | Get current user profile |

### Planned (Sprint 4)

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/photos` | Yes | Upload photo with lat/lng, caption, tags |
| GET | `/api/photos` | Yes | Get current user's photos |
| GET | `/api/photos/:id` | Yes | Get single photo |
| DELETE | `/api/photos/:id` | Yes | Delete photo (owner only) |

## Database Schemas

### User (implemented)

```js
{
  username: String,     // required, unique
  email: String,        // required, unique, lowercase
  password: String,     // required, bcrypt hashed
  createdAt: Date       // default: now
}
```

### Photo (planned — Sprint 4)

```js
{
  user: ObjectId,       // ref: User, required
  imageUrl: String,     // required, path to stored file
  location: {
    lat: Number,        // required
    lng: Number         // required
  },
  caption: String,      // optional
  tags: [String],       // e.g. ["cafe", "hiking"]
  isPublic: Boolean,    // default: false — controls community visibility
  createdAt: Date       // default: now
}
```

## Authentication Flow

1. User registers or logs in via `/api/auth/register` or `/api/auth/login`
2. Server returns a JWT containing `{ id: user._id }`
3. Client stores the JWT and sends it as `Authorization: Bearer <token>` on protected requests
4. The `auth` middleware (`server/middleware/auth.js`) verifies the token and attaches `req.user` with the user's ID

## Key Features & How They Connect

### Map Views & Toggle System

The map is the core UI. Users need to toggle between different views:

- **My Photos** — Shows the user's own photo pins on the map (default view)
- **Personal Heatmap** — Overlay showing the user's own exploration density
- **Community Heatmap** — Aggregated public photo activity from all users, with time range toggles:
  - **Weekly** — Photos from the past 7 days
  - **Monthly** — Photos from the past 30 days
  - **Yearly** — Photos from the past 365 days

These views should be togglable via a UI control (e.g., a sidebar toggle or segmented button). The personal pins view and heatmap views can coexist or be exclusive depending on implementation.

### Personal Vault Flow

```
User uploads photo → selects location on map → photo saved with coordinates
                                                      ↓
                              Photo appears as pin on personal map
                                                      ↓
                              Personal heatmap reflects updated density
```

### Community Discovery Flow

```
Users mark photos as public (isPublic: true)
          ↓
Backend aggregates public photos by time range (week/month/year)
          ↓
Community heatmap renders density of public photo activity
          ↓
User taps a heatmap zone → browses public photos from that area
```

## Environment Setup

### Backend (`server/`)

Requires a `.env` file:

```env
PORT=5000
MONGO_URI=mongodb+srv://<username>:<password>@momento-prod.4mkxecn.mongodb.net/?appName=momento-prod
JWT_SECRET=<random-string>
```

- MongoDB credentials are managed in [MongoDB Atlas](https://cloud.mongodb.com/) under Database Access
- Generate a JWT secret with: `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`

### Frontend (project root)

No environment variables needed currently. Runs on Vite's dev server (default port 5173).

### Running the App

```bash
# Terminal 1: Backend
cd server && npm install && npm run dev

# Terminal 2: Frontend (from project root)
npm install && npm run dev
```

## Implementation Status

| Milestone | Feature | Status |
|---|---|---|
| 1 | Backend server + MongoDB setup (Sprint 1) | Done |
| 1 | User auth — register, login, JWT (Sprint 2) | Done |
| 1 | Interactive map with React Leaflet (Sprint 3) | Done |
| 1 | Photo upload API — multer, CRUD endpoints (Sprint 4) | Not started |
| 1 | Frontend routing + auth pages (Sprint 5) | Not started |
| 2 | Personal exploration heatmap | Not started |
| 2 | Photo tagging system | Not started |
| 2 | Search/filter personal photos | Not started |
| 3 | Community heatmap (weekly/monthly/yearly toggle) | Not started |
| 3 | Browse public photos on map | Not started |
| 3 | Photo sharing toggle (public/private) | Not started |
| 3 | UI polish + performance | Not started |

## Conventions & Patterns

- **File structure**: Group by feature (e.g., `components/Map/`). Backend follows MVC pattern (`models/`, `controllers/`, `routes/`).
- **Styling**: Plain CSS files co-located with components. No CSS framework currently in use.
- **API pattern**: Express routes delegate to controller functions. Auth-protected routes use the `auth` middleware.
- **Error handling**: Controllers use try/catch and return appropriate HTTP status codes (400, 401, 403, 404, 500).
- **Module system**: Backend uses CommonJS (`require`/`module.exports`). Frontend uses ES modules (`import`/`export`).

## Sprint Specs

Detailed task breakdowns for each feature are in the `sprints/` folder. These contain step-by-step instructions, background context, and deliverable checklists. Always check the relevant sprint file before implementing a feature.
