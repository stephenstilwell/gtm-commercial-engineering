# Resource review

The repository maintainer owns the review cadence and can assign sources to contributors. Review the citation index and resource catalog once per calendar quarter and sooner after a license change, vendor deprecation, breaking tool change, or scheduled CI link failure.

1. **Open a review issue.** Select **Resource review** and include affected guides, recent CI results, or upstream notices.
2. **Check access and meaning.** Open the URL and confirm the publisher and relevant passage. Inspect redirects, scopes, plan changes, publication dates, and replaced versions.
3. **Exercise affected examples.** Run the offline checks. Reproduce changed vendor steps in an approved test account where available. Record that outcome separately from link and content verification.
4. **Update the index.** Refresh the verification date for a still-valid source. Replace a moved or superseded source and update affected links. Remove a source that no longer supports the guide and revise the claim. For access failures, record the attempt in the issue and preserve the last successful date until a follow-up check.
5. **Close with evidence.** Link the merged update. Give deferred items an owner and follow-up date.

Automated HTTP checks test reachability. Editors verify that the source still supports the guide.

## Review a catalog entry

1. Inspect the exact upstream license file and the OSI listing for open-source entries. Check enterprise directories, separately licensed components, and hosted edition terms before updating classification. Record the boundary in the entry.
2. Open the official pricing or access page, confirm the relevant edition and status, and check public repository activity where available. Treat archived or unconfirmed entries as review decisions. Remove an entry from the curated catalog when there is no longer evidence it is useful and available.
3. Verify that the linked handbook exercise matches the entry’s job. Replace any vendor claim that depends on access you could not confirm with a narrower description.
4. Update the catalog JSON, date the successful review, and regenerate the views with `python scripts/catalog.py`. Review the underlying sources and the rendered result in the pull request.

## Manual link checks

The Clay waterfalls and SEC EDGAR API pages opened during editorial review on November 19, 2026, and returned HTTP 403 to the automated link checker. The CI configuration excludes those two exact URLs. Open both during each quarterly review and retry the automated checks. Remove an exception when its URL passes the automated check.
