# AI and search implementation

Public content is static German-Swiss HTML. Main content does not require JavaScript. Services link to a stable business identity via JSON-LD @id; WebSite, WebPage and BreadcrumbList describe the site and navigation. New service pages use only services already stated on the homepage. No ratings, public shop address, prices or opening hours have been invented.

robots.txt explicitly allows OAI-SearchBot (ChatGPT search). The previous universal allow rule remains unchanged, including existing training-crawler policy. Check hosting/firewall access separately: robots permissions alone cannot guarantee access or inclusion.

There is no hidden AI prompt, guaranteed-ranking code or special AI schema. Google does not use llms.txt for ranking, so it is not added as a ranking tactic. Maintain useful visible facts and update JSON-LD with them.

Validation: run python -m unittest discover -s tests -v. After approval/deployment, verify jakoda.ch in Search Console, submit sitemap.xml, inspect canonical/indexing status and check eligibility/opt-in for Google generative search under the current Search Console settings. Measure organic leads and queries over time. Ads query history is not total regional search volume.

Sources checked 2026-10-02:
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.openai.com/api/docs/bots

## Owner-confirmed update, 2026-10-03

The brand is now Jakoda Dienstleistungen (short name Jakoda). David explicitly confirmed broad IT support plus programming, integrations, AI and automation. The homepage has visible matching identity facts, a named service catalog, a stable founder Person identity and contact point. New WLAN/network, Microsoft 365, and programming/integration pages are in the sitemap and linked from the homepage and relevant existing pages. The legacy directory wording Jakoda IT Dienstleistungen remains an alternate name to clarify the same provider; no unverified directory profile URLs or review counts were added.

Google and OpenAI primary guidance was rechecked on 2026-10-03. Code improvements do not update business-directory accounts, secure reviews, or guarantee inclusion in generated answers. The pasted AI ranking contained duplicate companies and is not a visibility measurement. The owner-facing handoff lists profile and Search Console work separately.
