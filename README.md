# Swiss Net Tech website

Static German-Swiss website for IT support in Winterthur and the Ostschweiz, deployed through GitHub Pages at `jakoda.ch`.

## Structure

- `index.html` — main local IT-support page.
- `privat/`, `unternehmen/`, `pc-reparatur/`, `pc-einrichtung/`, `ki-automation/` — focused service landing pages.
- `ratgeber/` — reviewed IT articles; see [`ARTICLES.md`](ARTICLES.md) for Jarvis's draft-and-approval workflow and [`LOCAL-SEO.md`](LOCAL-SEO.md) for account-side local SEO tasks.
- `impressum/`, `datenschutz/` — business contact and privacy information; review legal wording and personal details before launch.
- `vorschlag/` — demonstration pages for client prospects, intentionally `noindex` and excluded from the sitemap.
- `robots.txt`, `sitemap.xml` — crawler instructions and the indexable site URL list.

## Local checks

Run the standard-library metadata, sitemap and demo-indexing checks from the repository root:

```sh
python -m unittest discover -s tests -v
```

GitHub Pages serves files from the repository root; no package installation or build step is required. Every article and service page should have a self-referencing canonical, useful German content, and only verified facts. Jarvis must use a branch and pull request; do not publish or merge without David's explicit approval.
