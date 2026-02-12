# Mitria Website — Eleventy + Decap CMS

## What This Is

A static site built with [Eleventy](https://www.11ty.dev/) and [Decap CMS](https://decapcms.org/). Once deployed, the client can edit all content (experiences, projects, countries, blog posts, site settings) through a visual admin panel at `/admin`.

## Deployment Steps

### 1. Push to GitHub

Create a new repository on GitHub (e.g. `mitria-site`), then:

```bash
cd mitria-cms
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mitria-site.git
git push -u origin main
```

### 2. Connect to Netlify

1. Go to [app.netlify.com](https://app.netlify.com) and sign in
2. Click **Add new site** > **Import an existing project**
3. Select GitHub and authorize access
4. Choose the `mitria-site` repository
5. Netlify will auto-detect the build settings from `netlify.toml`:
   - Build command: `npx @11ty/eleventy`
   - Publish directory: `_site`
6. Click **Deploy site**

### 3. Enable Netlify Identity (required for CMS login)

1. In Netlify dashboard, go to **Site settings** > **Identity**
2. Click **Enable Identity**
3. Under **Registration**, select **Invite only**
4. Under **External providers**, optionally add Google for easier login
5. Go to **Identity** > **Services** > **Git Gateway** and click **Enable**
6. Go to **Identity** tab and click **Invite users** — add the client's email (e.g. `info@mitria.org`)

### 4. Enable Form Notifications

1. Go to **Site settings** > **Forms** > **Form notifications**
2. Add an email notification for the `contact` form → send to `info@mitria.org`
3. Add an email notification for the `subscribe` form if desired

### 5. Custom Domain (optional)

1. Go to **Site settings** > **Domain management** > **Add custom domain**
2. Enter `mitria.org` (or whatever domain)
3. Update DNS records at the domain registrar as Netlify instructs
4. Netlify provisions an SSL certificate automatically

## How the Client Uses the CMS

1. Visit `https://your-site.netlify.app/admin/`
2. Log in with the email that was invited in step 3
3. The admin panel shows editable collections:
   - **Experiences** — add/edit/delete trip descriptions
   - **Projects** — add/edit/delete Project Zomia entries
   - **Blog Posts** — write and publish blog entries
   - **Countries** — edit country pages including projects, partners, seasons
   - **Pages** — edit homepage and about page text and images
   - **Site Settings** — change site name, tagline, email, social links
4. After editing, click **Publish** — Netlify rebuilds the site automatically (takes ~30 seconds)

## How to Upload Images

In the CMS, any image field has an upload button. Images are stored in `src/images/` in the repository. The client can also use external URLs (like Unsplash links) by pasting them directly.

## Local Development

```bash
npm install
npm start
```

Site runs at `http://localhost:8080` with live reload.

## File Structure

```
src/
  _data/          Site-wide data (settings, partners)
  _includes/      Layout templates
  admin/          CMS admin panel
  blog/           Blog post markdown files
  countries/      Country page markdown files
  experiences/    Experience markdown files
  projects/       Project markdown files
  images/         Uploaded images
  styles.css      All styles
  *.njk           Page templates (home, about, contact, etc.)
```

## Editing Styles

All colors are defined as CSS custom properties at the top of `styles.css`:

```css
--color-primary: #6B7F5E;       /* sage green */
--color-primary-dark: #4A5940;
--color-accent: #C4A882;        /* warm tan */
--color-bg: #FAFAF6;            /* cream */
```

Change these to update the entire color scheme.
