# Resource review

The repository maintainer owns the review cadence and can assign sources to contributors. Review the index once per calendar quarter and sooner after a vendor deprecation, breaking tool change, or scheduled CI link failure.

1. **Open a review issue.** Select **Resource review** and include affected guides, recent CI results, or upstream notices.
2. **Check access and meaning.** Open the URL and confirm the publisher and relevant passage. Inspect redirects, scopes, plan changes, publication dates, and replaced versions.
3. **Exercise affected examples.** Run the offline checks. Reproduce changed vendor steps in an approved test account where available. Record that outcome separately from link and content verification.
4. **Update the index.** Refresh the verification date for a still-valid source. Replace a moved or superseded source and update affected links. Remove a source that no longer supports the guide and revise the claim. For access failures, record the attempt in the issue and preserve the last successful date until a follow-up check.
5. **Close with evidence.** Link the merged update. Give deferred items an owner and follow-up date.

Automated HTTP checks test reachability. Editors verify that the source still supports the guide.

## Manual link checks

The Clay waterfalls and SEC EDGAR API pages opened during editorial review on November 19, 2026, and returned HTTP 403 to the automated link checker. The CI configuration excludes those two exact URLs. Open both during each quarterly review and retry the automated checks. Remove an exception when its URL passes the automated check.
