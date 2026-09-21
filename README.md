# Suvan Fora — SEO-optimized site

Static, single-page luxury-travel-advisor site for `suvanfora.com`, built to rank for classic SEO queries (luxury travel advisor, luxury vacations, HNI/UHNI travel concierge, bespoke luxury travel booking) and to be well-understood by AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude).

## CTA links

All primary CTAs point to the real Google Form: `https://forms.gle/92fgJ293j9LuYYVe7`.

There's no static "Book With Us on Fora" link, since Fora's booking link is generated per client/destination after matching — instead, the secondary CTA links to Instagram (`@suvan.fora`) as an alternate contact channel. Once a lead submits the form, send them their personalized Fora booking link directly.

## What's included

- `index.html` — the full page: semantic HTML, meta title/description, Open Graph + Twitter cards, canonical tag, and JSON-LD structured data for `TravelAgency`, `WebSite`, and `FAQPage` (the FAQ schema is what lets Google and AI engines quote your answers directly in search/chat results).
- `robots.txt` — allows all standard search crawlers **and** explicitly allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, etc.) so AI tools can discover and cite the site — this is the "AI SEO" half of the request.
- `sitemap.xml` — single-page sitemap, referenced from `robots.txt`.
- `llms.txt` — an emerging convention (llmstxt.org) that gives AI crawlers a clean, structured summary of the business, services, and how booking works, so tools like ChatGPT/Perplexity are more likely to describe the business accurately when a user asks about it.
- `CNAME` — set to `suvanfora.com`, for GitHub Pages custom-domain hosting. Delete this file if you're hosting elsewhere.

## Target keywords used on-page

luxury travel advisor, luxury vacations, HNI travel planning, UHNI travel concierge, bespoke luxury travel booking, private villa rentals, luxury resort booking, luxury honeymoon planner, private jet vacation planning, luxury safari travel, exclusive travel concierge — worked naturally into the H1, section headings, and body copy rather than stuffed into hidden text (keyword stuffing is a demotion risk with modern Google).

## Deploying

Any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages). For GitHub Pages with the included `CNAME`:
1. Enable Pages on this repo, source = this branch, root folder.
2. Point `suvanfora.com`'s DNS to GitHub Pages (A/ALIAS records per GitHub's docs).

## Content notice

No testimonials, client counts, years-in-business, or awards were invented — those numbers belong to you. If you have real ones, add a "Client Experiences" section with your actual reviews; genuine testimonials matter more for both trust and SEO than generic ones ever would. Real photos of you and your work should replace the current image-free, typography-led design when you have them (also add real `og:image` / `twitter:image` tags at that point — none are set yet because no real image exists).