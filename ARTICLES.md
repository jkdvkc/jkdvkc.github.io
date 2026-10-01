# Jarvis article workflow

This repository is a static GitHub Pages website. Jarvis can draft one useful article per week, but a draft must not publish itself: create a pull request and wait for David's explicit review and approval before merging.

## Weekly schedule and Jarvis task

The weekly recurrence belongs to Jarvis, not this static website repository. This repository contains no Jarvis scheduler or credentials, so the recurrence still needs to be enabled in Jarvis by its account owner. Configure it for one run each week and use this task instruction:

> Every week, follow `ARTICLES.md` in the `jkdvkc/jkdvkc.github.io` repository. Research one distinct, genuinely useful IT question for private customers or small businesses in Winterthur / the Ostschweiz; use reliable primary sources and do not invent facts. Create a German-Swiss draft article under `ratgeber/<slug>/index.html` with `noindex`, run the documented checks, and open a pull request from a new `jarvis/article-YYYY-MM-DD-<slug>` branch. In the PR, state sources, target reader, verified facts, claims needing David's confirmation, and what is original. Do not push to `main`, merge, or enable auto-merge. Ask David to review and approve before the article can be published.

## Weekly routine

1. Pick one question real private customers or small businesses in Winterthur / the Ostschweiz ask. Prefer a concrete answer over a generic keyword-oriented topic.
2. Check existing pages and articles first; do not rewrite the same topic with a new date or location name.
3. Draft one German (`de-CH`) article under `ratgeber/<short-topic-slug>/index.html`, linked from `ratgeber/index.html` and included in `sitemap.xml` only after it is approved and published.
4. Create a branch named `jarvis/article-YYYY-MM-DD-short-topic` and open a pull request. Mark it as a draft if the factual review is incomplete. Never push straight to `main`, merge, or publish without David's approval.
5. In the PR body, include the search question, intended audience, source links, claims that require David's confirmation, and a concise description of what is original/useful in the article.
6. David reviews factual claims, service scope, spelling, safety advice, privacy implications, Swiss context, internal links and metadata; he requests changes or approves and merges.

## German (Swiss) style and content standard

- Write clear, natural Swiss Standard German (`de-CH`), using Swiss spelling (`ss`, not `ß`); address readers consistently with `Sie` on customer-facing pages.
- Give a direct answer near the beginning, then explain steps, limitations, risks and when an expert should inspect the device.
- Add real experience only when David supplied or verified it. Never invent case studies, customer stories, qualifications, dates, locations, price guarantees, service guarantees or performance statistics.
- Do not imply David is an authorised service centre, offers enterprise SLAs, professional forensic recovery, cybersecurity incident response, data-protection certification, or a particular software/hardware integration unless he confirms it.
- Cite reliable primary documentation for technical claims and date-sensitive instructions. Quote sparingly; summarize in original language and keep source links in the article.
- Avoid doorway pages, mass-generated location variants, keyword stuffing, fake reviews, self-awarded star ratings and AI-generated filler. A useful article must work for the reader even without a search engine.
- Do not submit confidential customer data, passwords, device dumps, contact information or unpublished business details to any external AI service.

## Article template

```html
<!doctype html>
<html lang="de-CH">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Specific question and useful outcome | Swiss Net Tech</title>
  <meta name="description" content="A factual one-sentence summary of the answer.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://jakoda.ch/ratgeber/short-topic-slug/">
</head>
<body>
  <main>
    <nav><a href="/ratgeber/">← IT-Ratgeber</a></nav>
    <article>
      <h1>Answer the reader's actual question</h1>
      <p>Give a brief, direct answer and state when this guidance applies.</p>
      <p><small>Geprüft von David Jakoda · Veröffentlicht: YYYY-MM-DD</small></p>
      <h2>Steps or explanation</h2>
      <!-- Original, practical and reviewed content -->
      <h2>Wann professionelle Hilfe sinnvoll ist</h2>
      <p>Describe limits honestly; link to an actually offered service.</p>
      <h2>Quellen</h2>
      <ul><li><a href="https://authoritative-source.example/">Primary technical source</a></li></ul>
    </article>
    <p><a href="/privat/">Private IT-Hilfe</a> · <a href="/unternehmen/">IT-Support für KMU</a></p>
  </main>
</body>
</html>
```

The template starts with `noindex` so a new, unreviewed draft cannot be indexed if accidentally deployed. Keep all drafts in PR branches only; GitHub Pages production serves `main`, so no preview or deployment from draft branches is configured. In the publication PR, David reviews the final changes before approving and merging. As part of the same PR, remove `noindex` (use `index, follow` or omit the robots directive), add the article to the hub and sitemap, and verify its canonical URL. Do not enable auto-merge or publish directly from Jarvis.

## Pre-PR checklist

- [ ] One real user question and a distinct answer; no near-duplicate or location-swapped doorway page.
- [ ] All service claims match current pages and have been confirmed by David.
- [ ] Every material technical or time-sensitive claim has a primary source and has been checked.
- [ ] No fabricated measurements, reviews, customer totals, exact performance claims or legal promises.
- [ ] Swiss German spelling, consistent `Sie`, concise title and non-duplicative meta description.
- [ ] Correct canonical path, useful internal links, accessible headings and link text.
- [ ] Draft is `noindex`; it is removed from `noindex` and added to hub/sitemap only as part of an approved publication PR.
- [ ] No home address, private customer data, credentials or secrets were added.
- [ ] The pull request requests David's explicit approval and does not auto-merge.
