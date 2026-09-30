# CyTOS Machines Pune — React Single Page Application (SPA)

Production-ready, high-performance React application built with **React 18**, **Vite**, and **React Router DOM**. Fully optimized for mobile responsiveness, SEO indexing, and seamless deployment on **Hostinger** from GitHub.

---

## 🚀 Quick Start (Local Development)

```bash
# 1. Navigate to the project directory
cd cytos-react

# 2. Install dependencies (if not already installed)
npm install

# 3. Start local development server
npm run dev
```

The app will start at `http://localhost:3000` with instant Hot Module Replacement (HMR).

---

## 🛠️ Production Build

To test and build the production-ready distribution:

```bash
npm run build
```

This compiles optimized, minified JS, CSS, and HTML into the `/dist` directory.

---

## 🌐 Deploying to Hostinger from GitHub

You can deploy this repository to Hostinger using any of the following 3 fast methods:

### Method 1: Hostinger Git Deployment (Easiest & Recommended)

1. **Push your code to GitHub**:
   Push the `cytos-react` project to your GitHub repository (e.g., `https://github.com/your-username/cytos-website`).

2. **Open Hostinger hPanel**:
   - Go to your Hostinger Dashboard → Select your domain (`cytos.in`).
   - In the search bar or left sidebar, click **Git**.

3. **Connect Your GitHub Repository**:
   - **Repository URL**: `https://github.com/your-username/cytos-website.git`
   - **Branch**: `main` (or `master`)
   - **Install path**: Leave empty or set to `public_html`.
   - Click **Create**.

4. **Auto-Deploy Webhook**:
   - Hostinger provides a Webhook URL. Copy it.
   - In your GitHub repo: Go to **Settings** → **Webhooks** → **Add Webhook**.
   - Paste the Payload URL and select `application/json`.
   - Now, every `git push` automatically updates your Hostinger site!

---

### Method 2: GitHub Actions Automated CI/CD (Zero Manual Steps)

A pre-configured GitHub Actions workflow is included at `.github/workflows/deploy.yml`.

1. Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**.
2. Click **New repository secret** and add the following 3 secrets from your Hostinger FTP account:
   - `HOSTINGER_FTP_SERVER` (e.g. `ftp.cytos.in` or IP address from Hostinger hPanel → Files → FTP Accounts)
   - `HOSTINGER_FTP_USERNAME` (your FTP username)
   - `HOSTINGER_FTP_PASSWORD` (your FTP password)
3. Whenever you push code to GitHub:
   - GitHub Actions automatically runs `npm ci` and `npm run build`.
   - It securely uploads the compiled `/dist/` folder directly to Hostinger's `public_html`.

---

### Method 3: Direct File Manager Upload (Instant 60-Second Deploy)

1. Run `npm run build` locally.
2. Open Hostinger **File Manager** → navigate to `public_html`.
3. Select all files inside the `cytos-react/dist/` folder (including `.htaccess`) and upload them to `public_html`.
4. Your website is immediately live!

---

## 📁 Key Files & Architecture

- **`public/.htaccess`**: Essential Apache rewrite configuration for Hostinger.
  - Rewrites all dynamic routes (`/about`, `/cnc-routers-milling`, `/blog/xyz`) to `/index.html` so client-side routing works without 404 errors.
  - Enables Gzip compression and browser caching for lightning-fast PageSpeed scores.
- **`src/App.jsx`**: Main route definitions for all 8 machine categories, company pages, and blog system.
- **`src/data/blogData.js`**: Database of all 22 technical engineering guides with meta tags, FAQs, and table of contents.
- **`src/data/machinesData.js`**: Machine tool specifications, RPM, table sizes, and tolerances.
- **`src/components/QuoteModal.jsx`**: Interactive RFQ popup with direct WhatsApp consultation integration.
- **`src/components/ReviewsSlider.jsx`**: Customer testimonial carousel with touch & desktop navigation.
- **`src/components/MachineFinder.jsx`**: 3-step recommendation wizard for selecting machines.
